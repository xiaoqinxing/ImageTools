# =============================================================
# Import the libraries
# =============================================================
import numpy as np  # array operations
from PySide2.QtGui import QImage
import cv2


# =============================================================
# class RawImageParams:

#   Helps set up necessary information/metadata of the image
# =============================================================
class RawImageParams():
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


class RawImageInfo():
    def __init__(self):
        self.data = None
        self.show_data = None # 用来显示图像
        self.__color_space = "raw"
        self.__bayer_pattern = "rggb"
        self.__raw_bit_depth = 12
        # 默认以14位进行处理
        self.__bit_depth = 14
        self.__size = [0, 0]

    def load_image(self, filename, height, width, bit_depth):
        """
        function: 加载图像
        input: 图像宽高和位深
        brief: 由于RAW图不同的bit深度，同样的ISP流程会导致出来的亮度不一样
        所以在RawImageInfor将原始raw图统一对齐为14bit
        """
        if(height > 0 and width > 0):
            self.data = np.fromfile(
                filename, dtype="uint16", sep="").reshape((height, width))

        if (self.data is not None):
            self.name = filename.split('/')[-1]
            self.__size = np.shape(self.data)
            self.__raw_bit_depth = bit_depth
            if (bit_depth < 14):
                self.data = np.left_shift(self.data, 14-bit_depth)

    def get_raw_data(self):
        return self.data

    def get_qimage(self):
        """
        function: convert to QImage
        brief: 把图像转换为QImage，用于显示
        """
        if (self.__color_space == "raw"):
            self.show_data = self.convert_bayer2color()
            return QImage(self.show_data, self.show_data.shape[1],
                          self.show_data.shape[0], QImage.Format_BGR888)
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
    
    def get_img_point(self,x,y):
        """
        获取图像中一个点的亮度值，注意颜色顺序是BGR
        如果是raw图，获取的就是当前颜色的亮度
        如果是RGB，获取的就是BGR
        如果是YUV，获取的就是YCRCB
        """
        if(x > 0 and x < self.get_width() and y > 0 and y < self.get_height()):
            right_shift_num = self.__bit_depth - self.__raw_bit_depth
            return np.right_shift(self.data[y, x], right_shift_num)
        else:
            return None

    def bayer_channel_separation(self):
        """
        function: bayer_channel_separation
        Output: R, G1, G2, B (Quarter resolution images)
        """
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
    
    def convert_bayer2color(self):
        """
        function: convert bayer to color
        brief: 将bayer用8位的rgb显示，不进行demosaic
        """
        data = np.zeros((self.get_height(), self.get_width(),3),dtype="uint8")
        right_shift_num = self.get_bit_depth() - 8
        if (self.__bayer_pattern == "rggb"):
            data[::2, ::2, 2] = np.right_shift(self.data[::2, ::2], right_shift_num)
            data[::2, 1::2, 1] = np.right_shift(self.data[::2, 1::2], right_shift_num)
            data[1::2, ::2, 1] = np.right_shift(self.data[1::2, ::2], right_shift_num)
            data[1::2, 1::2, 0] = np.right_shift(self.data[1::2, 1::2], right_shift_num)
        elif (self.__bayer_pattern == "grbg"):
            data[::2, ::2, 1] = np.right_shift(self.data[::2, ::2], right_shift_num)
            data[::2, 1::2, 2] = np.right_shift(self.data[::2, 1::2], right_shift_num)
            data[1::2, ::2, 0] = np.right_shift(self.data[1::2, ::2], right_shift_num)
            data[1::2, 1::2, 1] = np.right_shift(self.data[1::2, 1::2], right_shift_num)
        elif (self.__bayer_pattern == "gbrg"):
            data[::2, ::2, 1] = np.right_shift(self.data[::2, ::2], right_shift_num)
            data[::2, 1::2, 0] = np.right_shift(self.data[::2, 1::2], right_shift_num)
            data[1::2, ::2, 2] = np.right_shift(self.data[1::2, ::2], right_shift_num)
            data[1::2, 1::2, 1] = np.right_shift(self.data[1::2, 1::2], right_shift_num)
        elif (self.__bayer_pattern == "bggr"):
            data[::2, ::2, 0] = np.right_shift(self.data[::2, ::2], right_shift_num)
            data[::2, 1::2, 1] = np.right_shift(self.data[::2, 1::2], right_shift_num)
            data[1::2, ::2, 1] = np.right_shift(self.data[1::2, ::2], right_shift_num)
            data[1::2, 1::2, 2] = np.right_shift(self.data[1::2, 1::2], right_shift_num)
        else:
            print("pattern must be one of these: rggb, grbg, gbrg, bggr")
            return None
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
