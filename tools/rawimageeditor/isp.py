# =============================================================
# Import the libraries
# =============================================================
import numpy as np  # array operations
import math         # basing math operations
from matplotlib import pylab as plt
import time         # measure runtime
import tools.rawimageeditor.utility
import tools.rawimageeditor.debayer
from tools.rawimageeditor.rawImage import RawImageInfo, RawImageParams
import sys          # float precision
from scipy import signal        # convolutions
from scipy import interpolate   # for interpolation

pipeline_dict = {
        "raw":          0,
        "black level":  1,
        "BLC":          1,
        "rolloff":      2,
        "ABF":          3,
        "demosaic":     4,
        "awb":          5,
        "AWB":          5,
        "ccm":          6,
        "CCM":          6,
        "gamma":        7,
        "LTM":          8,
        "advanced chroma enhancement":  9,
        "ACE":                          9,
        "wavelet denoise":              10,
        "WNR":                          10,
        "adaptive spatial filter":      11,
        "ASF":                          11,
        "bad pixel correction":         12
    }

def black_level_correction(raw: RawImageInfo, params: RawImageParams):
    """
    function: black_level_correction
    brief: subtracts the black level channel wise
    input: raw:RawImageInfo() params:RawImageParams()
    根据不同的bit_depth，需要对black_level进行移位
    """
    black_level = params.get_black_level()
    bayer_pattern = raw.get_bayer_pattern()
    bit_depth = raw.get_raw_bit_depth()
    raw_data = raw.get_raw_data()
    if(raw_data is None):
        params.set_error_str("RAW data is None")
        return None

    if (bit_depth < 14):
        black_level = np.left_shift(black_level, 14 - bit_depth)

    if(raw.get_color_space() == "raw"):
        black_level = resort_with_bayer_pattern(black_level, bayer_pattern)
        ret_img = RawImageInfo()
        ret_img.create_image('after black level', raw_data.shape)
        # create new data so that original raw data do not change

        # bring data in range 0 to 1
        # list[i:j:2] 数组从取i 到 j 但加入了步长 这里步长为2
        # list[::2 ] 就是取奇数位，list[1::2]就是取偶数位
        ret_img.data[::2, ::2] = raw_data[::2, ::2] - black_level[0]
        ret_img.data[::2, 1::2] = raw_data[::2, 1::2] - black_level[1]
        ret_img.data[1::2, ::2] = raw_data[1::2, ::2] - black_level[2]
        ret_img.data[1::2, 1::2] = raw_data[1::2, 1::2] - black_level[3]
        return ret_img

    else:
        params.set_error_str("black level correction need RAW data")
        return None


def channel_gain_white_balance(raw: RawImageInfo, params: RawImageParams):
    """
    function: channel_gain_white_balance
    brief: multiply with the white balance channel gains
    input: raw:RawImageInfo() params:RawImageParams()
    """
    # get params
    (r_gain, g_gain, b_gain) = params.get_awb_gain()
    channel_gain = (r_gain, g_gain, g_gain, b_gain)
    bayer_pattern = raw.get_bayer_pattern()
    raw_data = raw.get_raw_data()
    ret_img = RawImageInfo()
    # check error
    if(raw_data is None):
        params.set_error_str("RAW data is None")
        return None

    # ensure input color space and process
    if(raw.get_color_space() == "raw"):
        ret_img.create_image('after awb', raw_data.shape)
        channel_gain = resort_with_bayer_pattern(channel_gain, bayer_pattern)
        # multiply with the channel gains
        ret_img.data[::2, ::2] = raw_data[::2, ::2] * channel_gain[0]
        ret_img.data[::2, 1::2] = raw_data[::2, 1::2] * channel_gain[1]
        ret_img.data[1::2, ::2] = raw_data[1::2, ::2] * channel_gain[2]
        ret_img.data[1::2, 1::2] = raw_data[1::2, 1::2] * channel_gain[3]

        return ret_img
    else:
        params.set_error_str("white balance correction need RAW data")
        return None


def bad_pixel_correction(raw: RawImageInfo, params: RawImageParams):
    """
    function: bad_pixel_correction
    correct for the bad (dead, stuck, or hot) pixels
    input: raw:RawImageInfo() params:RawImageParams()
    卷积核neighborhood_size * neighborhood_size，当这个值大于卷积核内最大的值或者小于最小的值，会将这个值替代掉
    这个算法应该会损失不少分辨率
    """
    neighborhood_size = params.get_size_for_bad_pixel_correction()
    if ((neighborhood_size % 2) == 0):
        print("neighborhood_size shoud be odd number, recommended value 3")
        return raw

    raw_data = raw.get_raw_data()
    if(raw_data is None):
        params.set_error_str("RAW data is None")
        return None

    if (raw.get_color_space() == "raw"):
        ret_img = RawImageInfo()
        ret_img.create_image('after bad pixel correction', raw_data.shape)
        # Separate out the quarter resolution images
        D = split_raw_data(raw_data)

        # number of pixels to be padded at the borders
        #no_of_pixel_pad = math.floor(neighborhood_size / 2.)
        no_of_pixel_pad = neighborhood_size // 2

        for idx in range(0, len(D)):  # perform same operation for each quarter

            # display progress
            print("bad pixel correction: Quarter " + str(idx+1) + " of 4")

            img = D[idx]
            width, height = img.shape[1], img.shape[0]

            # pad pixels at the borders, 扩充边缘
            img = np.pad(img,
                         (no_of_pixel_pad, no_of_pixel_pad),
                         'reflect')  # reflect would not repeat the border value

            for i in range(no_of_pixel_pad, height + no_of_pixel_pad):
                for j in range(no_of_pixel_pad, width + no_of_pixel_pad):

                    # save the middle pixel value
                    mid_pixel_val = img[i, j]

                    # extract the neighborhood
                    neighborhood = img[i - no_of_pixel_pad: i + no_of_pixel_pad+1,
                                       j - no_of_pixel_pad: j + no_of_pixel_pad+1]

                    # set the center pixels value same as the left pixel
                    # Does not matter replace with right or left pixel
                    # is used to replace the center pixels value
                    neighborhood[no_of_pixel_pad,
                                 no_of_pixel_pad] = neighborhood[no_of_pixel_pad, no_of_pixel_pad-1]

                    min_neighborhood = np.min(neighborhood)
                    max_neighborhood = np.max(neighborhood)

                    if (mid_pixel_val < min_neighborhood):
                        img[i, j] = min_neighborhood
                    elif (mid_pixel_val > max_neighborhood):
                        img[i, j] = max_neighborhood
                    else:
                        img[i, j] = mid_pixel_val

            # Put the corrected image to the dictionary
            D[idx] = img[no_of_pixel_pad: height + no_of_pixel_pad,
                         no_of_pixel_pad: width + no_of_pixel_pad]

        # Regrouping the data
        ret_img.data[::2, ::2] = D[0]
        ret_img.data[::2, 1::2] = D[1]
        ret_img.data[1::2, ::2] = D[2]
        ret_img.data[1::2, 1::2] = D[3]

        return ret_img
    else:
        params.set_error_str("bad pixel correction need RAW data")
        return None
