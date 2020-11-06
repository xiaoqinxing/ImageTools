from scipy.ndimage.filters import convolve
import numpy as np
import math
import time
import tools.rawimageeditor.utility
from scipy import signal
from tools.rawimageeditor.rawImage import RawImageInfo, RawImageParams


def demosaic(raw: RawImageInfo, params: RawImageParams):
    """
    function: demosaic
    input: raw:RawImageInfo() params:RawImageParams()
    demosaic有两种算法，设置demosaic的算法
    0: Malvar-He-Cutler algorithm
    1: directionally weighted gradient based interpolation algorithm
    """
    bayer_pattern = params.get_pattern()
    ret_img = RawImageInfo()
    ret_img.create_image(
        'after demosaic', (raw.get_height(), raw.get_width(), 3))
    # ret_img.set_name('after demosaic')
    # ret_img.set_size((raw.get_height(), raw.get_width(), 3))
    # ret_img.set_bit_depth(14)
    demosaicing_CFA_Bayer_bilinear(
        raw.get_raw_data(), ret_img.data, bayer_pattern)
    # if (params.get_demosaic_funct_type() == 0):
    #     ret_img.data = debayer_mhc(
    #         raw.get_raw_data(), bayer_pattern, [0, 65535], False)
    # else:
    #     ret_img.data = directionally_weighted_gradient_based_interpolation(raw)
    if (params.get_demosaic_need_proc_color() == 1):
        ret_img.data = post_process_local_color_ratio(raw, 0.80 * 65535)
    if (params.get_demosaic_need_media_filter() == 1):
        ret_img.data = post_process_median_filter(raw.get_raw_data())
    ret_img.set_color_space("RGB")
    return ret_img


def post_process_local_color_ratio(raw: RawImageInfo, beta):
    """
    Objective is to reduce high chroma jump
    Beta is controlling parameter, higher gives more effect,
    however, too high does not make any more change
    """

    print("----------------------------------------------------")
    print("Demosaicing post process using local color ratio...")

    data = raw.get_raw_data()

    # add beta with the data to prevent divide by zero
    data_beta = data + beta

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
    if raw.get_bayer_pattern() == "rggb":
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

    elif raw.get_bayer_pattern() == "grbg":
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

    elif raw.get_bayer_pattern() == "gbrg":
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

    elif raw.get_bayer_pattern() == "bggr":
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

    return data


def post_process_median_filter(data, edge_detect_kernel_size=3, edge_threshold=0, median_filter_kernel_size=3, clip_range=[0, 65535]):
    """
    Objective is to reduce the zipper effect around the edges
    Inputs:
        edge_detect_kernel_size: the neighborhood size used to detect edges
        edge_threshold: the threshold value above which (compared against)
                        the gradient_magnitude to declare if it is an edge
        median_filter_kernel_size: the neighborhood size used to perform
                                    median filter operation
        clip_range: used for scaling in edge_detection

    Output:
        output: median filtered output around the edges
        edge_location: a debug image to see where the edges were detected
                        based on the threshold
    """

    # detect edge locations
    edge_location = utility.edge_detection(data).sobel(
        edge_detect_kernel_size, "is_edge", edge_threshold, clip_range)

    # allocate space for output
    output = np.empty(np.shape(data), dtype=np.float32)

    if (np.ndim(data) > 2):

        for i in range(0, np.shape(data)[2]):
            output[:, :, i] = utility.helpers(data[:, :, i]).edge_wise_median(
                median_filter_kernel_size, edge_location[:, :, i])

    elif (np.ndim(data) == 2):
        output = utility.helpers(data).edge_wise_median(
            median_filter_kernel_size, edge_location)

    return output


def directionally_weighted_gradient_based_interpolation(raw: RawImageInfo):
    """
    Reference:
    http://www.arl.army.mil/arlreports/2010/ARL-TR-5061.pdf
    """

    print("Running demosaicing using directionally weighted gradient based interpolation...")
    data = raw.get_raw_data()
    # data = np.float16(data)
    bayer_pattern = raw.get_bayer_pattern()
    # Fill up the green channel
    G = fill_channel_directional_weight(
        data, bayer_pattern)

    B, R = fill_br_locations(data, G, bayer_pattern)

    width, height = raw.get_width(), raw.get_height()
    output = np.empty((height, width, 3), dtype="uint16")
    output[:, :, 0] = B.astype(np.uint16)
    output[:, :, 1] = G.astype(np.uint16)
    output[:, :, 2] = R.astype(np.uint16)

    return np.clip(output, 0, 65535)


