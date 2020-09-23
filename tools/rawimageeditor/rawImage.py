# =============================================================
# Import the libraries
# =============================================================
import numpy as np  # array operations
from PySide2.QtGui import QImage


# =============================================================
# class RawImageParams:

#   Helps set up necessary information/metadata of the image
# =============================================================
class RawImageParams:
    def __init__(self):
        self.channel_gain = (1.0, 1.0, 1.0, 1.0)
        self.black_level = (0, 0, 0, 0)
        self.white_level = (1, 1, 1, 1)
        self.color_matrix = [[1., .0, .0],
                             [.0, 1., .0],
                             [.0, .0, 1.]]  # xyz2cam
        self.is_load_image = False
        self.old_pipeline = []
        self.pipeline = []
        self.img_show_index = 0
        self.error_str = ""
        self.height = 0
        self.width = 0
        self.bit_depth = 0
        self.raw_format = "MIPI"
        self.pattern = "rggb"

    def set_pipeline(self, pipeline):
        self.old_pipeline = self.pipeline
        self.pipeline = pipeline

    def get_pipeline(self):
        return self.pipeline

    def update_pipeline(self, pipeline):
        self.pipeline = pipeline

    def set_channel_gain(self, channel_gain):
        self.channel_gain = channel_gain

    def get_channel_gain(self):
        return self.channel_gain

    def set_color_matrix(self, color_matrix):
        self.color_matrix = color_matrix

    def get_color_matrix(self):
        return self.color_matrix

    def set_black_level(self, black_level):
        self.black_level = np.array(black_level)

    def get_black_level(self):
        return self.black_level

    def set_error_str(self, string):
        self.error_str = string

    def get_error_str(self):
        return self.error_str

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_bit_depth(self, bit_depth):
        self.bit_depth = bit_depth

    def get_bit_depth(self):
        return self.bit_depth

    def set_raw_format(self, raw_format):
        self.raw_format = raw_format

    def get_raw_format(self):
        return self.raw_format

    def set_pattern(self, pattern):
        self.pattern = pattern

    def get_pattern(self):
        return self.pattern

    def __str__(self):
        return "Image " + " params:" + \
            "\n\tchannel gains:\t" + str(self.channel_gain) + \
            "\n\tbit depth:\t" + str(self.set_bit_depth) + \
            "\n\tblack level:\t" + str(self.black_level)

# =============================================================
# class RawImageInfo:

#   raw image info RAW图自身的属性
# =============================================================