# =============================================================
# class: demosaic
# =============================================================


class demosaic:
    def __init__(self, data, bayer_pattern="rggb", clip_range=[0, 65535], name="demosaic"):
        self.data = np.float32(data)
        self.bayer_pattern = bayer_pattern
        self.clip_range = clip_range
        self.name = name

    def mhc(self, timeshow=False):

        print("----------------------------------------------------")
        print("Running demosaicing using Malvar-He-Cutler algorithm...")

        return debayer.debayer_mhc(self.data, self.bayer_pattern, self.clip_range, timeshow)

    def post_process_local_color_ratio(self, beta):
        # Objective is to reduce high chroma jump
        # Beta is controlling parameter, higher gives more effect,
        # however, too high does not make any more change

        print("----------------------------------------------------")
        print("Demosaicing post process using local color ratio...")

        data = self.data

        # add beta with the data to prevent divide by zero
        data_beta = self.data + beta

        # convolution kernels
        # zeta1 averages the up, down, left, and right four values of a 3x3 window
        zeta1 = np.multiply([[0., 1., 0.], [1., 0., 1.], [0., 1., 0.]], .25)
        # zeta2 averages the four corner values of a 3x3 window
        zeta2 = np.multiply([[1., 0., 1.], [0., 0., 0.], [1., 0., 1.]], .25)

        # average of color ratio
        g_over_b = signal.convolve2d(np.divide(
            data_beta[:, :, 1], data_beta[:, :, 2]), zeta1, mode="same", boundary="symm")
        g_over_r = signal.convolve2d(np.divide(
            data_beta[:, :, 1], data_beta[:, :, 0]), zeta1, mode="same", boundary="symm")
        b_over_g_zeta2 = signal.convolve2d(np.divide(
            data_beta[:, :, 2], data_beta[:, :, 1]), zeta2, mode="same", boundary="symm")
        r_over_g_zeta2 = signal.convolve2d(np.divide(
            data_beta[:, :, 0], data_beta[:, :, 1]), zeta2, mode="same", boundary="symm")
        b_over_g_zeta1 = signal.convolve2d(np.divide(
            data_beta[:, :, 2], data_beta[:, :, 1]), zeta1, mode="same", boundary="symm")
        r_over_g_zeta1 = signal.convolve2d(np.divide(
            data_beta[:, :, 0], data_beta[:, :, 1]), zeta1, mode="same", boundary="symm")

        # G at B locations and G at R locations
        if self.bayer_pattern == "rggb":
            # G at B locations
            data[1::2, 1::2, 1] = -beta + \
                np.multiply(data_beta[1::2, 1::2, 2], g_over_b[1::2, 1::2])
            # G at R locations
            data[::2, ::2, 1] = -beta + \
                np.multiply(data_beta[::2, ::2, 0], g_over_r[::2, ::2])
            # B at R locations
            data[::2, ::2, 2] = -beta + \
                np.multiply(data_beta[::2, ::2, 1], b_over_g_zeta2[::2, ::2])
            # R at B locations
            data[1::2, 1::2, 0] = -beta + \
                np.multiply(data_beta[1::2, 1::2, 1],
                            r_over_g_zeta2[1::2, 1::2])
            # B at G locations
            data[::2, 1::2, 2] = -beta + \
                np.multiply(data_beta[::2, 1::2, 1], b_over_g_zeta1[::2, 1::2])
            data[1::2, ::2, 2] = -beta + \
                np.multiply(data_beta[1::2, ::2, 1], b_over_g_zeta1[1::2, ::2])
            # R at G locations
            data[::2, 1::2, 0] = -beta + \
                np.multiply(data_beta[::2, 1::2, 1], r_over_g_zeta1[::2, 1::2])
            data[1::2, ::2, 0] = -beta + \
                np.multiply(data_beta[1::2, ::2, 1], r_over_g_zeta1[1::2, ::2])

        elif self.bayer_pattern == "grbg":
            # G at B locations
            data[1::2, ::2, 1] = -beta + \
                np.multiply(data_beta[1::2, ::2, 2], g_over_b[1::2, 1::2])
            # G at R locations
            data[::2, 1::2, 1] = -beta + \
                np.multiply(data_beta[::2, 1::2, 0], g_over_r[::2, 1::2])
            # B at R locations
            data[::2, 1::2, 2] = -beta + \
                np.multiply(data_beta[::2, 1::2, 1], b_over_g_zeta2[::2, 1::2])
            # R at B locations
            data[1::2, ::2, 0] = -beta + \
                np.multiply(data_beta[1::2, ::2, 1], r_over_g_zeta2[1::2, ::2])
            # B at G locations
            data[::2, ::2, 2] = -beta + \
                np.multiply(data_beta[::2, ::2, 1], b_over_g_zeta1[::2, ::2])
            data[1::2, 1::2, 2] = -beta + \
                np.multiply(data_beta[1::2, 1::2, 1],
                            b_over_g_zeta1[1::2, 1::2])
            # R at G locations
            data[::2, ::2, 0] = -beta + \
                np.multiply(data_beta[::2, ::2, 1], r_over_g_zeta1[::2, ::2])
            data[1::2, 1::2, 0] = -beta + \
                np.multiply(data_beta[1::2, 1::2, 1],
                            r_over_g_zeta1[1::2, 1::2])

        elif self.bayer_pattern == "gbrg":
            # G at B locations
            data[::2, 1::2, 1] = -beta + \
                np.multiply(data_beta[::2, 1::2, 2], g_over_b[::2, 1::2])
            # G at R locations
            data[1::2, ::2, 1] = -beta + \
                np.multiply(data_beta[1::2, ::2, 0], g_over_r[1::2, ::2])
            # B at R locations
            data[1::2, ::2, 2] = -beta + \
                np.multiply(data_beta[1::2, ::2, 1], b_over_g_zeta2[1::2, ::2])
            # R at B locations
            data[::2, 1::2, 0] = -beta + \
                np.multiply(data_beta[::2, 1::2, 1], r_over_g_zeta2[::2, 1::2])
            # B at G locations
            data[::2, ::2, 2] = -beta + \
                np.multiply(data_beta[::2, ::2, 1], b_over_g_zeta1[::2, ::2])
            data[1::2, 1::2, 2] = -beta + \
                np.multiply(data_beta[1::2, 1::2, 1],
                            b_over_g_zeta1[1::2, 1::2])
            # R at G locations
            data[::2, ::2, 0] = -beta + \
                np.multiply(data_beta[::2, ::2, 1], r_over_g_zeta1[::2, ::2])
            data[1::2, 1::2, 0] = -beta + \
                np.multiply(data_beta[1::2, 1::2, 1],
                            r_over_g_zeta1[1::2, 1::2])

        elif self.bayer_pattern == "bggr":
            # G at B locations
            data[::2, ::2, 1] = -beta + \
                np.multiply(data_beta[::2, ::2, 2], g_over_b[::2, ::2])
            # G at R locations
            data[1::2, 1::2, 1] = -beta + \
                np.multiply(data_beta[1::2, 1::2, 0], g_over_r[1::2, 1::2])
            # B at R locations
            data[1::2, 1::2, 2] = -beta + \
                np.multiply(data_beta[1::2, 1::2, 1],
                            b_over_g_zeta2[1::2, 1::2])
            # R at B locations
            data[::2, ::2, 0] = -beta + \
                np.multiply(data_beta[::2, ::2, 1], r_over_g_zeta2[::2, ::2])
            # B at G locations
            data[::2, 1::2, 2] = -beta + \
                np.multiply(data_beta[::2, 1::2, 1], b_over_g_zeta1[::2, 1::2])
            data[1::2, ::2, 2] = -beta + \
                np.multiply(data_beta[1::2, ::2, 1], b_over_g_zeta1[1::2, ::2])
            # R at G locations
            data[::2, 1::2, 0] = -beta + \
                np.multiply(data_beta[::2, 1::2, 1], r_over_g_zeta1[::2, 1::2])
            data[1::2, ::2, 0] = -beta + \
                np.multiply(data_beta[1::2, ::2, 1], r_over_g_zeta1[1::2, ::2])

        return np.clip(data, self.clip_range[0], self.clip_range[1])

    def directionally_weighted_gradient_based_interpolation(self):
        # Reference:
        # http://www.arl.army.mil/arlreports/2010/ARL-TR-5061.pdf

        print("----------------------------------------------------")
        print("Running demosaicing using directionally weighted gradient based interpolation...")

        # Fill up the green channel
        G = debayer.fill_channel_directional_weight(
            self.data, self.bayer_pattern)

        B, R = debayer.fill_br_locations(self.data, G, self.bayer_pattern)

        width, height = utility.helpers(self.data).get_width_height()
        output = np.empty((height, width, 3), dtype=np.float32)
        output[:, :, 0] = R
        output[:, :, 1] = G
        output[:, :, 2] = B

        return np.clip(output, self.clip_range[0], self.clip_range[1])

    def post_process_median_filter(self, edge_detect_kernel_size=3, edge_threshold=0, median_filter_kernel_size=3, clip_range=[0, 65535]):
        # Objective is to reduce the zipper effect around the edges
        # Inputs:
        #   edge_detect_kernel_size: the neighborhood size used to detect edges
        #   edge_threshold: the threshold value above which (compared against)
        #                   the gradient_magnitude to declare if it is an edge
        #   median_filter_kernel_size: the neighborhood size used to perform
        #                               median filter operation
        #   clip_range: used for scaling in edge_detection
        #
        # Output:
        #   output: median filtered output around the edges
        #   edge_location: a debug image to see where the edges were detected
        #                   based on the threshold

        # detect edge locations
        edge_location = utility.edge_detection(self.data).sobel(
            edge_detect_kernel_size, "is_edge", edge_threshold, clip_range)

        # allocate space for output
        output = np.empty(np.shape(self.data), dtype=np.float32)

        if (np.ndim(self.data) > 2):

            for i in range(0, np.shape(self.data)[2]):
                output[:, :, i] = utility.helpers(self.data[:, :, i]).edge_wise_median(
                    median_filter_kernel_size, edge_location[:, :, i])

        elif (np.ndim(self.data) == 2):
            output = utility.helpers(self.data).edge_wise_median(
                median_filter_kernel_size, edge_location)

        return output, edge_location

    def __str__(self):
        return self.name