def debayer_mhc(raw, bayer_pattern="rggb", clip_range=[0, 65535], timeshow=False):
    """
    demosaicing using Malvar-He-Cutler algorithm
    http://www.ipol.im/pub/art/2011/g_mhcd/
    """
    # convert to float32 in case it was not
    # raw = np.float32(raw)

    # dimensions
    width, height = raw.shape[1], raw.shape[0]

    # number of pixels to pad
    no_of_pixel_pad = 2
    raw = np.pad(raw,
                 (no_of_pixel_pad, no_of_pixel_pad),
                 'reflect')  # reflect would not repeat the border value

    # allocate space for the R, G, B planes
    R = np.empty((height + no_of_pixel_pad * 2, width +
                  no_of_pixel_pad * 2), dtype=np.float32)
    G = np.empty((height + no_of_pixel_pad * 2, width +
                  no_of_pixel_pad * 2), dtype=np.float32)
    B = np.empty((height + no_of_pixel_pad * 2, width +
                  no_of_pixel_pad * 2), dtype=np.float32)

    # create a RGB output
    demosaic_out = np.empty((height, width, 3), dtype=np.float32)

    # fill up the directly available values according to the Bayer pattern
    if (bayer_pattern == "rggb"):

        G[::2, 1::2] = raw[::2, 1::2]
        G[1::2, ::2] = raw[1::2, ::2]
        R[::2, ::2] = raw[::2, ::2]
        B[1::2, 1::2] = raw[1::2, 1::2]

        # Green channel
        for i in range(no_of_pixel_pad, height + no_of_pixel_pad):

            # to display progress
            t0 = time.process_time()

            for j in range(no_of_pixel_pad, width + no_of_pixel_pad):

                # G at Red location
                if (((i % 2) == 0) and ((j % 2) == 0)):
                    G[i, j] = 0.125 * np.sum([-1. * R[i-2, j],
                                              2. * G[i-1, j],
                                              -1. * R[i, j-2], 2. * G[i, j-1], 4. *
                                              R[i, j], 2. * G[i, j+1], -
                                              1. * R[i, j+2],
                                              2. * G[i+1, j],
                                              -1. * R[i+2, j]])
                # G at Blue location
                elif (((i % 2) != 0) and ((j % 2) != 0)):
                    G[i, j] = 0.125 * np.sum([-1. * B[i-2, j],
                                              2. * G[i-1, j],
                                              -1. * B[i, j-2], 2. * G[i, j-1], 4. *
                                              B[i, j], 2. * G[i, j+1], -
                                              1. * B[i, j+2],
                                              2. * G[i+1, j],
                                              -1. * B[i+2, j]])
            if (timeshow):
                elapsed_time = time.process_time() - t0
                print("Green: row index: " + str(i-1) + " of " + str(height) +
                      " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")

        # Red and Blue channel
        for i in range(no_of_pixel_pad, height + no_of_pixel_pad):

            # to display progress
            t0 = time.process_time()

            for j in range(no_of_pixel_pad, width + no_of_pixel_pad):

                # Green locations in Red rows
                if (((i % 2) == 0) and ((j % 2) != 0)):
                    # R at Green locations in Red rows
                    R[i, j] = 0.125 * np.sum([.5 * G[i-2, j],
                                              -1. * G[i-1, j-1], -
                                              1. * G[i-1, j+1],
                                              -1. * G[i, j-2], 4. * R[i, j-1], 5. *
                                              G[i, j], 4. * R[i, j+1], -
                                              1. * G[i, j+2],
                                              -1. * G[i+1, j-1], -
                                              1. * G[i+1, j+1],
                                              .5 * G[i+2, j]])

                    # B at Green locations in Red rows
                    B[i, j] = 0.125 * np.sum([-1. * G[i-2, j],
                                              -1. * G[i-1, j-1], 4. *
                                              B[i-1, j], -1. * G[i-1, j+1],
                                              .5 * G[i, j-2], 5. *
                                              G[i, j], .5 * G[i, j+2],
                                              -1. * G[i+1, j-1], 4. *
                                              B[i+1, j],  -1. * G[i+1, j+1],
                                              -1. * G[i+2, j]])

                # Green locations in Blue rows
                elif (((i % 2) != 0) and ((j % 2) == 0)):

                    # R at Green locations in Blue rows
                    R[i, j] = 0.125 * np.sum([-1. * G[i-2, j],
                                              -1. * G[i-1, j-1], 4. *
                                              R[i-1, j], -1. * G[i-1, j+1],
                                              .5 * G[i, j-2], 5. *
                                              G[i, j], .5 * G[i, j+2],
                                              -1. * G[i+1, j-1], 4. *
                                              R[i+1, j],  -1. * G[i+1, j+1],
                                              -1. * G[i+2, j]])

                    # B at Green locations in Blue rows
                    B[i, j] = 0.125 * np.sum([.5 * G[i-2, j],
                                              -1. * G[i-1, j-1], -
                                              1. * G[i-1, j+1],
                                              -1. * G[i, j-2], 4. * B[i, j-1], 5. *
                                              G[i, j], 4. * B[i, j+1], -
                                              1. * G[i, j+2],
                                              -1. * G[i+1, j-1], -
                                              1. * G[i+1, j+1],
                                              .5 * G[i+2, j]])

                # R at Blue locations
                elif (((i % 2) != 0) and ((j % 2) != 0)):
                    R[i, j] = 0.125 * np.sum([-1.5 * B[i-2, j],
                                              2. * R[i-1, j-1], 2. *
                                              R[i-1, j+1],
                                              -1.5 * B[i, j-2], 6. *
                                              B[i, j], -1.5 * B[i, j+2],
                                              2. * R[i+1, j-1], 2. *
                                              R[i+1, j+1],
                                              -1.5 * B[i+2, j]])

                # B at Red locations
                elif (((i % 2) == 0) and ((j % 2) == 0)):
                    B[i, j] = 0.125 * np.sum([-1.5 * R[i-2, j],
                                              2. * B[i-1, j-1], 2. *
                                              B[i-1, j+1],
                                              -1.5 * R[i, j-2], 6. *
                                              R[i, j], -1.5 * R[i, j+2],
                                              2. * B[i+1, j-1], 2. *
                                              B[i+1, j+1],
                                              -1.5 * R[i+2, j]])

            if (timeshow):
                elapsed_time = time.process_time() - t0
                print("Red/Blue: row index: " + str(i-1) + " of " + str(height) +
                      " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")

    elif (bayer_pattern == "gbrg"):

        G[::2, ::2] = raw[::2, ::2]
        G[1::2, 1::2] = raw[1::2, 1::2]
        R[1::2, ::2] = raw[1::2, ::2]
        B[::2, 1::2] = raw[::2, 1::2]

        # Green channel
        for i in range(no_of_pixel_pad, height + no_of_pixel_pad):

            # to display progress
            t0 = time.process_time()

            for j in range(no_of_pixel_pad, width + no_of_pixel_pad):

                # G at Red location
                if (((i % 2) != 0) and ((j % 2) == 0)):
                    G[i, j] = 0.125 * np.sum([-1. * R[i-2, j],
                                              2. * G[i-1, j],
                                              -1. * R[i, j-2], 2. * G[i, j-1], 4. *
                                              R[i, j], 2. * G[i, j+1], -
                                              1. * R[i, j+2],
                                              2. * G[i+1, j],
                                              -1. * R[i+2, j]])
                # G at Blue location
                elif (((i % 2) == 0) and ((j % 2) != 0)):
                    G[i, j] = 0.125 * np.sum([-1. * B[i-2, j],
                                              2. * G[i-1, j],
                                              -1. * B[i, j-2], 2. * G[i, j-1], 4. *
                                              B[i, j], 2. * G[i, j+1], -
                                              1. * B[i, j+2],
                                              2. * G[i+1, j],
                                              -1. * B[i+2, j]])
            if (timeshow):
                elapsed_time = time.process_time() - t0
                print("Green: row index: " + str(i-1) + " of " + str(height) +
                      " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")

        # Red and Blue channel
        for i in range(no_of_pixel_pad, height + no_of_pixel_pad):

            # to display progress
            t0 = time.process_time()

            for j in range(no_of_pixel_pad, width + no_of_pixel_pad):

                # Green locations in Red rows
                if (((i % 2) != 0) and ((j % 2) != 0)):
                    # R at Green locations in Red rows
                    R[i, j] = 0.125 * np.sum([.5 * G[i-2, j],
                                              -1. * G[i-1, j-1], -
                                              1. * G[i-1, j+1],
                                              -1. * G[i, j-2], 4. * R[i, j-1], 5. *
                                              G[i, j], 4. * R[i, j+1], -
                                              1. * G[i, j+2],
                                              -1. * G[i+1, j-1], -
                                              1. * G[i+1, j+1],
                                              .5 * G[i+2, j]])

                    # B at Green locations in Red rows
                    B[i, j] = 0.125 * np.sum([-1. * G[i-2, j],
                                              -1. * G[i-1, j-1], 4. *
                                              B[i-1, j], -1. * G[i-1, j+1],
                                              .5 * G[i, j-2], 5. *
                                              G[i, j], .5 * G[i, j+2],
                                              -1. * G[i+1, j-1], 4. *
                                              B[i+1, j],  -1. * G[i+1, j+1],
                                              -1. * G[i+2, j]])

                # Green locations in Blue rows
                elif (((i % 2) == 0) and ((j % 2) == 0)):

                    # R at Green locations in Blue rows
                    R[i, j] = 0.125 * np.sum([-1. * G[i-2, j],
                                              -1. * G[i-1, j-1], 4. *
                                              R[i-1, j], -1. * G[i-1, j+1],
                                              .5 * G[i, j-2], 5. *
                                              G[i, j], .5 * G[i, j+2],
                                              -1. * G[i+1, j-1], 4. *
                                              R[i+1, j],  -1. * G[i+1, j+1],
                                              -1. * G[i+2, j]])

                    # B at Green locations in Blue rows
                    B[i, j] = 0.125 * np.sum([.5 * G[i-2, j],
                                              -1. * G[i-1, j-1], -
                                              1. * G[i-1, j+1],
                                              -1. * G[i, j-2], 4. * B[i, j-1], 5. *
                                              G[i, j], 4. * B[i, j+1], -
                                              1. * G[i, j+2],
                                              -1. * G[i+1, j-1], -
                                              1. * G[i+1, j+1],
                                              .5 * G[i+2, j]])

                # R at Blue locations
                elif (((i % 2) == 0) and ((j % 2) != 0)):
                    R[i, j] = 0.125 * np.sum([-1.5 * B[i-2, j],
                                              2. * R[i-1, j-1], 2. *
                                              R[i-1, j+1],
                                              -1.5 * B[i, j-2], 6. *
                                              B[i, j], -1.5 * B[i, j+2],
                                              2. * R[i+1, j-1], 2. *
                                              R[i+1, j+1],
                                              -1.5 * B[i+2, j]])

                # B at Red locations
                elif (((i % 2) != 0) and ((j % 2) == 0)):
                    B[i, j] = 0.125 * np.sum([-1.5 * R[i-2, j],
                                              2. * B[i-1, j-1], 2. *
                                              B[i-1, j+1],
                                              -1.5 * R[i, j-2], 6. *
                                              R[i, j], -1.5 * R[i, j+2],
                                              2. * B[i+1, j-1], 2. *
                                              B[i+1, j+1],
                                              -1.5 * R[i+2, j]])

            if (timeshow):
                elapsed_time = time.process_time() - t0
                print("Red/Blue: row index: " + str(i-1) + " of " + str(height) +
                      " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")

    elif (bayer_pattern == "grbg"):

        G[::2, ::2] = raw[::2, ::2]
        G[1::2, 1::2] = raw[1::2, 1::2]
        R[::2, 1::2] = raw[::2, 1::2]
        B[1::2, ::2] = raw[1::2, ::2]

        # Green channel
        for i in range(no_of_pixel_pad, height + no_of_pixel_pad):

            # to display progress
            t0 = time.process_time()

            for j in range(no_of_pixel_pad, width + no_of_pixel_pad):

                # G at Red location
                if (((i % 2) == 0) and ((j % 2) != 0)):
                    G[i, j] = 0.125 * np.sum([-1. * R[i-2, j],
                                              2. * G[i-1, j],
                                              -1. * R[i, j-2], 2. * G[i, j-1], 4. *
                                              R[i, j], 2. * G[i, j+1], -
                                              1. * R[i, j+2],
                                              2. * G[i+1, j],
                                              -1. * R[i+2, j]])
                # G at Blue location
                elif (((i % 2) != 0) and ((j % 2) == 0)):
                    G[i, j] = 0.125 * np.sum([-1. * B[i-2, j],
                                              2. * G[i-1, j],
                                              -1. * B[i, j-2], 2. * G[i, j-1], 4. *
                                              B[i, j], 2. * G[i, j+1], -
                                              1. * B[i, j+2],
                                              2. * G[i+1, j],
                                              -1. * B[i+2, j]])
            if (timeshow):
                elapsed_time = time.process_time() - t0
                print("Green: row index: " + str(i-1) + " of " + str(height) +
                      " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")

        # Red and Blue channel
        for i in range(no_of_pixel_pad, height + no_of_pixel_pad):

            # to display progress
            t0 = time.process_time()

            for j in range(no_of_pixel_pad, width + no_of_pixel_pad):

                # Green locations in Red rows
                if (((i % 2) == 0) and ((j % 2) == 0)):
                    # R at Green locations in Red rows
                    R[i, j] = 0.125 * np.sum([.5 * G[i-2, j],
                                              -1. * G[i-1, j-1], -
                                              1. * G[i-1, j+1],
                                              -1. * G[i, j-2], 4. * R[i, j-1], 5. *
                                              G[i, j], 4. * R[i, j+1], -
                                              1. * G[i, j+2],
                                              -1. * G[i+1, j-1], -
                                              1. * G[i+1, j+1],
                                              .5 * G[i+2, j]])

                    # B at Green locations in Red rows
                    B[i, j] = 0.125 * np.sum([-1. * G[i-2, j],
                                              -1. * G[i-1, j-1], 4. *
                                              B[i-1, j], -1. * G[i-1, j+1],
                                              .5 * G[i, j-2], 5. *
                                              G[i, j], .5 * G[i, j+2],
                                              -1. * G[i+1, j-1], 4. *
                                              B[i+1, j],  -1. * G[i+1, j+1],
                                              -1. * G[i+2, j]])

                # Green locations in Blue rows
                elif (((i % 2) != 0) and ((j % 2) != 0)):

                    # R at Green locations in Blue rows
                    R[i, j] = 0.125 * np.sum([-1. * G[i-2, j],
                                              -1. * G[i-1, j-1], 4. *
                                              R[i-1, j], -1. * G[i-1, j+1],
                                              .5 * G[i, j-2], 5. *
                                              G[i, j], .5 * G[i, j+2],
                                              -1. * G[i+1, j-1], 4. *
                                              R[i+1, j],  -1. * G[i+1, j+1],
                                              -1. * G[i+2, j]])

                    # B at Green locations in Blue rows
                    B[i, j] = 0.125 * np.sum([.5 * G[i-2, j],
                                              -1. * G[i-1, j-1], -
                                              1. * G[i-1, j+1],
                                              -1. * G[i, j-2], 4. * B[i, j-1], 5. *
                                              G[i, j], 4. * B[i, j+1], -
                                              1. * G[i, j+2],
                                              -1. * G[i+1, j-1], -
                                              1. * G[i+1, j+1],
                                              .5 * G[i+2, j]])

                # R at Blue locations
                elif (((i % 2) != 0) and ((j % 2) == 0)):
                    R[i, j] = 0.125 * np.sum([-1.5 * B[i-2, j],
                                              2. * R[i-1, j-1], 2. *
                                              R[i-1, j+1],
                                              -1.5 * B[i, j-2], 6. *
                                              B[i, j], -1.5 * B[i, j+2],
                                              2. * R[i+1, j-1], 2. *
                                              R[i+1, j+1],
                                              -1.5 * B[i+2, j]])

                # B at Red locations
                elif (((i % 2) == 0) and ((j % 2) != 0)):
                    B[i, j] = 0.125 * np.sum([-1.5 * R[i-2, j],
                                              2. * B[i-1, j-1], 2. *
                                              B[i-1, j+1],
                                              -1.5 * R[i, j-2], 6. *
                                              R[i, j], -1.5 * R[i, j+2],
                                              2. * B[i+1, j-1], 2. *
                                              B[i+1, j+1],
                                              -1.5 * R[i+2, j]])

            if (timeshow):
                elapsed_time = time.process_time() - t0
                print("Red/Blue: row index: " + str(i-1) + " of " + str(height) +
                      " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")

    elif (bayer_pattern == "bggr"):

        G[::2, 1::2] = raw[::2, 1::2]
        G[1::2, ::2] = raw[1::2, ::2]
        R[1::2, 1::2] = raw[1::2, 1::2]
        B[::2, ::2] = raw[::2, ::2]

        # Green channel
        for i in range(no_of_pixel_pad, height + no_of_pixel_pad):

            # to display progress
            t0 = time.process_time()

            for j in range(no_of_pixel_pad, width + no_of_pixel_pad):

                # G at Red location
                if (((i % 2) != 0) and ((j % 2) != 0)):
                    G[i, j] = 0.125 * np.sum([-1. * R[i-2, j],
                                              2. * G[i-1, j],
                                              -1. * R[i, j-2], 2. * G[i, j-1], 4. *
                                              R[i, j], 2. * G[i, j+1], -
                                              1. * R[i, j+2],
                                              2. * G[i+1, j],
                                              -1. * R[i+2, j]])
                # G at Blue location
                elif (((i % 2) == 0) and ((j % 2) == 0)):
                    G[i, j] = 0.125 * np.sum([-1. * B[i-2, j],
                                              2. * G[i-1, j],
                                              -1. * B[i, j-2], 2. * G[i, j-1], 4. *
                                              B[i, j], 2. * G[i, j+1], -
                                              1. * B[i, j+2],
                                              2. * G[i+1, j],
                                              -1. * B[i+2, j]])
            if (timeshow):
                elapsed_time = time.process_time() - t0
                print("Green: row index: " + str(i-1) + " of " + str(height) +
                      " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")

        # Red and Blue channel
        for i in range(no_of_pixel_pad, height + no_of_pixel_pad):

            # to display progress
            t0 = time.process_time()

            for j in range(no_of_pixel_pad, width + no_of_pixel_pad):

                # Green locations in Red rows
                if (((i % 2) != 0) and ((j % 2) == 0)):
                    # R at Green locations in Red rows
                    R[i, j] = 0.125 * np.sum([.5 * G[i-2, j],
                                              -1. * G[i-1, j-1], -
                                              1. * G[i-1, j+1],
                                              -1. * G[i, j-2], 4. * R[i, j-1], 5. *
                                              G[i, j], 4. * R[i, j+1], -
                                              1. * G[i, j+2],
                                              -1. * G[i+1, j-1], -
                                              1. * G[i+1, j+1],
                                              .5 * G[i+2, j]])

                    # B at Green locations in Red rows
                    B[i, j] = 0.125 * np.sum([-1. * G[i-2, j],
                                              -1. * G[i-1, j-1], 4. *
                                              B[i-1, j], -1. * G[i-1, j+1],
                                              .5 * G[i, j-2], 5. *
                                              G[i, j], .5 * G[i, j+2],
                                              -1. * G[i+1, j-1], 4. *
                                              B[i+1, j],  -1. * G[i+1, j+1],
                                              -1. * G[i+2, j]])

                # Green locations in Blue rows
                elif (((i % 2) == 0) and ((j % 2) != 0)):

                    # R at Green locations in Blue rows
                    R[i, j] = 0.125 * np.sum([-1. * G[i-2, j],
                                              -1. * G[i-1, j-1], 4. *
                                              R[i-1, j], -1. * G[i-1, j+1],
                                              .5 * G[i, j-2], 5. *
                                              G[i, j], .5 * G[i, j+2],
                                              -1. * G[i+1, j-1], 4. *
                                              R[i+1, j],  -1. * G[i+1, j+1],
                                              -1. * G[i+2, j]])

                    # B at Green locations in Blue rows
                    B[i, j] = 0.125 * np.sum([.5 * G[i-2, j],
                                              -1. * G[i-1, j-1], -
                                              1. * G[i-1, j+1],
                                              -1. * G[i, j-2], 4. * B[i, j-1], 5. *
                                              G[i, j], 4. * B[i, j+1], -
                                              1. * G[i, j+2],
                                              -1. * G[i+1, j-1], -
                                              1. * G[i+1, j+1],
                                              .5 * G[i+2, j]])

                # R at Blue locations
                elif (((i % 2) == 0) and ((j % 2) == 0)):
                    R[i, j] = 0.125 * np.sum([-1.5 * B[i-2, j],
                                              2. * R[i-1, j-1], 2. *
                                              R[i-1, j+1],
                                              -1.5 * B[i, j-2], 6. *
                                              B[i, j], -1.5 * B[i, j+2],
                                              2. * R[i+1, j-1], 2. *
                                              R[i+1, j+1],
                                              -1.5 * B[i+2, j]])

                # B at Red locations
                elif (((i % 2) != 0) and ((j % 2) != 0)):
                    B[i, j] = 0.125 * np.sum([-1.5 * R[i-2, j],
                                              2. * B[i-1, j-1], 2. *
                                              B[i-1, j+1],
                                              -1.5 * R[i, j-2], 6. *
                                              R[i, j], -1.5 * R[i, j+2],
                                              2. * B[i+1, j-1], 2. *
                                              B[i+1, j+1],
                                              -1.5 * R[i+2, j]])

            if (timeshow):
                elapsed_time = time.process_time() - t0
                print("Red/Blue: row index: " + str(i-1) + " of " + str(height) +
                      " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")

    else:
        print("Invalid bayer pattern. Valid pattern can be rggb, gbrg, grbg, bggr")
        return demosaic_out  # This will be all zeros

    # Fill up the RGB output with interpolated values
    demosaic_out[0:height, 0:width, 0] = R[no_of_pixel_pad: height + no_of_pixel_pad,
                                           no_of_pixel_pad: width + no_of_pixel_pad]
    demosaic_out[0:height, 0:width, 1] = G[no_of_pixel_pad: height + no_of_pixel_pad,
                                           no_of_pixel_pad: width + no_of_pixel_pad]
    demosaic_out[0:height, 0:width, 2] = B[no_of_pixel_pad: height + no_of_pixel_pad,
                                           no_of_pixel_pad: width + no_of_pixel_pad]

    demosaic_out = np.clip(demosaic_out, clip_range[0], clip_range[1])
    return demosaic_out