class RawImageInfo:
    def __init__(self):
        self.data = None
        self.__color_space = "raw"
        self.__bayer_pattern = "unknown"
        # 默认以14位进行处理
        self.__bit_depth = 14
        self.__size = [0, 0]

    def load_image(self, filename, height, width, bit_depth):
        if(height > 0 and width > 0):
            self.data = np.fromfile(
                filename, dtype="uint16", sep="").reshape([height, width])

        if (self.data is not None):
            self.name = filename.split('/')[-1]
            self.__size = np.shape(self.data)
            # 由于RAW图不同的bit深度，同样的ISP流程会导致出来的亮度不一样
            # 所以在一开始需要将原始数据对齐为14bit！！
            if (bit_depth < 14):
                self.data = np.left_shift(self.data, 14-bit_depth)

    def get_raw_data(self):
        return self.data

    def get_qimage(self):
        if (self.__color_space == "raw"):
            data = np.left_shift(self.data, 2)
            return QImage(data, self.__size[1],
                          self.__size[0], QImage.Format_Grayscale16)
        elif (self.__color_space == "RGB"):
            return QImage(self.data, self.__size[1],
                          self.__size[0], QImage.Format_BGR888)
        else:
            return

    def get_size(self):
        return self.__size

    def get_width(self):
        return self.__size[1]

    def get_height(self):
        return self.__size[0]

    def get_depth(self):
        if np.ndim(self.data) > 2:
            return self.__size[2]
        else:
            return 0

    def set_color_space(self, color_space):
        self.__color_space = color_space

    def get_color_space(self):
        return self.__color_space

    def set_bayer_pattern(self, bayer_pattern):
        self.__bayer_pattern = bayer_pattern

    def get_bayer_pattern(self):
        return self.__bayer_pattern

    def set_bit_depth(self, bit_depth):
        self.__bit_depth = bit_depth

    def get_bit_depth(self):
        return self.__bit_depth

    def bayer_channel_separation(self):
        # ------------------------------------------------------
        # function: bayer_channel_separation
        #   Objective: Outputs four channels of the bayer pattern
        #   Input:
        #       data:   the bayer data
        #       pattern:    rggb, grbg, gbrg, or bggr
        #   Output:
        #       R, G1, G2, B (Quarter resolution images)
        # ------------------------------------------------------
        if (self.__bayer_pattern == "rggb"):
            R = self.data[::2, ::2]
            Gr = self.data[::2, 1::2]
            Gb = self.data[1::2, ::2]
            B = self.data[1::2, 1::2]
        elif (self.__bayer_pattern == "grbg"):
            Gr = self.data[::2, ::2]
            R = self.data[::2, 1::2]
            B = self.data[1::2, ::2]
            Gb = self.data[1::2, 1::2]
        elif (self.__bayer_pattern == "gbrg"):
            Gb = self.data[::2, ::2]
            B = self.data[::2, 1::2]
            R = self.data[1::2, ::2]
            Gr = self.data[1::2, 1::2]
        elif (self.__bayer_pattern == "bggr"):
            B = self.data[::2, ::2]
            Gb = self.data[::2, 1::2]
            Gr = self.data[1::2, ::2]
            R = self.data[1::2, 1::2]
        else:
            print("pattern must be one of these: rggb, grbg, gbrg, bggr")
            return

        return R, Gr, Gb, B

    def shuffle_bayer_pattern(self, pattern):
        """
        function: bayer_channel_integration
        brief: convert bayer pattern
        """
        R, Gr, Gb, B = self.bayer_channel_separation()
        data = np.zeros_like(self.data)
        if (pattern == "rggb"):
            data[::2, ::2] = R
            data[::2, 1::2] = Gr
            data[1::2, ::2] = Gb
            data[1::2, 1::2] = B
        elif (pattern == "grbg"):
            data[::2, ::2] = Gr
            data[::2, 1::2] = R
            data[1::2, ::2] = B
            data[1::2, 1::2] = Gb
        elif (pattern == "gbrg"):
            data[::2, ::2] = Gb
            data[::2, 1::2] = B
            data[1::2, ::2] = R
            data[1::2, 1::2] = Gr
        elif (pattern == "bggr"):
            data[::2, ::2] = B
            data[::2, 1::2] = Gb
            data[1::2, ::2] = Gr
            data[1::2, 1::2] = R
        else:
            print("pattern must be one of these: rggb, grbg, gbrg, bggr")
            return

        return data

    def bilinear_interpolation(self, x, y):
        """
        function: 双线性差值
        brief: x,y为float型，输出坐标(x,y)的值
        """

        width, height = self.__size[0], self.__size[1]

        x0 = np.floor(x).astype(int)
        x1 = x0 + 1
        y0 = np.floor(y).astype(int)
        y1 = y0 + 1

        x0 = np.clip(x0, 0, width-1)
        x1 = np.clip(x1, 0, width-1)
        y0 = np.clip(y0, 0, height-1)
        y1 = np.clip(y1, 0, height-1)

        Ia = self.data[y0, x0]
        Ib = self.data[y1, x0]
        Ic = self.data[y0, x1]
        Id = self.data[y1, x1]

        x = np.clip(x, 0, width-1)
        y = np.clip(y, 0, height-1)

        wa = (x1 - x) * (y1 - y)
        wb = (x1 - x) * (y - y0)
        wc = (x - x0) * (y1 - y)
        wd = (x - x0) * (y - y0)

        return wa * Ia + wb * Ib + wc * Ic + wd * Id