# =============================================================
# class: lens_shading_correction
#   Correct the lens shading / vignetting
# =============================================================
class lens_shading_correction:
    def __init__(self, data, name="lens_shading_correction"):
        # convert to float32 in case it was not
        self.data = np.float32(data)
        self.name = name

    def flat_field_compensation(self, dark_current_image, flat_field_image):
        # dark_current_image:
        #       is captured from the camera with cap on
        #       and fully dark condition, several images captured and
        #       temporally averaged
        # flat_field_image:
        #       is found by capturing an image of a flat field test chart
        #       with certain lighting condition
        # Note: flat_field_compensation is memory intensive procedure because
        #       both the dark_current_image and flat_field_image need to be
        #       saved in memory beforehand
        print("----------------------------------------------------")
        print("Running lens shading correction with flat field compensation...")

        # convert to float32 in case it was not
        dark_current_image = np.float32(dark_current_image)
        flat_field_image = np.float32(flat_field_image)
        temp = flat_field_image - dark_current_image
        return np.average(temp) * np.divide((self.data - dark_current_image), temp)

    def approximate_mathematical_compensation(self, params, clip_min=0, clip_max=65535):
        # parms:
        #       parameters of a parabolic model y = a*(x-b)^2 + c
        #       For example, params = [0.01759, -28.37, -13.36]
        # Note: approximate_mathematical_compensation require less memory
        print("----------------------------------------------------")
        print(
            "Running lens shading correction with approximate mathematical compensation...")
        width, height = utility.helpers(self.data).get_width_height()

        center_pixel_pos = [height/2, width/2]
        max_distance = utility.distance_euclid(
            center_pixel_pos, [height, width])

        # allocate memory for output
        temp = np.empty((height, width), dtype=np.float32)

        for i in range(0, height):
            for j in range(0, width):
                distance = utility.distance_euclid(
                    center_pixel_pos, [i, j]) / max_distance
                # parabolic model
                gain = params[0] * (distance - params[1])**2 + params[2]
                temp[i, j] = self.data[i, j] * gain

        temp = np.clip(temp, clip_min, clip_max)
        return temp

    def __str__(self):
        return "lens shading correction. There are two methods: " + \
            "\n (1) flat_field_compensation: requires dark_current_image and flat_field_image" + \
            "\n (2) approximate_mathematical_compensation:"