def fill_channel_directional_weight(data, bayer_pattern):

    # == Calculate the directional weights (weight_N, weight_E, weight_S, weight_W.
    # where N, E, S, W stand for north, east, south, and west.)
    data = np.asarray(data)
    v = np.asarray(signal.convolve2d(
        data, [[1], [0], [-1]], mode="same", boundary="symm"))
    h = np.asarray(signal.convolve2d(
        data, [[1, 0, -1]], mode="same", boundary="symm"))

    weight_N = np.zeros(np.shape(data), dtype=np.float32)
    weight_E = np.zeros(np.shape(data), dtype=np.float32)
    weight_S = np.zeros(np.shape(data), dtype=np.float32)
    weight_W = np.zeros(np.shape(data), dtype=np.float32)

    value_N = np.zeros(np.shape(data), dtype=np.float32)
    value_E = np.zeros(np.shape(data), dtype=np.float32)
    value_S = np.zeros(np.shape(data), dtype=np.float32)
    value_W = np.zeros(np.shape(data), dtype=np.float32)

    if ((bayer_pattern == "rggb") or (bayer_pattern == "bggr")):

        # note that in the following the locations in the comments are given
        # assuming the bayer_pattern rggb

        # == CALCULATE WEIGHTS IN B LOCATIONS
        weight_N[1::2, 1::2] = np.abs(v[1::2, 1::2]) + np.abs(v[::2, 1::2])

        # repeating the column before the last to the right so that sampling
        # does not cause any dimension mismatch
        temp_h_b = np.hstack((h, np.atleast_2d(h[:, -2]).T))
        weight_E[1::2, 1::2] = np.abs(
            h[1::2, 1::2]) + np.abs(temp_h_b[1::2, 2::2])

        # repeating the row before the last row to the bottom so that sampling
        # does not cause any dimension mismatch
        temp_v_b = np.vstack((v, v[-1]))
        weight_S[1::2, 1::2] = np.abs(
            v[1::2, 1::2]) + np.abs(temp_v_b[2::2, 1::2])
        weight_W[1::2, 1::2] = np.abs(h[1::2, 1::2]) + np.abs(h[1::2, ::2])

        # == CALCULATE WEIGHTS IN R LOCATIONS
        # repeating the second row at the top of matrix so that sampling does
        # not cause any dimension mismatch, also remove the bottom row
        temp_v_r = np.delete(np.vstack((v[1], v)), -1, 0)
        weight_N[::2, ::2] = np.abs(v[::2, ::2]) + np.abs(temp_v_r[::2, ::2])

        weight_E[::2, ::2] = np.abs(h[::2, ::2]) + np.abs(h[::2, 1::2])

        weight_S[::2, ::2] = np.abs(v[::2, ::2]) + np.abs(v[1::2, ::2])

        # repeating the second column at the left of matrix so that sampling
        # does not cause any dimension mismatch, also remove the rightmost
        # column
        temp_h_r = np.delete(np.hstack((np.atleast_2d(h[:, 1]).T, h)), -1, 1)
        weight_W[::2, ::2] = np.abs(h[::2, ::2]) + np.abs(temp_h_r[::2, ::2])

        weight_N = np.divide(1., 1. + weight_N)
        weight_E = np.divide(1., 1. + weight_E)
        weight_S = np.divide(1., 1. + weight_S)
        weight_W = np.divide(1., 1. + weight_W)

        # == CALCULATE DIRECTIONAL ESTIMATES IN B LOCATIONS
        value_N[1::2, 1::2] = data[::2, 1::2] + v[::2, 1::2] / 2.

        # repeating the column before the last to the right so that sampling
        # does not cause any dimension mismatch
        temp = np.hstack((data, np.atleast_2d(data[:, -2]).T))
        value_E[1::2, 1::2] = temp[1::2, 2::2] - temp_h_b[1::2, 2::2] / 2.

        # repeating the row before the last row to the bottom so that sampling
        # does not cause any dimension mismatch
        temp = np.vstack((data, data[-1]))
        value_S[1::2, 1::2] = temp[2::2, 1::2] - temp_v_b[2::2, 1::2] / 2.

        value_W[1::2, 1::2] = data[1::2, ::2] + h[1::2, ::2] / 2.

        # == CALCULATE DIRECTIONAL ESTIMATES IN R LOCATIONS
        # repeating the second row at the top of matrix so that sampling does
        # not cause any dimension mismatch, also remove the bottom row
        temp = np.delete(np.vstack((data[1], data)), -1, 0)
        value_N[::2, ::2] = temp[::2, ::2] + temp_v_r[::2, ::2] / 2.

        value_E[::2, ::2] = data[::2, 1::2] - h[::2, 1::2] / 2.

        value_S[::2, ::2] = data[1::2, ::2] - v[1::2, ::2] / 2.

        # repeating the second column at the left of matrix so that sampling
        # does not cause any dimension mismatch, also remove the rightmost
        # column
        temp = np.delete(np.hstack((np.atleast_2d(data[:, 1]).T, data)), -1, 1)
        value_W[::2, ::2] = temp[::2, ::2] + temp_h_r[::2, ::2] / 2.

        # output = np.zeros(np.shape(data), dtype=np.float32)
        output = np.divide((np.multiply(value_N, weight_N) +
                            np.multiply(value_E, weight_E) +
                            np.multiply(value_S, weight_S) +
                            np.multiply(value_W, weight_W)),
                           (weight_N + weight_E + weight_S + weight_W))

        # output[::2, 1::2] = output[::2, 1::2]
        # output[1::2, ::2] = output[1::2, ::2]

        return output

    elif ((bayer_pattern == "gbrg") or (bayer_pattern == "grbg")):

        # note that in the following the locations in the comments are given
        # assuming the bayer_pattern gbrg

        # == CALCULATE WEIGHTS IN B LOCATIONS
        # repeating the second row at the top of matrix so that sampling does
        # not cause any dimension mismatch, also remove the bottom row
        temp_v_b = np.delete(np.vstack((v[1], v)), -1, 0)
        weight_N[::2, 1::2] = np.abs(
            v[::2, 1::2]) + np.abs(temp_v_b[::2, 1::2])

        # repeating the column before the last to the right so that sampling
        # does not cause any dimension mismatch
        temp_h_b = np.hstack((h, np.atleast_2d(h[:, -2]).T))
        weight_E[::2, 1::2] = np.abs(
            h[::2, 1::2]) + np.abs(temp_h_b[::2, 2::2])

        # repeating the row before the last row to the bottom so that sampling
        # does not cause any dimension mismatch
        weight_S[::2, 1::2] = np.abs(v[::2, 1::2]) + np.abs(v[1::2, 1::2])
        weight_W[::2, 1::2] = np.abs(h[::2, 1::2]) + np.abs(h[::2, ::2])

        # == CALCULATE WEIGHTS IN R LOCATIONS
        weight_N[1::2, ::2] = np.abs(v[1::2, ::2]) + np.abs(v[::2, ::2])
        weight_E[1::2, ::2] = np.abs(h[1::2, ::2]) + np.abs(h[1::2, 1::2])

        # repeating the row before the last row to the bottom so that sampling
        # does not cause any dimension mismatch
        temp_v_r = np.vstack((v, v[-1]))
        weight_S[1::2, ::2] = np.abs(
            v[1::2, ::2]) + np.abs(temp_v_r[2::2, ::2])

        # repeating the second column at the left of matrix so that sampling
        # does not cause any dimension mismatch, also remove the rightmost
        # column
        temp_h_r = np.delete(np.hstack((np.atleast_2d(h[:, 1]).T, h)), -1, 1)
        weight_W[1::2, ::2] = np.abs(
            h[1::2, ::2]) + np.abs(temp_h_r[1::2, ::2])

        weight_N = np.divide(1., 1. + weight_N)
        weight_E = np.divide(1., 1. + weight_E)
        weight_S = np.divide(1., 1. + weight_S)
        weight_W = np.divide(1., 1. + weight_W)

        # == CALCULATE DIRECTIONAL ESTIMATES IN B LOCATIONS
        # repeating the second row at the top of matrix so that sampling does
        # not cause any dimension mismatch, also remove the bottom row
        temp = np.delete(np.vstack((data[1], data)), -1, 0)
        value_N[::2, 1::2] = temp[::2, 1::2] + temp_v_b[::2, 1::2] / 2.

        # repeating the column before the last to the right so that sampling
        # does not cause any dimension mismatch
        temp = np.hstack((data, np.atleast_2d(data[:, -2]).T))
        value_E[::2, 1::2] = temp[::2, 2::2] - temp_h_b[::2, 2::2] / 2.

        # repeating the row before the last row to the bottom so that sampling
        # does not cause any dimension mismatch
        value_S[::2, 1::2] = data[1::2, 1::2] - v[1::2, 1::2] / 2.

        value_W[::2, 1::2] = data[::2, ::2] + h[::2, ::2] / 2.

        # == CALCULATE DIRECTIONAL ESTIMATES IN R LOCATIONS
        # repeating the second row at the top of matrix so that sampling does
        # not cause any dimension mismatch, also remove the bottom row
        value_N[1::2, ::2] = data[::2, ::2] + v[::2, ::2] / 2.
        value_E[1::2, ::2] = data[1::2, 1::2] - h[1::2, 1::2] / 2.

        # repeating the row before the last row to the bottom so that sampling
        # does not cause any dimension mismatch
        temp = np.vstack((data, data[-1]))
        value_S[1::2, ::2] = temp[2::2, ::2] - temp_v_r[2::2, ::2] / 2.

        # repeating the second column at the left of matrix so that sampling
        # does not cause any dimension mismatch, also remove the rightmost
        # column
        temp = np.delete(np.hstack((np.atleast_2d(data[:, 1]).T, data)), -1, 1)
        value_W[1::2, ::2] = temp[1::2, ::2] + temp_h_r[1::2, ::2] / 2.

        output = np.zeros(np.shape(data), dtype=np.float32)
        output = np.divide((np.multiply(value_N, weight_N) +
                            np.multiply(value_E, weight_E) +
                            np.multiply(value_S, weight_S) +
                            np.multiply(value_W, weight_W)),
                           (weight_N + weight_E + weight_S + weight_W))

        output[::2, ::2] = data[::2, ::2]
        output[1::2, 1::2] = data[1::2, 1::2]

        return output