# =============================================================
# class: lens_shading_correction
#   Correct the lens shading / vignetting
# =============================================================
class bayer_denoising:
    def __init__(self, data, name="bayer_denoising"):
        # convert to float32 in case it was not
        self.data = np.float32(data)
        self.name = name

    def utilize_hvs_behavior(self, bayer_pattern, initial_noise_level, hvs_min, hvs_max, threshold_red_blue, clip_range):
        # Objective: bayer denoising
        # Inputs:
        #   bayer_pattern:  rggb, gbrg, grbg, bggr
        #   initial_noise_level:
        # Output:
        #   denoised bayer raw output
        # Source: Based on paper titled "Noise Reduction for CFA Image Sensors
        #   Exploiting HVS Behaviour," by Angelo Bosco, Sebastiano Battiato,
        #   Arcangelo Bruna and Rosetta Rizzo
        #   Sensors 2009, 9, 1692-1713; doi:10.3390/s90301692

        print("----------------------------------------------------")
        print("Running bayer denoising utilizing hvs behavior...")

        # copy the self.data to raw and we will only work on raw
        # to make sure no change happen to self.data
        raw = self.data
        raw = np.clip(raw, clip_range[0], clip_range[1])
        width, height = utility.helpers(raw).get_width_height()

        # First make the bayer_pattern rggb
        # The algorithm is written only for rggb pattern, thus convert all other
        # pattern to rggb. Furthermore, this shuffling does not affect the
        # algorithm output
        if (bayer_pattern != "rggb"):
            raw = utility.helpers(self.data).shuffle_bayer_pattern(
                bayer_pattern, "rggb")

        # fixed neighborhood_size
        neighborhood_size = 5  # we are keeping this fixed
        # bigger size such as 9 can be declared
        # however, the code need to be changed then

        # pad two pixels at the border
        no_of_pixel_pad = math.floor(
            neighborhood_size / 2)   # number of pixels to pad

        raw = np.pad(raw,
                     (no_of_pixel_pad, no_of_pixel_pad),
                     'reflect')  # reflect would not repeat the border value

        # allocating space for denoised output
        denoised_out = np.empty((height, width), dtype=np.float32)

        texture_degree_debug = np.empty((height, width), dtype=np.float32)
        for i in range(no_of_pixel_pad, height + no_of_pixel_pad):
            for j in range(no_of_pixel_pad, width + no_of_pixel_pad):

                # center pixel
                center_pixel = raw[i, j]

                # signal analyzer block
                half_max = clip_range[1] / 2
                if (center_pixel <= half_max):
                    hvs_weight = - \
                        (((hvs_max - hvs_min) * center_pixel) / half_max) + hvs_max
                else:
                    hvs_weight = (
                        ((center_pixel - clip_range[1]) * (hvs_max - hvs_min))/(clip_range[1] - half_max)) + hvs_max

                # noise level estimator previous value
                if (j < no_of_pixel_pad+2):
                    noise_level_previous_red = initial_noise_level
                    noise_level_previous_blue = initial_noise_level
                    noise_level_previous_green = initial_noise_level
                else:
                    noise_level_previous_green = noise_level_current_green
                    if ((i % 2) == 0):  # red
                        noise_level_previous_red = noise_level_current_red
                    elif ((i % 2) != 0):  # blue
                        noise_level_previous_blue = noise_level_current_blue

                # Processings depending on Green or Red/Blue
                # Red
                if (((i % 2) == 0) and ((j % 2) == 0)):
                    # get neighborhood
                    neighborhood = [raw[i-2, j-2], raw[i-2, j], raw[i-2, j+2],
                                    raw[i, j-2], raw[i, j+2],
                                    raw[i+2, j-2], raw[i+2, j], raw[i+2, j+2]]

                    # absolute difference from the center pixel
                    d = np.abs(neighborhood - center_pixel)

                    # maximum and minimum difference
                    d_max = np.max(d)
                    d_min = np.min(d)

                    # calculate texture_threshold
                    texture_threshold = hvs_weight + noise_level_previous_red

                    # texture degree analyzer
                    if (d_max <= threshold_red_blue):
                        texture_degree = 1.
                    elif ((d_max > threshold_red_blue) and (d_max <= texture_threshold)):
                        texture_degree = - \
                            ((d_max - threshold_red_blue) /
                             (texture_threshold - threshold_red_blue)) + 1.
                    elif (d_max > texture_threshold):
                        texture_degree = 0.

                    # noise level estimator update
                    noise_level_current_red = texture_degree * d_max + \
                        (1 - texture_degree) * noise_level_previous_red

                # Blue
                elif (((i % 2) != 0) and ((j % 2) != 0)):

                    # get neighborhood
                    neighborhood = [raw[i-2, j-2], raw[i-2, j], raw[i-2, j+2],
                                    raw[i, j-2], raw[i, j+2],
                                    raw[i+2, j-2], raw[i+2, j], raw[i+2, j+2]]

                    # absolute difference from the center pixel
                    d = np.abs(neighborhood - center_pixel)

                    # maximum and minimum difference
                    d_max = np.max(d)
                    d_min = np.min(d)

                    # calculate texture_threshold
                    texture_threshold = hvs_weight + noise_level_previous_blue

                    # texture degree analyzer
                    if (d_max <= threshold_red_blue):
                        texture_degree = 1.
                    elif ((d_max > threshold_red_blue) and (d_max <= texture_threshold)):
                        texture_degree = - \
                            ((d_max - threshold_red_blue) /
                             (texture_threshold - threshold_red_blue)) + 1.
                    elif (d_max > texture_threshold):
                        texture_degree = 0.

                    # noise level estimator update
                    noise_level_current_blue = texture_degree * d_max + \
                        (1 - texture_degree) * noise_level_previous_blue

                # Green
                elif ((((i % 2) == 0) and ((j % 2) != 0)) or (((i % 2) != 0) and ((j % 2) == 0))):

                    neighborhood = [raw[i-2, j-2], raw[i-2, j], raw[i-2, j+2],
                                    raw[i-1, j-1], raw[i-1, j+1],
                                    raw[i, j-2], raw[i, j+2],
                                    raw[i+1, j-1], raw[i+1, j+1],
                                    raw[i+2, j-2], raw[i+2, j], raw[i+2, j+2]]

                    # difference from the center pixel
                    d = np.abs(neighborhood - center_pixel)

                    # maximum and minimum difference
                    d_max = np.max(d)
                    d_min = np.min(d)

                    # calculate texture_threshold
                    texture_threshold = hvs_weight + noise_level_previous_green

                    # texture degree analyzer
                    if (d_max == 0):
                        texture_degree = 1
                    elif ((d_max > 0) and (d_max <= texture_threshold)):
                        texture_degree = -(d_max / texture_threshold) + 1.
                    elif (d_max > texture_threshold):
                        texture_degree = 0

                    # noise level estimator update
                    noise_level_current_green = texture_degree * d_max + \
                        (1 - texture_degree) * noise_level_previous_green

                # similarity threshold calculation
                if (texture_degree == 1):
                    threshold_low = threshold_high = d_max
                elif (texture_degree == 0):
                    threshold_low = d_min
                    threshold_high = (d_max + d_min) / 2
                elif ((texture_degree > 0) and (texture_degree < 1)):
                    threshold_high = (d_max + ((d_max + d_min) / 2)) / 2
                    threshold_low = (d_min + threshold_high) / 2

                # weight computation
                weight = np.empty(np.size(d), dtype=np.float32)
                pf = 0.
                for w_i in range(0, np.size(d)):
                    if (d[w_i] <= threshold_low):
                        weight[w_i] = 1.
                    elif (d[w_i] > threshold_high):
                        weight[w_i] = 0.
                    elif ((d[w_i] > threshold_low) and (d[w_i] < threshold_high)):
                        weight[w_i] = 1. + ((d[w_i] - threshold_low) /
                                            (threshold_low - threshold_high))

                    pf += weight[w_i] * neighborhood[w_i] + \
                        (1. - weight[w_i]) * center_pixel

                denoised_out[i - no_of_pixel_pad, j -
                             no_of_pixel_pad] = pf / np.size(d)
                # texture_degree_debug is a debug output
                texture_degree_debug[i - no_of_pixel_pad,
                                     j-no_of_pixel_pad] = texture_degree

        if (bayer_pattern != "rggb"):
            denoised_out = utility.shuffle_bayer_pattern(
                denoised_out, "rggb", bayer_pattern)

        return np.clip(denoised_out, clip_range[0], clip_range[1]), texture_degree_debug

    def __str__(self):
        return self.name


# =============================================================
# class: color_correction
#   Correct the color in linaer domain
# =============================================================
class color_correction:
    def __init__(self, data, color_matrix, color_space="srgb", illuminant="d65", name="color correction", clip_range=[0, 65535]):
        # Inputs:
        #   data:   linear rgb image before nonlinearity/gamma
        #   xyz2cam: 3x3 matrix found from the camera metedata, specifically
        #            color matrix 2 from the metadata
        #   color_space: output color space
        #   illuminance: the illuminant of the lighting condition
        #   name: name of the class
        self.data = np.float32(data)
        self.xyz2cam = np.float32(color_matrix)
        self.color_space = color_space
        self.illuminant = illuminant
        self.name = name
        self.clip_range = clip_range

    def get_rgb2xyz(self):
        # Objective: get the rgb2xyz matrix dependin on the output color space
        #            and the illuminant
        # Source: http://www.brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html
        if (self.color_space == "srgb"):
            if (self.illuminant == "d65"):
                return [[.4124564,  .3575761,  .1804375],
                        [.2126729,  .7151522,  .0721750],
                        [.0193339,  .1191920,  .9503041]]
            elif (self.illuminant == "d50"):
                return [[.4360747,  .3850649,  .1430804],
                        [.2225045,  .7168786,  .0606169],
                        [.0139322,  .0971045,  .7141733]]
            else:
                print("for now, color_space must be d65 or d50")
                return

        elif (self.color_space == "adobe-rgb-1998"):
            if (self.illuminant == "d65"):
                return [[.5767309,  .1855540,  .1881852],
                        [.2973769,  .6273491,  .0752741],
                        [.0270343,  .0706872,  .9911085]]
            elif (self.illuminant == "d50"):
                return [[.6097559,  .2052401,  .1492240],
                        [.3111242,  .6256560,  .0632197],
                        [.0194811,  .0608902,  .7448387]]
            else:
                print("for now, illuminant must be d65 or d50")
                return
        else:
            print("for now, color_space must be srgb or adobe-rgb-1998")
            return

    def calculate_cam2rgb(self):
        # Objective: Calculates the color correction matrix

        # matric multiplication
        rgb2cam = np.dot(self.xyz2cam, self.get_rgb2xyz())

        # make sum of each row to be 1.0, necessary to preserve white balance
        # basically divice each value by its row wise sum
        rgb2cam = np.divide(rgb2cam, np.reshape(np.sum(rgb2cam, 1), [3, 1]))

        # - inverse the matrix to get cam2rgb.
        # - cam2rgb should also have the characteristic that sum of each row
        # equal to 1.0 to preserve white balance
        # - check if rgb2cam is invertible by checking the condition of
        # rgb2cam. If rgb2cam is singular it will give a warning and
        # return an identiry matrix
        if (np.linalg.cond(rgb2cam) < (1 / sys.float_info.epsilon)):
            # this is cam2rgb / color correction matrix
            return np.linalg.inv(rgb2cam)
        else:
            print("Warning! matrix not invertible.")
            return np.identity(3, dtype=np.float32)

    def apply_cmatrix(self):
        # Objective: Apply the color correction matrix (cam2rgb)

        print("----------------------------------------------------")
        print("running color correction...")

        # check if data is 3 dimensional
        if (np.ndim(self.data) != 3):
            print("data need to be three dimensional")
            return

        # get the color correction matrix
        cam2rgb = self.calculate_cam2rgb()

        # get width and height
        width, height = utility.helpers(self.data).get_width_height()

        # apply the matrix
        R = self.data[:, :, 0]
        G = self.data[:, :, 1]
        B = self.data[:, :, 2]

        color_corrected = np.empty((height, width, 3), dtype=np.float32)
        color_corrected[:, :, 0] = R * cam2rgb[0, 0] + \
            G * cam2rgb[0, 1] + B * cam2rgb[0, 2]
        color_corrected[:, :, 1] = R * cam2rgb[1, 0] + \
            G * cam2rgb[1, 1] + B * cam2rgb[1, 2]
        color_corrected[:, :, 2] = R * cam2rgb[2, 0] + \
            G * cam2rgb[2, 1] + B * cam2rgb[2, 2]

        return np.clip(color_corrected, self.clip_range[0], self.clip_range[1])

    def __str__(self):
        return self.name