def fill_br_locations(data, G, bayer_pattern):

    # Fill up the B/R values interpolated at R/B locations
    # B = np.zeros(np.shape(data), dtype=np.float32)
    # R = np.zeros(np.shape(data), dtype=np.float32)

    data = np.asarray(data)
    G = np.asarray(G)
    d1 = np.asarray(signal.convolve2d(
        data, [[-1, 0, 0], [0, 0, 0], [0, 0, 1]], mode="same", boundary="symm"))
    d2 = np.asarray(signal.convolve2d(
        data, [[0, 0, 1], [0, 0, 0], [-1, 0, 0]], mode="same", boundary="symm"))

    df_NE = np.asarray(signal.convolve2d(
        G, [[0, 0, 0], [0, 1, 0], [-1, 0, 0]], mode="same", boundary="symm"))
    df_SE = np.asarray(signal.convolve2d(
        G, [[-1, 0, 0], [0, 1, 0], [0, 0, 0]], mode="same", boundary="symm"))
    df_SW = np.asarray(signal.convolve2d(
        G, [[0, 0, -1], [0, 1, 0], [0, 0, 0]], mode="same", boundary="symm"))
    df_NW = np.asarray(signal.convolve2d(
        G, [[0, 0, 0], [0, 1, 0], [0, 0, -1]], mode="same", boundary="symm"))

    weight_NE = np.zeros(np.shape(data), dtype=np.float32)
    weight_SE = np.zeros(np.shape(data), dtype=np.float32)
    weight_SW = np.zeros(np.shape(data), dtype=np.float32)
    weight_NW = np.zeros(np.shape(data), dtype=np.float32)

    value_NE = np.zeros(np.shape(data), dtype=np.float32)
    value_SE = np.zeros(np.shape(data), dtype=np.float32)
    value_SW = np.zeros(np.shape(data), dtype=np.float32)
    value_NW = np.zeros(np.shape(data), dtype=np.float32)

    if ((bayer_pattern == "rggb") or (bayer_pattern == "bggr")):

        # == weights for B in R locations
        weight_NE[::2, ::2] = np.abs(d2[::2, ::2]) + np.abs(df_NE[::2, ::2])
        weight_SE[::2, ::2] = np.abs(d1[::2, ::2]) + np.abs(df_SE[::2, ::2])
        weight_SW[::2, ::2] = np.abs(d2[::2, ::2]) + np.abs(df_SW[::2, ::2])
        weight_NW[::2, ::2] = np.abs(d1[::2, ::2]) + np.abs(df_NW[::2, ::2])

        # == weights for R in B locations
        weight_NE[1::2, 1::2] = np.abs(
            d2[1::2, 1::2]) + np.abs(df_NE[1::2, 1::2])
        weight_SE[1::2, 1::2] = np.abs(
            d1[1::2, 1::2]) + np.abs(df_SE[1::2, 1::2])
        weight_SW[1::2, 1::2] = np.abs(
            d2[1::2, 1::2]) + np.abs(df_SW[1::2, 1::2])
        weight_NW[1::2, 1::2] = np.abs(
            d1[1::2, 1::2]) + np.abs(df_NW[1::2, 1::2])

        weight_NE = np.divide(1., 1. + weight_NE)
        weight_SE = np.divide(1., 1. + weight_SE)
        weight_SW = np.divide(1., 1. + weight_SW)
        weight_NW = np.divide(1., 1. + weight_NW)

        # == directional estimates of B in R locations
        # repeating the second row at the top of matrix so that sampling does
        # not cause any dimension mismatch, also remove the bottom row
        temp = np.delete(np.vstack((data[1], data)), -1, 0)
        value_NE[::2, ::2] = temp[::2, 1::2] + df_NE[::2, ::2] / 2.
        value_SE[::2, ::2] = data[1::2, 1::2] + df_SE[::2, ::2] / 2.
        # repeating the second column at the left of matrix so that sampling
        # does not cause any dimension mismatch, also remove the rightmost
        # column
        temp = np.delete(np.hstack((np.atleast_2d(data[:, 1]).T, data)), -1, 1)
        value_SW[::2, ::2] = temp[1::2, ::2] + df_SW[::2, ::2] / 2.

        # repeating the second row at the top of matrix so that sampling does
        # not cause any dimension mismatch, also remove the bottom row
        temp = np.delete(np.vstack((data[1], data)), -1, 0)
        # repeating the second column at the left of matrix so that sampling
        # does not cause any dimension mismatch, also remove the rightmost
        # column
        temp = np.delete(np.hstack((np.atleast_2d(temp[:, 1]).T, temp)), -1, 1)
        value_NW[::2, ::2] = temp[::2, ::2] + df_NW[::2, ::2]

        # == directional estimates of R in B locations
        # repeating the column before the last to the right so that sampling
        # does not cause any dimension mismatch
        temp = np.hstack((data, np.atleast_2d(data[:, -2]).T))
        value_NE[1::2, 1::2] = temp[::2, 2::2] + df_NE[1::2, 1::2] / 2.
        # repeating the column before the last to the right so that sampling
        # does not cause any dimension mismatch
        temp = np.hstack((data, np.atleast_2d(data[:, -2]).T))
        # repeating the row before the last row to the bottom so that sampling
        # does not cause any dimension mismatch
        temp = np.vstack((temp, temp[-1]))
        value_SE[1::2, 1::2] = temp[2::2, 2::2] + df_SE[1::2, 1::2] / 2.
        # repeating the row before the last row to the bottom so that sampling
        # does not cause any dimension mismatch
        temp = np.vstack((data, data[-1]))
        value_SW[1::2, 1::2] = temp[2::2, ::2] + df_SW[1::2, 1::2] / 2.
        value_NW[1::2, 1::2] = data[::2, ::2] + df_NW[1::2, 1::2] / 2.

        RB = np.divide(np.multiply(weight_NE, value_NE) +
                       np.multiply(weight_SE, value_SE) +
                       np.multiply(weight_SW, value_SW) +
                       np.multiply(weight_NW, value_NW),
                       (weight_NE + weight_SE + weight_SW + weight_NW))

        if (bayer_pattern == "rggb"):

            R[1::2, 1::2] = RB[1::2, 1::2]
            R[::2, ::2] = data[::2, ::2]
            B[::2, ::2] = RB[::2, ::2]
            B[1::2, 1::2] = data[1::2, 1::2]

        elif (bayer_pattern == "bggr"):
            R[::2, ::2] = RB[::2, ::2]
            R[1::2, 1::2] = data[1::2, 1::2]
            B[1::2, 1::2] = RB[1::2, 1::2]
            B[::2, ::2] = data[::2, ::2]

        R[1::2, ::2] = G[1::2, ::2]
        R[::2, 1::2] = G[::2, 1::2]
        R = fill_channel_directional_weight(R, "gbrg")

        B[1::2, ::2] = G[1::2, ::2]
        B[::2, 1::2] = G[::2, 1::2]
        B = fill_channel_directional_weight(B, "gbrg")

    elif ((bayer_pattern == "grbg") or (bayer_pattern == "gbrg")):
        # == weights for B in R locations
        weight_NE[::2, 1::2] = np.abs(d2[::2, 1::2]) + np.abs(df_NE[::2, 1::2])
        weight_SE[::2, 1::2] = np.abs(d1[::2, 1::2]) + np.abs(df_SE[::2, 1::2])
        weight_SW[::2, 1::2] = np.abs(d2[::2, 1::2]) + np.abs(df_SW[::2, 1::2])
        weight_NW[::2, 1::2] = np.abs(d1[::2, 1::2]) + np.abs(df_NW[::2, 1::2])

        # == weights for R in B locations
        weight_NE[1::2, ::2] = np.abs(d2[1::2, ::2]) + np.abs(df_NE[1::2, ::2])
        weight_SE[1::2, ::2] = np.abs(d1[1::2, ::2]) + np.abs(df_SE[1::2, ::2])
        weight_SW[1::2, ::2] = np.abs(d2[1::2, ::2]) + np.abs(df_SW[1::2, ::2])
        weight_NW[1::2, ::2] = np.abs(d1[1::2, ::2]) + np.abs(df_NW[1::2, ::2])

        weight_NE = np.divide(1., 1. + weight_NE)
        weight_SE = np.divide(1., 1. + weight_SE)
        weight_SW = np.divide(1., 1. + weight_SW)
        weight_NW = np.divide(1., 1. + weight_NW)

        # == directional estimates of B in R locations
        # repeating the second row at the top of matrix so that sampling does
        # not cause any dimension mismatch, also remove the bottom row
        temp = np.delete(np.vstack((data[1], data)), -1, 0)
        # repeating the column before the last to the right so that sampling
        # does not cause any dimension mismatch
        temp = np.hstack((temp, np.atleast_2d(temp[:, -2]).T))
        value_NE[::2, 1::2] = temp[::2, 2::2] + df_NE[::2, 1::2] / 2.
        # repeating the column before the last to the right so that sampling
        # does not cause any dimension mismatch
        temp = np.hstack((data, np.atleast_2d(data[:, -2]).T))
        value_SE[::2, 1::2] = temp[1::2, 2::2] + df_SE[::2, 1::2] / 2.
        value_SW[::2, 1::2] = data[1::2, ::2] + df_SW[::2, 1::2] / 2.

        # repeating the second row at the top of matrix so that sampling does
        # not cause any dimension mismatch, also remove the bottom row
        temp = np.delete(np.vstack((data[1], data)), -1, 0)
        value_NW[::2, 1::2] = temp[::2, ::2] + df_NW[::2, 1::2]

        # == directional estimates of R in B locations
        value_NE[1::2, ::2] = data[::2, 1::2] + df_NE[1::2, ::2] / 2.
        # repeating the column before the last to the right so that sampling
        # does not cause any dimension mismatch
        temp = np.hstack((data, np.atleast_2d(data[:, -2]).T))
        # repeating the row before the last row to the bottom so that sampling
        # does not cause any dimension mismatch
        temp = np.vstack((temp, temp[-1]))
        value_SE[1::2, ::2] = temp[2::2, 1::2] + df_SE[1::2, ::2] / 2.
        # repeating the row before the last row to the bottom so that sampling
        # does not cause any dimension mismatch
        temp = np.vstack((data, data[-1]))
        # repeating the second column at the left of matrix so that sampling
        # does not cause any dimension mismatch, also remove the rightmost
        # column
        temp = np.delete(np.hstack((np.atleast_2d(temp[:, 1]).T, temp)), -1, 1)
        value_SW[1::2, ::2] = temp[2::2, ::2] + df_SW[1::2, ::2] / 2.
        # repeating the second column at the left of matrix so that sampling
        # does not cause any dimension mismatch, also remove the rightmost
        # column
        temp = np.delete(np.hstack((np.atleast_2d(data[:, 1]).T, data)), -1, 1)
        value_NW[1::2, ::2] = temp[::2, ::2] + df_NW[1::2, ::2] / 2.

        RB = np.divide(np.multiply(weight_NE, value_NE) +
                       np.multiply(weight_SE, value_SE) +
                       np.multiply(weight_SW, value_SW) +
                       np.multiply(weight_NW, value_NW),
                       (weight_NE + weight_SE + weight_SW + weight_NW))

        if (bayer_pattern == "grbg"):

            R[1::2, ::2] = RB[1::2, ::2]
            R[::2, 1::2] = data[::2, 1::2]
            B[::2, 1::2] = RB[::2, 1::2]
            B[1::2, ::2] = data[1::2, ::2]

        elif (bayer_pattern == "gbrg"):
            R[::2, 1::2] = RB[::2, 1::2]
            R[1::2, ::2] = data[1::2, ::2]
            B[1::2, ::2] = RB[1::2, ::2]
            B[::2, 1::2] = data[::2, 1::2]

        R[::2, ::2] = G[::2, ::2]
        R[1::2, 1::2] = G[1::2, 1::2]
        R = fill_channel_directional_weight(R, "rggb")

        B[1::2, 1::2] = G[1::2, 1::2]
        B[::2, ::2] = G[::2, ::2]
        B = fill_channel_directional_weight(B, "rggb")

    return B, R


# # =============================================================
# # function: dbayer_mhc_fast
# #   demosaicing using Malvar-He-Cutler algorithm
# #   http://www.ipol.im/pub/art/2011/g_mhcd/
# # =============================================================
# def debayer_mhc_fast(raw, bayer_pattern="rggb", clip_range=[0, 65535], timeshow=False):
#
#     # convert to float32 in case it was not
#     raw = np.float32(raw)
#
#     # dimensions
#     width, height = utility.helpers(raw).get_width_height()
#
#     # allocate space for the R, G, B planes
#     R = np.empty((height, width), dtype = np.float32)
#     G = np.empty((height, width), dtype = np.float32)
#     B = np.empty((height, width), dtype = np.float32)
#
#     # create a RGB output
#     demosaic_out = np.empty( (height, width, 3), dtype = np.float32 )
#
#     # define the convolution kernels
#     kernel_g_at_rb = [[0., 0., -1., 0., 0.],\
#                       [0., 0., 2., 0., 0.],\
#                       [-1., 2., 4., 2., -1.],\
#                       [0., 0., 2., 0., 0.],\
#                       [0., 0., -1., 0., 0.]] * .125
#
#     kernel_r_at_gr = [[0., 0., .5, 0., 0.],\
#                       [0., -1., 0., -1., 0.],\
#                       [-1., 4., 5., 4., -1.],\
#                       [0., -1., 0., -1., 0.],\
#                       [0., 0., .5, 0., 0.]] * .125
#
#     kernel_b_at_gr = [[0., 0., -1., 0., 0.],\
#                       [0., -1., 4., -1., 0.],\
#                       [.5., 0., 5., 0., .5],\
#                       [0., -1., 4., -1., 0],\
#                       [0., 0., -1., 0., 0.]] * .125
#
#     kernel_r_at_gb = [[0., 0., -1., 0., 0.],\
#                       [0., -1., 4., -1., 0.],\
#                       [.5, 0., 5., 0., .5],\
#                       [0., -1., 4., -1., 0.],\
#                       [0., 0., -1., 0., 0.]] * .125
#
#     kernel_b_at_gb = [[0., 0., .5, 0., 0.],\
#                       [0., -1., 0., -1., 0.],\
#                       [-1., 4., 5., 4., -1.],\
#                       [0., -1., 0., -1., 0.],\
#                       [0., 0., .5, 0., 0.]] * .125
#
#     kernel_r_at_b = [[0., 0., -1.5, 0., 0.],\
#                      [0., 2., 0., 2., 0.],\
#                      [-1.5, 0., 6., 0., -1.5],\
#                      [0., 2., 0., 2., 0.],\
#                      [0., 0., -1.5, 0., 0.]] * .125
#
#     kernel_b_at_r = [[0., 0., -1.5, 0., 0.],\
#                      [0., 2., 0., 2., 0.],\
#                      [-1.5, 0., 6., 0., -1.5],\
#                      [0., 2., 0., 2., 0.],\
#                      [0., 0., -1.5, 0., 0.]] * .125
#
#
#
#     # fill up the directly available values according to the Bayer pattern
#     if (bayer_pattern == "rggb"):
#
#         G[::2, 1::2]  = raw[::2, 1::2]
#         G[1::2, ::2]  = raw[1::2, ::2]
#         R[::2, ::2]   = raw[::2, ::2]
#         B[1::2, 1::2] = raw[1::2, 1::2]
#
#         # Green channel
#         for i in range(no_of_pixel_pad, height + no_of_pixel_pad):
#
#             # to display progress
#             t0 = time.process_time()
#
#             for j in range(no_of_pixel_pad, width + no_of_pixel_pad):
#
#                 # G at Red location
#                 if (((i % 2) == 0) and ((j % 2) == 0)):
#                     G[i, j] = 0.125 * np.sum([-1. * R[i-2, j], \
#                     2. * G[i-1, j], \
#                     -1. * R[i, j-2], 2. * G[i, j-1], 4. * R[i,j], 2. * G[i, j+1], -1. * R[i, j+2],\
#                     2. * G[i+1, j], \
#                     -1. * R[i+2, j]])
#                 # G at Blue location
#                 elif (((i % 2) != 0) and ((j % 2) != 0)):
#                     G[i, j] = 0.125 * np.sum([-1. * B[i-2, j], \
#                     2. * G[i-1, j], \
#                     -1. * B[i, j-2], 2. * G[i, j-1], 4. * B[i,j], 2. * G[i, j+1], -1. * B[i, j+2], \
#                     2. * G[i+1, j],\
#                     -1. * B[i+2, j]])
#             if (timeshow):
#                 elapsed_time = time.process_time() - t0
#                 print("Green: row index: " + str(i-1) + " of " + str(height) + \
#                       " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")
#
#         # Red and Blue channel
#         for i in range(no_of_pixel_pad, height + no_of_pixel_pad):
#
#             # to display progress
#             t0 = time.process_time()
#
#             for j in range(no_of_pixel_pad, width + no_of_pixel_pad):
#
#                 # Green locations in Red rows
#                 if (((i % 2) == 0) and ((j % 2) != 0)):
#                     # R at Green locations in Red rows
#                     R[i, j] = 0.125 * np.sum([.5 * G[i-2, j],\
#                      -1. * G[i-1, j-1], -1. * G[i-1, j+1], \
#                      -1. * G[i, j-2], 4. * R[i, j-1], 5. * G[i,j], 4. * R[i, j+1], -1. * G[i, j+2], \
#                      -1. * G[i+1, j-1], -1. * G[i+1, j+1], \
#                       .5 * G[i+2, j]])
#
#                     # B at Green locations in Red rows
#                     B[i, j] = 0.125 * np.sum([-1. * G[i-2, j], \
#                     -1. * G[i-1, j-1], 4. * B[i-1, j], -1. * G[i-1, j+1], \
#                     .5 * G[i, j-2], 5. * G[i,j], .5 * G[i, j+2], \
#                     -1. * G[i+1, j-1], 4. * B[i+1,j],  -1. * G[i+1, j+1], \
#                     -1. * G[i+2, j]])
#
#                 # Green locations in Blue rows
#                 elif (((i % 2) != 0) and ((j % 2) == 0)):
#
#                     # R at Green locations in Blue rows
#                     R[i, j] = 0.125 * np.sum([-1. * G[i-2, j], \
#                     -1. * G[i-1, j-1], 4. * R[i-1, j], -1. * G[i-1, j+1], \
#                     .5 * G[i, j-2], 5. * G[i,j], .5 * G[i, j+2], \
#                     -1. * G[i+1, j-1], 4. * R[i+1, j],  -1. * G[i+1, j+1], \
#                     -1. * G[i+2, j]])
#
#                     # B at Green locations in Blue rows
#                     B[i, j] = 0.125 * np.sum([.5 * G[i-2, j], \
#                     -1. * G [i-1, j-1], -1. * G[i-1, j+1], \
#                     -1. * G[i, j-2], 4. * B[i, j-1], 5. * G[i,j], 4. * B[i, j+1], -1. * G[i, j+2], \
#                     -1. * G[i+1, j-1], -1. * G[i+1, j+1], \
#                     .5 * G[i+2, j]])
#
#                 # R at Blue locations
#                 elif (((i % 2) != 0) and ((j % 2) != 0)):
#                     R[i, j] = 0.125 * np.sum([-1.5 * B[i-2, j], \
#                     2. * R[i-1, j-1], 2. * R[i-1, j+1], \
#                     -1.5 * B[i, j-2], 6. * B[i,j], -1.5 * B[i, j+2], \
#                     2. * R[i+1, j-1], 2. * R[i+1, j+1], \
#                     -1.5 * B[i+2, j]])
#
#                 # B at Red locations
#                 elif (((i % 2) == 0) and ((j % 2) == 0)):
#                     B[i, j] = 0.125 * np.sum([-1.5 * R[i-2, j], \
#                     2. * B[i-1, j-1], 2. * B[i-1, j+1], \
#                     -1.5 * R[i, j-2], 6. * R[i,j], -1.5 * R[i, j+2], \
#                     2. * B[i+1, j-1], 2. * B[i+1, j+1], \
#                     -1.5 * R[i+2, j]])
#
#             if (timeshow):
#                 elapsed_time = time.process_time() - t0
#                 print("Red/Blue: row index: " + str(i-1) + " of " + str(height) + \
#                       " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")
#
#
#     elif (bayer_pattern == "gbrg"):
#
#         G[::2, ::2]   = raw[::2, ::2]
#         G[1::2, 1::2] = raw[1::2, 1::2]
#         R[1::2, ::2]  = raw[1::2, ::2]
#         B[::2, 1::2]  = raw[::2, 1::2]
#
#         # Green channel
#         for i in range(no_of_pixel_pad, height + no_of_pixel_pad):
#
#             # to display progress
#             t0 = time.process_time()
#
#             for j in range(no_of_pixel_pad, width + no_of_pixel_pad):
#
#                 # G at Red location
#                 if (((i % 2) != 0) and ((j % 2) == 0)):
#                     G[i, j] = 0.125 * np.sum([-1. * R[i-2, j], \
#                     2. * G[i-1, j], \
#                     -1. * R[i, j-2], 2. * G[i, j-1], 4. * R[i,j], 2. * G[i, j+1], -1. * R[i, j+2],\
#                     2. * G[i+1, j], \
#                     -1. * R[i+2, j]])
#                 # G at Blue location
#                 elif (((i % 2) == 0) and ((j % 2) != 0)):
#                     G[i, j] = 0.125 * np.sum([-1. * B[i-2, j], \
#                     2. * G[i-1, j], \
#                     -1. * B[i, j-2], 2. * G[i, j-1], 4. * B[i,j], 2. * G[i, j+1], -1. * B[i, j+2], \
#                     2. * G[i+1, j],\
#                     -1. * B[i+2, j]])
#             if (timeshow):
#                 elapsed_time = time.process_time() - t0
#                 print("Green: row index: " + str(i-1) + " of " + str(height) + \
#                       " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")
#
#         # Red and Blue channel
#         for i in range(no_of_pixel_pad, height + no_of_pixel_pad):
#
#             # to display progress
#             t0 = time.process_time()
#
#             for j in range(no_of_pixel_pad, width + no_of_pixel_pad):
#
#                 # Green locations in Red rows
#                 if (((i % 2) != 0) and ((j % 2) != 0)):
#                     # R at Green locations in Red rows
#                     R[i, j] = 0.125 * np.sum([.5 * G[i-2, j],\
#                      -1. * G[i-1, j-1], -1. * G[i-1, j+1], \
#                      -1. * G[i, j-2], 4. * R[i, j-1], 5. * G[i,j], 4. * R[i, j+1], -1. * G[i, j+2], \
#                      -1. * G[i+1, j-1], -1. * G[i+1, j+1], \
#                       .5 * G[i+2, j]])
#
#                     # B at Green locations in Red rows
#                     B[i, j] = 0.125 * np.sum([-1. * G[i-2, j], \
#                     -1. * G[i-1, j-1], 4. * B[i-1, j], -1. * G[i-1, j+1], \
#                     .5 * G[i, j-2], 5. * G[i,j], .5 * G[i, j+2], \
#                     -1. * G[i+1, j-1], 4. * B[i+1,j],  -1. * G[i+1, j+1], \
#                     -1. * G[i+2, j]])
#
#                 # Green locations in Blue rows
#                 elif (((i % 2) == 0) and ((j % 2) == 0)):
#
#                     # R at Green locations in Blue rows
#                     R[i, j] = 0.125 * np.sum([-1. * G[i-2, j], \
#                     -1. * G[i-1, j-1], 4. * R[i-1, j], -1. * G[i-1, j+1], \
#                     .5 * G[i, j-2], 5. * G[i,j], .5 * G[i, j+2], \
#                     -1. * G[i+1, j-1], 4. * R[i+1, j],  -1. * G[i+1, j+1], \
#                     -1. * G[i+2, j]])
#
#                     # B at Green locations in Blue rows
#                     B[i, j] = 0.125 * np.sum([.5 * G[i-2, j], \
#                     -1. * G [i-1, j-1], -1. * G[i-1, j+1], \
#                     -1. * G[i, j-2], 4. * B[i, j-1], 5. * G[i,j], 4. * B[i, j+1], -1. * G[i, j+2], \
#                     -1. * G[i+1, j-1], -1. * G[i+1, j+1], \
#                     .5 * G[i+2, j]])
#
#                 # R at Blue locations
#                 elif (((i % 2) == 0) and ((j % 2) != 0)):
#                     R[i, j] = 0.125 * np.sum([-1.5 * B[i-2, j], \
#                     2. * R[i-1, j-1], 2. * R[i-1, j+1], \
#                     -1.5 * B[i, j-2], 6. * B[i,j], -1.5 * B[i, j+2], \
#                     2. * R[i+1, j-1], 2. * R[i+1, j+1], \
#                     -1.5 * B[i+2, j]])
#
#                 # B at Red locations
#                 elif (((i % 2) != 0) and ((j % 2) == 0)):
#                     B[i, j] = 0.125 * np.sum([-1.5 * R[i-2, j], \
#                     2. * B[i-1, j-1], 2. * B[i-1, j+1], \
#                     -1.5 * R[i, j-2], 6. * R[i,j], -1.5 * R[i, j+2], \
#                     2. * B[i+1, j-1], 2. * B[i+1, j+1], \
#                     -1.5 * R[i+2, j]])
#
#             if (timeshow):
#                 elapsed_time = time.process_time() - t0
#                 print("Red/Blue: row index: " + str(i-1) + " of " + str(height) + \
#                       " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")
#
#     elif (bayer_pattern == "grbg"):
#
#         G[::2, ::2]   = raw[::2, ::2]
#         G[1::2, 1::2] = raw[1::2, 1::2]
#         R[::2, 1::2]  = raw[::2, 1::2]
#         B[1::2, ::2]  = raw[1::2, ::2]
#
#         # Green channel
#         for i in range(no_of_pixel_pad, height + no_of_pixel_pad):
#
#             # to display progress
#             t0 = time.process_time()
#
#             for j in range(no_of_pixel_pad, width + no_of_pixel_pad):
#
#                 # G at Red location
#                 if (((i % 2) == 0) and ((j % 2) != 0)):
#                     G[i, j] = 0.125 * np.sum([-1. * R[i-2, j], \
#                     2. * G[i-1, j], \
#                     -1. * R[i, j-2], 2. * G[i, j-1], 4. * R[i,j], 2. * G[i, j+1], -1. * R[i, j+2],\
#                     2. * G[i+1, j], \
#                     -1. * R[i+2, j]])
#                 # G at Blue location
#                 elif (((i % 2) != 0) and ((j % 2) == 0)):
#                     G[i, j] = 0.125 * np.sum([-1. * B[i-2, j], \
#                     2. * G[i-1, j], \
#                     -1. * B[i, j-2], 2. * G[i, j-1], 4. * B[i,j], 2. * G[i, j+1], -1. * B[i, j+2], \
#                     2. * G[i+1, j],\
#                     -1. * B[i+2, j]])
#             if (timeshow):
#                 elapsed_time = time.process_time() - t0
#                 print("Green: row index: " + str(i-1) + " of " + str(height) + \
#                       " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")
#
#         # Red and Blue channel
#         for i in range(no_of_pixel_pad, height + no_of_pixel_pad):
#
#             # to display progress
#             t0 = time.process_time()
#
#             for j in range(no_of_pixel_pad, width + no_of_pixel_pad):
#
#                 # Green locations in Red rows
#                 if (((i % 2) == 0) and ((j % 2) == 0)):
#                     # R at Green locations in Red rows
#                     R[i, j] = 0.125 * np.sum([.5 * G[i-2, j],\
#                      -1. * G[i-1, j-1], -1. * G[i-1, j+1], \
#                      -1. * G[i, j-2], 4. * R[i, j-1], 5. * G[i,j], 4. * R[i, j+1], -1. * G[i, j+2], \
#                      -1. * G[i+1, j-1], -1. * G[i+1, j+1], \
#                       .5 * G[i+2, j]])
#
#                     # B at Green locations in Red rows
#                     B[i, j] = 0.125 * np.sum([-1. * G[i-2, j], \
#                     -1. * G[i-1, j-1], 4. * B[i-1, j], -1. * G[i-1, j+1], \
#                     .5 * G[i, j-2], 5. * G[i,j], .5 * G[i, j+2], \
#                     -1. * G[i+1, j-1], 4. * B[i+1,j],  -1. * G[i+1, j+1], \
#                     -1. * G[i+2, j]])
#
#                 # Green locations in Blue rows
#                 elif (((i % 2) != 0) and ((j % 2) != 0)):
#
#                     # R at Green locations in Blue rows
#                     R[i, j] = 0.125 * np.sum([-1. * G[i-2, j], \
#                     -1. * G[i-1, j-1], 4. * R[i-1, j], -1. * G[i-1, j+1], \
#                     .5 * G[i, j-2], 5. * G[i,j], .5 * G[i, j+2], \
#                     -1. * G[i+1, j-1], 4. * R[i+1, j],  -1. * G[i+1, j+1], \
#                     -1. * G[i+2, j]])
#
#                     # B at Green locations in Blue rows
#                     B[i, j] = 0.125 * np.sum([.5 * G[i-2, j], \
#                     -1. * G [i-1, j-1], -1. * G[i-1, j+1], \
#                     -1. * G[i, j-2], 4. * B[i, j-1], 5. * G[i,j], 4. * B[i, j+1], -1. * G[i, j+2], \
#                     -1. * G[i+1, j-1], -1. * G[i+1, j+1], \
#                     .5 * G[i+2, j]])
#
#                 # R at Blue locations
#                 elif (((i % 2) != 0) and ((j % 2) == 0)):
#                     R[i, j] = 0.125 * np.sum([-1.5 * B[i-2, j], \
#                     2. * R[i-1, j-1], 2. * R[i-1, j+1], \
#                     -1.5 * B[i, j-2], 6. * B[i,j], -1.5 * B[i, j+2], \
#                     2. * R[i+1, j-1], 2. * R[i+1, j+1], \
#                     -1.5 * B[i+2, j]])
#
#                 # B at Red locations
#                 elif (((i % 2) == 0) and ((j % 2) != 0)):
#                     B[i, j] = 0.125 * np.sum([-1.5 * R[i-2, j], \
#                     2. * B[i-1, j-1], 2. * B[i-1, j+1], \
#                     -1.5 * R[i, j-2], 6. * R[i,j], -1.5 * R[i, j+2], \
#                     2. * B[i+1, j-1], 2. * B[i+1, j+1], \
#                     -1.5 * R[i+2, j]])
#
#             if (timeshow):
#                 elapsed_time = time.process_time() - t0
#                 print("Red/Blue: row index: " + str(i-1) + " of " + str(height) + \
#                       " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")
#
#     elif (bayer_pattern == "bggr"):
#
#         G[::2, 1::2]  = raw[::2, 1::2]
#         G[1::2, ::2]  = raw[1::2, ::2]
#         R[1::2, 1::2] = raw[1::2, 1::2]
#         B[::2, ::2]   = raw[::2, ::2]
#
#         # Green channel
#         for i in range(no_of_pixel_pad, height + no_of_pixel_pad):
#
#             # to display progress
#             t0 = time.process_time()
#
#             for j in range(no_of_pixel_pad, width + no_of_pixel_pad):
#
#                 # G at Red location
#                 if (((i % 2) != 0) and ((j % 2) != 0)):
#                     G[i, j] = 0.125 * np.sum([-1. * R[i-2, j], \
#                     2. * G[i-1, j], \
#                     -1. * R[i, j-2], 2. * G[i, j-1], 4. * R[i,j], 2. * G[i, j+1], -1. * R[i, j+2],\
#                     2. * G[i+1, j], \
#                     -1. * R[i+2, j]])
#                 # G at Blue location
#                 elif (((i % 2) == 0) and ((j % 2) == 0)):
#                     G[i, j] = 0.125 * np.sum([-1. * B[i-2, j], \
#                     2. * G[i-1, j], \
#                     -1. * B[i, j-2], 2. * G[i, j-1], 4. * B[i,j], 2. * G[i, j+1], -1. * B[i, j+2], \
#                     2. * G[i+1, j],\
#                     -1. * B[i+2, j]])
#             if (timeshow):
#                 elapsed_time = time.process_time() - t0
#                 print("Green: row index: " + str(i-1) + " of " + str(height) + \
#                       " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")
#
#         # Red and Blue channel
#         for i in range(no_of_pixel_pad, height + no_of_pixel_pad):
#
#             # to display progress
#             t0 = time.process_time()
#
#             for j in range(no_of_pixel_pad, width + no_of_pixel_pad):
#
#                 # Green locations in Red rows
#                 if (((i % 2) != 0) and ((j % 2) == 0)):
#                     # R at Green locations in Red rows
#                     R[i, j] = 0.125 * np.sum([.5 * G[i-2, j],\
#                      -1. * G[i-1, j-1], -1. * G[i-1, j+1], \
#                      -1. * G[i, j-2], 4. * R[i, j-1], 5. * G[i,j], 4. * R[i, j+1], -1. * G[i, j+2], \
#                      -1. * G[i+1, j-1], -1. * G[i+1, j+1], \
#                       .5 * G[i+2, j]])
#
#                     # B at Green locations in Red rows
#                     B[i, j] = 0.125 * np.sum([-1. * G[i-2, j], \
#                     -1. * G[i-1, j-1], 4. * B[i-1, j], -1. * G[i-1, j+1], \
#                     .5 * G[i, j-2], 5. * G[i,j], .5 * G[i, j+2], \
#                     -1. * G[i+1, j-1], 4. * B[i+1,j],  -1. * G[i+1, j+1], \
#                     -1. * G[i+2, j]])
#
#                 # Green locations in Blue rows
#                 elif (((i % 2) == 0) and ((j % 2) != 0)):
#
#                     # R at Green locations in Blue rows
#                     R[i, j] = 0.125 * np.sum([-1. * G[i-2, j], \
#                     -1. * G[i-1, j-1], 4. * R[i-1, j], -1. * G[i-1, j+1], \
#                     .5 * G[i, j-2], 5. * G[i,j], .5 * G[i, j+2], \
#                     -1. * G[i+1, j-1], 4. * R[i+1, j],  -1. * G[i+1, j+1], \
#                     -1. * G[i+2, j]])
#
#                     # B at Green locations in Blue rows
#                     B[i, j] = 0.125 * np.sum([.5 * G[i-2, j], \
#                     -1. * G [i-1, j-1], -1. * G[i-1, j+1], \
#                     -1. * G[i, j-2], 4. * B[i, j-1], 5. * G[i,j], 4. * B[i, j+1], -1. * G[i, j+2], \
#                     -1. * G[i+1, j-1], -1. * G[i+1, j+1], \
#                     .5 * G[i+2, j]])
#
#                 # R at Blue locations
#                 elif (((i % 2) == 0) and ((j % 2) == 0)):
#                     R[i, j] = 0.125 * np.sum([-1.5 * B[i-2, j], \
#                     2. * R[i-1, j-1], 2. * R[i-1, j+1], \
#                     -1.5 * B[i, j-2], 6. * B[i,j], -1.5 * B[i, j+2], \
#                     2. * R[i+1, j-1], 2. * R[i+1, j+1], \
#                     -1.5 * B[i+2, j]])
#
#                 # B at Red locations
#                 elif (((i % 2) != 0) and ((j % 2) != 0)):
#                     B[i, j] = 0.125 * np.sum([-1.5 * R[i-2, j], \
#                     2. * B[i-1, j-1], 2. * B[i-1, j+1], \
#                     -1.5 * R[i, j-2], 6. * R[i,j], -1.5 * R[i, j+2], \
#                     2. * B[i+1, j-1], 2. * B[i+1, j+1], \
#                     -1.5 * R[i+2, j]])
#
#             if (timeshow):
#                 elapsed_time = time.process_time() - t0
#                 print("Red/Blue: row index: " + str(i-1) + " of " + str(height) + \
#                       " | elapsed time: " + "{:.3f}".format(elapsed_time) + " seconds")
#
#     else:
#         print("Invalid bayer pattern. Valid pattern can be rggb, gbrg, grbg, bggr")
#         return demosaic_out # This will be all zeros
#
#     # Fill up the RGB output with interpolated values
#     demosaic_out[0:height, 0:width, 0] = R[no_of_pixel_pad : height + no_of_pixel_pad, \
#                                            no_of_pixel_pad : width + no_of_pixel_pad]
#     demosaic_out[0:height, 0:width, 1] = G[no_of_pixel_pad : height + no_of_pixel_pad, \
#                                            no_of_pixel_pad : width + no_of_pixel_pad]
#     demosaic_out[0:height, 0:width, 2] = B[no_of_pixel_pad : height + no_of_pixel_pad, \
#                                            no_of_pixel_pad : width + no_of_pixel_pad]
#
#     demosaic_out = np.clip(demosaic_out, clip_range[0], clip_range[1])
#     return demosaic_out