# =============================================================
# class: nonlinearity
#   apply gamma or degamma
# =============================================================
class nonlinearity:
    def __init__(self, data, name="nonlinearity"):
        self.data = np.float32(data)
        self.name = name

    def luma_adjustment(self, multiplier, clip_range=[0, 65535]):
        # The multiplier is applied only on luma channel
        # by a multipler in log10 scale:
        #   multipler 10 means multiplied by 1.
        #   multipler 100 means multiplied by 2. as such

        print("----------------------------------------------------")
        print("Running brightening...")

        return np.clip(np.log10(multiplier) * self.data, clip_range[0], clip_range[1])

    def by_value(self, value, clip_range):

        print("----------------------------------------------------")
        print("Running nonlinearity by value...")

        # clip within the range
        data = np.clip(self.data, clip_range[0], clip_range[1])
        # make 0 to 1
        data = data / clip_range[1]
        # apply nonlinearity
        return np.clip(clip_range[1] * (data**value), clip_range[0], clip_range[1])

    def by_table(self, table, nonlinearity_type="gamma", clip_range=[0, 65535]):

        print("----------------------------------------------------")
        print("Running nonlinearity by table...")

        gamma_table = np.loadtxt(table)
        gamma_table = clip_range[1] * gamma_table / np.max(gamma_table)
        linear_table = np.linspace(
            clip_range[0], clip_range[1], np.size(gamma_table))

        # linear interpolation, query is the self.data
        if (nonlinearity_type == "gamma"):
            # mapping is from linear_table to gamma_table
            return np.clip(np.interp(self.data, linear_table, gamma_table), clip_range[0], clip_range[1])
        elif (nonlinearity_type == "degamma"):
            # mapping is from gamma_table to linear_table
            return np.clip(np.interp(self.data, gamma_table, linear_table), clip_range[0], clip_range[1])

    def by_equation(self, a, b, clip_range):

        print("----------------------------------------------------")
        print("Running nonlinearity by equation...")

        # clip within the range
        data = np.clip(self.data, clip_range[0], clip_range[1])
        # make 0 to 1
        data = data / clip_range[1]

        # apply nonlinearity
        return np.clip(clip_range[1] * (a * np.exp(b * data) + data + a * data - a * np.exp(b) * data - a), clip_range[0], clip_range[1])

    def __str__(self):
        return self.name


# =============================================================
# class: tone_mapping
#   improve the overall tone of the image
# =============================================================
class tone_mapping:
    def __init__(self, data, name="tone mapping"):
        self.data = np.float32(data)
        self.name = name

    def nonlinear_masking(self, strength_multiplier=1.0, gaussian_kernel_size=[5, 5], gaussian_sigma=1.0, clip_range=[0, 65535]):
        # Objective: improves the overall tone of the image
        # Inputs:
        #   strength_multiplier: >0. The higher the more aggressing tone mapping
        #   gaussian_kernel_size: kernel size for calculating the mask image
        #   gaussian_sigma: spread of the gaussian kernel for calculating the
        #                   mask image
        #
        # Source:
        # N. Moroney, “Local color correction using non-linear masking”,
        # Proc. IS&T/SID 8th Color Imaging Conference, pp. 108-111, (2000)
        #
        # Note, Slight changes is carried by mushfiqul alam, specifically
        # introducing the strength_multiplier

        print("----------------------------------------------------")
        print("Running tone mapping by non linear masking...")

        # convert to gray image
        if (np.ndim(self.data) == 3):
            gray_image = utility.color_conversion(self.data).rgb2gray()
        else:
            gray_image = self.data

        # gaussian blur the gray image
        gaussian_kernel = utility.create_filter().gaussian(
            gaussian_kernel_size, gaussian_sigma)

        # the mask image:   (1) blur
        #                   (2) bring within range 0 to 1
        #                   (3) multiply with strength_multiplier
        mask = signal.convolve2d(
            gray_image, gaussian_kernel, mode="same", boundary="symm")
        mask = strength_multiplier * mask / clip_range[1]

        # calculate the alpha image
        temp = np.power(0.5, mask)
        if (np.ndim(self.data) == 3):
            width, height = utility.helpers(self.data).get_width_height()
            alpha = np.empty((height, width, 3), dtype=np.float32)
            alpha[:, :, 0] = temp
            alpha[:, :, 1] = temp
            alpha[:, :, 2] = temp
        else:
            alpha = temp

        # output
        return np.clip(clip_range[1] * np.power(self.data/clip_range[1], alpha), clip_range[0], clip_range[1])

    def dynamic_range_compression(self, drc_type="normal", drc_bound=[-40., 260.], clip_range=[0, 65535]):

        ycc = utility.color_conversion(self.data).rgb2ycc("bt601")
        y = ycc[:, :, 0]
        cb = ycc[:, :, 1]
        cr = ycc[:, :, 2]

        if (drc_type == "normal"):
            edge = y
        elif (drc_type == "joint"):
            edge = utility.edge_detection(y).sobel(3, "gradient_magnitude")

        y_bilateral_filtered = utility.special_function(
            y).bilateral_filter(edge)
        detail = np.divide(ycc[:, :, 0], y_bilateral_filtered)

        C = drc_bound[0] * clip_range[1] / 255.
        temp = drc_bound[1] * clip_range[1] / 255.
        F = (temp * (C + clip_range[1])) / (clip_range[1] * (temp - C))
        y_bilateral_filtered_contrast_reduced = F * \
            (y_bilateral_filtered -
             (clip_range[1] / 2.)) + (clip_range[1] / 2.)

        y_out = np.multiply(y_bilateral_filtered_contrast_reduced, detail)

        ycc_out = ycc
        ycc_out[:, :, 0] = y_out
        rgb_out = utility.color_conversion(ycc_out).ycc2rgb("bt601")

        return np.clip(rgb_out, clip_range[0], clip_range[1])


# =============================================================
# class: sharpening
#   sharpens the image
# =============================================================
class sharpening:
    def __init__(self, data, name="sharpening"):
        self.data = np.float32(data)
        self.name = name

    def unsharp_masking(self, gaussian_kernel_size=[5, 5], gaussian_sigma=2.0,
                        slope=1.5, tau_threshold=0.05, gamma_speed=4., clip_range=[0, 65535]):
        # Objective: sharpen image
        # Input:
        #   gaussian_kernel_size:   dimension of the gaussian blur filter kernel
        #
        #   gaussian_sigma:         spread of the gaussian blur filter kernel
        #                           bigger sigma more sharpening
        #
        #   slope:                  controls the boost.
        #                           the amount of sharpening, higher slope
        #                           means more aggresssive sharpening
        #
        #   tau_threshold:          controls the amount of coring.
        #                           threshold value till which the image is
        #                           not sharpened. The lower the value of
        #                           tau_threshold the more frequencies
        #                           goes through the sharpening process
        #
        #   gamma_speed:            controls the speed of convergence to the slope
        #                           smaller value gives a little bit more
        #                           sharpened image, this may be a fine tuner

        print("----------------------------------------------------")
        print("Running sharpening by unsharp masking...")

        # create gaussian kernel
        gaussian_kernel = utility.create_filter().gaussian(
            gaussian_kernel_size, gaussian_sigma)

        # convolove the image with the gaussian kernel
        # first input is the image
        # second input is the kernel
        # output shape will be the same as the first input
        # boundary will be padded by using symmetrical method while convolving
        if np.ndim(self.data > 2):
            image_blur = np.empty(np.shape(self.data), dtype=np.float32)
            for i in range(0, np.shape(self.data)[2]):
                image_blur[:, :, i] = signal.convolve2d(
                    self.data[:, :, i], gaussian_kernel, mode="same", boundary="symm")
        else:
            image_blur = signal.convolove2d(
                self.data, gaussian_kernel, mode="same", boundary="symm")

        # the high frequency component image
        image_high_pass = self.data - image_blur

        # soft coring (see in utility)
        # basically pass the high pass image via a slightly nonlinear function
        tau_threshold = tau_threshold * clip_range[1]

        # add the soft cored high pass image to the original and clip
        # within range and return
        return np.clip(self.data + utility.special_function(
            image_high_pass).soft_coring(
            slope, tau_threshold, gamma_speed), clip_range[0], clip_range[1])

    def __str__(self):
        return self.name