def demosaicing_CFA_Bayer_bilinear(CFA, output, pattern='rggb'):
    """
    Returns the demosaiced *RGB* colourspace array from given *Bayer* CFA using
    bilinear interpolation.

    Parameters
    ----------
    CFA : array_like
        *Bayer* CFA.
    pattern : unicode, optional
        **{'RGGB', 'BGGR', 'GRBG', 'GBRG'}**,
        Arrangement of the colour filters on the pixel array.

    Returns
    -------
    ndarray
        *RGB* colourspace array.

    Notes
    -----
    -   The definition output is not clipped in range [0, 1] : this allows for
        direct HDRI / radiance image generation on *Bayer* CFA data and post
        demosaicing of the high dynamic range data as showcased in this
        `Jupyter Notebook <https://github.com/colour-science/colour-hdri/\
blob/develop/colour_hdri/examples/\
examples_merge_from_raw_files_with_post_demosaicing.ipynb>`__.

    References
    ----------
    :cite:`Losson2010c`

    Examples
    --------
    >>> import numpy as np
    >>> CFA = np.array(
    ...     [[0.30980393, 0.36078432, 0.30588236, 0.3764706],
    ...      [0.35686275, 0.39607844, 0.36078432, 0.40000001]])
    >>> demosaicing_CFA_Bayer_bilinear(CFA)
    array([[[ 0.69705884,  0.17941177,  0.09901961],
            [ 0.46176472,  0.4509804 ,  0.19803922],
            [ 0.45882354,  0.27450981,  0.19901961],
            [ 0.22941177,  0.5647059 ,  0.30000001]],
    <BLANKLINE>
           [[ 0.23235295,  0.53529412,  0.29705883],
            [ 0.15392157,  0.26960785,  0.59411766],
            [ 0.15294118,  0.4509804 ,  0.59705884],
            [ 0.07647059,  0.18431373,  0.90000002]]])
    >>> CFA = np.array(
    ...     [[0.3764706, 0.360784320, 0.40784314, 0.3764706],
    ...      [0.35686275, 0.30980393, 0.36078432, 0.29803923]])
    >>> demosaicing_CFA_Bayer_bilinear(CFA, 'BGGR')
    array([[[ 0.07745098,  0.17941177,  0.84705885],
            [ 0.15490197,  0.4509804 ,  0.5882353 ],
            [ 0.15196079,  0.27450981,  0.61176471],
            [ 0.22352942,  0.5647059 ,  0.30588235]],
    <BLANKLINE>
           [[ 0.23235295,  0.53529412,  0.28235295],
            [ 0.4647059 ,  0.26960785,  0.19607843],
            [ 0.45588237,  0.4509804 ,  0.20392157],
            [ 0.67058827,  0.18431373,  0.10196078]]])
    """

    # CFA = as_float_array(CFA)
    R_m, G_m, B_m = masks_CFA_Bayer(CFA.shape, pattern)

    H_G = np.uint16(
        [[0, 1, 0],
         [1, 4, 1],
         [0, 1, 0]])  # yapf: disable

    H_RB = np.uint16(
        [[1, 2, 1],
         [2, 4, 2],
         [1, 2, 1]])  # yapf: disable

    output[:, :, 2] = convolve(CFA * R_m, H_RB)/4
    output[:, :, 1] = convolve(CFA * G_m, H_G)/4
    output[:, :, 0] = convolve(CFA * B_m, H_RB)/4

    del R_m, G_m, B_m, H_RB, H_G
    return


def masks_CFA_Bayer(shape, pattern='rggb'):
    """
    Returns the *Bayer* CFA red, green and blue masks for given pattern.
    Parameters
    ----------
    shape : array_like
        Dimensions of the *Bayer* CFA.
    pattern : unicode, optional
        **{'RGGB', 'BGGR', 'GRBG', 'GBRG'}**,
        Arrangement of the colour filters on the pixel array.
    Returns
    -------
    tuple
        *Bayer* CFA red, green and blue masks.
    Examples
    --------
    >>> from pprint import pprint
    >>> shape = (3, 3)
    >>> pprint(masks_CFA_Bayer(shape))
    (array([[ True, False,  True],
           [False, False, False],
           [ True, False,  True]], dtype=bool),
     array([[False,  True, False],
           [ True, False,  True],
           [False,  True, False]], dtype=bool),
     array([[False, False, False],
           [False,  True, False],
           [False, False, False]], dtype=bool))
    >>> pprint(masks_CFA_Bayer(shape, 'BGGR'))
    (array([[False, False, False],
           [False,  True, False],
           [False, False, False]], dtype=bool),
     array([[False,  True, False],
           [ True, False,  True],
           [False,  True, False]], dtype=bool),
     array([[ True, False,  True],
           [False, False, False],
           [ True, False,  True]], dtype=bool))
    """

    pattern = pattern.lower()

    channels = dict((channel, np.zeros(shape, dtype=np.uint16))
                    for channel in 'rgb')
    for channel, (y, x) in zip(pattern, [(0, 0), (0, 1), (1, 0), (1, 1)]):
        channels[channel][y::2, x::2] = 1

    return tuple(channels[c] for c in 'rgb')