# =============================================================
# class: noise_reduction
#   reduce noise of the nonlinear image (after gamma)
# =============================================================
class noise_reduction:
    def __init__(self, data, clip_range=[0, 65535], name="noise reduction"):
        self.data = np.float32(data)
        self.clip_range = clip_range
        self.name = name

    def sigma_filter(self, neighborhood_size=7, sigma=[6, 6, 6]):

        print("----------------------------------------------------")
        print("Running noise reduction by sigma filter...")

        if np.ndim(self.data > 2):  # if rgb image
            output = np.empty(np.shape(self.data), dtype=np.float32)
            for i in range(0, np.shape(self.data)[2]):
                output[:, :, i] = utility.helpers(
                    self.data[:, :, i]).sigma_filter_helper(neighborhood_size, sigma[i])
            return np.clip(output, self.clip_range[0], self.clip_range[1])
        else:  # gray image
            return np.clip(utility.helpers(self.data).sigma_filter_helper(neighborhood_size, sigma), self.clip_range[0], self.clip_range[1])

    def __str__(self):
        return self.name


# =============================================================
# class: distortion_correction
#   correct the distortion
# =============================================================
class distortion_correction:
    def __init__(self, data, name="distortion correction"):
        self.data = np.float32(data)
        self.name = name

    def empirical_correction(self, correction_type="pincushion-1", strength=0.1, zoom_type="crop", clip_range=[0, 65535]):
        # ------------------------------------------------------
        # Objective:
        #   correct geometric distortion with the assumption that the distortion
        #   is symmetric and the center is at the center of of the image
        # Input:
        #   correction_type:    which type of correction needed to be carried
        #                       out, choose one the four:
        #                       pincushion-1, pincushion-2, barrel-1, barrel-2
        #                       1 and 2 are difference between the power
        #                       over the radius
        #
        #   strength:           should be equal or greater than 0.
        #                       0 means no correction will be done.
        #                       if negative value were applied correction_type
        #                       will be reversed. Thus,>=0 value expected.
        #
        #   zoom_type:          either "fit" or "crop"
        #                       fit will return image with full content
        #                       in the whole area
        #                       crop will return image will 0 values outsise
        #                       the border
        #
        #   clip_range:         to clip the final image within the range
        # ------------------------------------------------------

        if (strength < 0):
            print("Warning! strength should be equal of greater than 0.")
            return self.data

        print("----------------------------------------------------")
        print("Running distortion correction by empirical method...")

        # get half_width and half_height, assume this is the center
        width, height = utility.helpers(self.data).get_width_height()
        half_width = width / 2
        half_height = height / 2

        # create a meshgrid of points
        xi, yi = np.meshgrid(np.linspace(-half_width, half_width, width),
                             np.linspace(-half_height, half_height, height))

        # cartesian to polar coordinate
        r = np.sqrt(xi**2 + yi**2)
        theta = np.arctan2(yi, xi)

        # maximum radius
        R = math.sqrt(width**2 + height**2)

        # make r within range 0~1
        r = r / R

        # apply the radius to the desired transformation
        s = utility.special_function(r).distortion_function(
            correction_type, strength)

        # select a scaling_parameter based on zoon_type and k value
        if ((correction_type == "barrel-1") or (correction_type == "barrel-2")):
            if (zoom_type == "fit"):
                scaling_parameter = r[0, 0] / s[0, 0]
            elif (zoom_type == "crop"):
                scaling_parameter = 1. / \
                    (1. + strength * (np.min([half_width, half_height])/R)**2)
        elif ((correction_type == "pincushion-1") or (correction_type == "pincushion-2")):
            if (zoom_type == "fit"):
                scaling_parameter = 1. / \
                    (1. + strength * (np.min([half_width, half_height])/R)**2)
            elif (zoom_type == "crop"):
                scaling_parameter = r[0, 0] / s[0, 0]

        # multiply by scaling_parameter and un-normalize
        s = s * scaling_parameter * R

        # convert back to cartesian coordinate and add back the center coordinate
        xt = np.multiply(s, np.cos(theta))
        yt = np.multiply(s, np.sin(theta))

        # interpolation
        if np.ndim(self.data == 3):

            output = np.empty(np.shape(self.data), dtype=np.float32)

            output[:, :, 0] = utility.helpers(self.data[:, :, 0]).bilinear_interpolation(
                xt + half_width, yt + half_height)
            output[:, :, 1] = utility.helpers(self.data[:, :, 1]).bilinear_interpolation(
                xt + half_width, yt + half_height)
            output[:, :, 2] = utility.helpers(self.data[:, :, 2]).bilinear_interpolation(
                xt + half_width, yt + half_height)

        elif np.ndim(self.data == 2):

            output = utility.helpers(self.data).bilinear_interpolation(
                xt + half_width, yt + half_height)

        return np.clip(output, clip_range[0], clip_range[1])

    def __str__(self):
        return self.name


# =============================================================
# class: memory_color_enhancement
#   enhance memory colors such as sky, grass, skin color
# =============================================================
class memory_color_enhancement:
    def __init__(self, data, name="memory color enhancement"):
        self.data = np.float32(data)
        self.name = name

    def by_hue_squeeze(self, target_hue, hue_preference, hue_sigma, is_both_side, multiplier, chroma_preference, chroma_sigma, color_space="srgb", illuminant="d65", clip_range=[0, 65535], cie_version="1931"):

        # RGB to xyz
        data = utility.color_conversion(
            self.data).rgb2xyz(color_space, clip_range)
        # xyz to lab
        data = utility.color_conversion(data).xyz2lab(cie_version, illuminant)
        # lab to lch
        data = utility.color_conversion(data).lab2lch()

        # hue squeezing
        # we are traversing through different color preferences
        width, height = utility.helpers(self.data).get_width_height()
        hue_correction = np.zeros((height, width), dtype=np.float32)
        for i in range(0, np.size(target_hue)):

            delta_hue = data[:, :, 2] - hue_preference[i]

            if is_both_side[i]:
                weight_temp = np.exp(-np.power(data[:, :, 2] - target_hue[i], 2) / (2 * hue_sigma[i]**2)) + \
                    np.exp(-np.power(data[:, :, 2] +
                                     target_hue[i], 2) / (2 * hue_sigma[i]**2))
            else:
                weight_temp = np.exp(-np.power(data[:, :, 2] -
                                               target_hue[i], 2) / (2 * hue_sigma[i]**2))

            weight_hue = multiplier[i] * weight_temp / np.max(weight_temp)

            weight_chroma = np.exp(-np.power(data[:, :, 1] -
                                             chroma_preference[i], 2) / (2 * chroma_sigma[i]**2))

            hue_correction = hue_correction + \
                np.multiply(np.multiply(delta_hue, weight_hue), weight_chroma)

        # correct the hue
        data[:, :, 2] = data[:, :, 2] - hue_correction

        # lch to lab
        data = utility.color_conversion(data).lch2lab()
        # lab to xyz
        data = utility.color_conversion(data).lab2xyz(cie_version, illuminant)
        # xyz to rgb
        data = utility.color_conversion(data).xyz2rgb(color_space, clip_range)

        return data

    def __str__(self):
        return self.name


# =============================================================
# class: chromatic_aberration_correction
#   removes artifacts similar to result from chromatic
#   aberration
# =============================================================
class chromatic_aberration_correction:
    def __init__(self, data, name="chromatic aberration correction"):
        self.data = np.float32(data)
        self.name = name

    def purple_fringe_removal(self, nsr_threshold, cr_threshold, clip_range=[0, 65535]):
        # --------------------------------------------------------------
        # nsr_threshold: near saturated region threshold (in percentage)
        # cr_threshold: candidate region threshold
        # --------------------------------------------------------------

        width, height = utility.helpers(self.data).get_width_height()

        r = self.data[:, :, 0]
        g = self.data[:, :, 1]
        b = self.data[:, :, 2]

        # Detection of purple fringe
        # near saturated region detection
        nsr_threshold = clip_range[1] * nsr_threshold / 100
        temp = (r + g + b) / 3
        temp = np.asarray(temp)
        mask = temp > nsr_threshold
        nsr = np.zeros((height, width), dtype=np.int)
        nsr[mask] = 1

        # candidate region detection
        temp = r - b
        temp1 = b - g
        temp = np.asarray(temp)
        temp1 = np.asarray(temp1)
        mask = (temp < cr_threshold) & (temp1 > cr_threshold)
        cr = np.zeros((height, width), dtype=np.int)
        cr[mask] = 1

        # quantization
        qr = utility.helpers(r).nonuniform_quantization()
        qg = utility.helpers(g).nonuniform_quantization()
        qb = utility.helpers(b).nonuniform_quantization()

        g_qr = utility.edge_detection(qr).sobel(5, "gradient_magnitude")
        g_qg = utility.edge_detection(qg).sobel(5, "gradient_magnitude")
        g_qb = utility.edge_detection(qb).sobel(5, "gradient_magnitude")

        g_qr = np.asarray(g_qr)
        g_qg = np.asarray(g_qg)
        g_qb = np.asarray(g_qb)

        # bgm: binary gradient magnitude
        bgm = np.zeros((height, width), dtype=np.float32)
        mask = (g_qr != 0) | (g_qg != 0) | (g_qb != 0)
        bgm[mask] = 1

        fringe_map = np.multiply(np.multiply(nsr, cr), bgm)
        fring_map = np.asarray(fringe_map)
        mask = (fringe_map == 1)

        r1 = r
        g1 = g
        b1 = b
        r1[mask] = g1[mask] = b1[mask] = (r[mask] + g[mask] + b[mask]) / 3.

        output = np.empty(np.shape(self.data), dtype=np.float32)
        output[:, :, 0] = r1
        output[:, :, 1] = g1
        output[:, :, 2] = b1

        return np.float32(output)

    def __str__(self):
        return self.name


def resort_with_bayer_pattern(data, bayer_pattern):
    """
    将data按照pattern格式重新排列成raw图上的顺序
    """
    ret = [0, 0, 0, 0]
    if (bayer_pattern == "rggb"):
        ret[0] = data[0]
        ret[1] = data[1]
        ret[2] = data[2]
        ret[3] = data[3]
    elif (bayer_pattern == "grbg"):
        ret[0] = data[1]
        ret[1] = data[0]
        ret[2] = data[3]
        ret[3] = data[2]
    elif (bayer_pattern == "bggr"):
        ret[0] = data[3]
        ret[1] = data[2]
        ret[2] = data[1]
        ret[3] = data[0]
    elif (bayer_pattern == "gbrg"):
        ret[0] = data[2]
        ret[1] = data[3]
        ret[2] = data[0]
        ret[3] = data[1]

    return ret


def bayer_channel_separation(data, pattern):
    """
    function: bayer_channel_separation
        Objective: Outputs four channels of the bayer pattern
        Input:
            data:   the bayer data
            pattern:    rggb, grbg, gbrg, or bggr
        Output:
            R, G1, G2, B (Quarter resolution images)
    """
    if (pattern == "rggb"):
        R = data[::2, ::2]
        Gr = data[::2, 1::2]
        Gb = data[1::2, ::2]
        B = data[1::2, 1::2]
    elif (pattern == "grbg"):
        Gr = data[::2, ::2]
        R = data[::2, 1::2]
        B = data[1::2, ::2]
        Gb = data[1::2, 1::2]
    elif (pattern == "gbrg"):
        Gb = data[::2, ::2]
        B = data[::2, 1::2]
        R = data[1::2, ::2]
        Gr = data[1::2, 1::2]
    elif (pattern == "bggr"):
        B = data[::2, ::2]
        Gb = data[::2, 1::2]
        Gr = data[1::2, ::2]
        R = data[1::2, 1::2]
    else:
        print("pattern must be one of these: rggb, grbg, gbrg, bggr")
        return

    return R, Gr, Gb, B


def split_raw_data(data):
    ret = []
    ret.append(data[::2, ::2])
    ret.append(data[::2, 1::2])
    ret.append(data[1::2, ::2])
    ret.append(data[1::2, 1::2])
    return ret
