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
        self.awb_gain = [1., 1., 1.]
        self.black_level = (0, 0, 0, 0)
        self.white_level = (1, 1, 1, 1)
        self.color_matrix = [[1., .0, .0],
                             [.0, 1., .0],
                             [.0, .0, 1.]]  # xyz2cam
        self.is_load_image = False
        self.img_show_index = 0
        self.error_str = ""
        self.height = 0
        self.width = 0
        self.bit_depth = 0
        self.raw_format = "MIPI"
        self.pattern = "rggb"
        self.__neighborhood_size_for_bad_pixel_correction = 3
        self.__demosaic_func_type = 0
        self.__demosaic_need_proc_color = 0
        self.__demosaic_need_media_filter = 0
        self.__gamma_ratio = 2.2
        # gamma 查找表的长度
        self.gamma_table_size = 512
        self.__dark_boost = 100
        self.__bright_suppress = 100
        # 自动刷新pipeline的参数，防止设置参数没有生效
        self.need_flush = False
        self.filename = ''

    def set_demosaic_func_type(self, demosaic_type):
        """
        demosaic有两种算法，设置demosaic的算法
        0: 双线性插值
        1: Malvar-He-Cutler algorithm
        2: directionally weighted gradient based interpolation algorithm
        """
        if(demosaic_type == '双线性插值'):
            index = 0
        elif(demosaic_type == 'Malvar2004'):
            index = 1
        else:
            index = 2
        if(index != self.__demosaic_func_type):
            self.__demosaic_func_type = index
            self.need_flush = True

    def get_demosaic_func_string(self):
        if(self.__demosaic_func_type == 0):
            ret = '双线性插值'
        elif(self.__demosaic_func_type == 1):
            ret = 'Malvar2004'
        else:
            ret = 'Menon2007'
        return ret
    
    def get_demosaic_funct_type(self):
        return self.__demosaic_func_type

    def set_demosaic_need_proc_color(self, value):
        """
        是否在demosaic之后启用色度抑制
        """
        self.__demosaic_need_proc_color = value

    def get_demosaic_need_proc_color(self):
        return self.__demosaic_need_proc_color

    def set_demosaic_need_media_filter(self, value):
        """
        是否在demosaic之后启用中值滤波
        """
        self.__demosaic_need_media_filter = value

    def get_demosaic_need_media_filter(self):
        return self.__demosaic_need_media_filter

    def set_dark_boost(self, value):
        """
        设置暗处提亮程度
        """
        if(value != self.__dark_boost):
            self.need_flush = True
            self.__dark_boost = value
    
    def get_dark_boost(self):
        return self.__dark_boost

    def set_bright_suppress(self, value):
        if(value != self.__bright_suppress):
            self.need_flush = True
            self.__bright_suppress = value
    
    def get_bright_suppress(self):
        return self.__bright_suppress

    def set_channel_gain(self, channel_gain):
        """
        设置raw图上RGGB每个通道的增益
        """
        self.channel_gain = channel_gain

    def get_channel_gain(self):
        return self.channel_gain

    def set_size_for_bad_pixel_correction(self, value):
        """
        设置bad pixel correction的检测核大小
        默认值为3，代表在3x3的范围内检测，这个范围内如果超过两个坏点则不生效
        """
        self.__neighborhood_size_for_bad_pixel_correction = value

    def get_size_for_bad_pixel_correction(self):
        return self.__neighborhood_size_for_bad_pixel_correction

    def set_color_matrix(self, color_matrix):
        """
        设置CCM 3x3
        """
        if(color_matrix != self.color_matrix):
            self.color_matrix = color_matrix
            self.need_flush = True

    def get_color_matrix(self):
        return self.color_matrix

    def set_black_level(self, black_level):
        if(black_level != self.black_level):
            self.black_level = black_level
            self.need_flush = True

    def get_black_level(self):
        return np.array(self.black_level)

    def set_awb_gain(self, awb_gain):
        """
        设置AWB的增益 1x3
        """
        if(awb_gain != self.awb_gain):
            self.awb_gain = awb_gain
            self.need_flush = True

    def get_awb_gain(self):
        return self.awb_gain

    def set_awb_ratio(self, awb_ratio):
        """
        设置r/g和b/g的值
        """
        awb_gain = [1, 1, 1]
        awb_gain[0] = awb_ratio[0]
        awb_gain[1] = 1
        awb_gain[2] = awb_ratio[1]
        if (awb_gain != self.awb_gain):
            self.awb_gain = awb_gain
            self.need_flush = True

    def set_gamma(self, gamma_ratio):
        """
        设置gamma的值
        """
        if(gamma_ratio != self.__gamma_ratio):
            self.__gamma_ratio = gamma_ratio
            self.need_flush = True

    def get_gamma_ratio(self):
        return self.__gamma_ratio

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

# =============================================================
# class RawImageInfo:

#   raw image info RAW图自身的属性
# =============================================================


class RawImageInfo():
    rgb_pattern_dict = {
        'r':2,
        'g':1,
        'b':0
    }

    def __init__(self):
        self.data = None
        self.show_data = None  # 用来显示图像
        self.__color_space = "raw"
        self.__bayer_pattern = "rggb"
        self.__raw_bit_depth = 12
        # 默认以14位进行处理
        self.__bit_depth = 14
        self.max_data = 4095
        self.__size = [0, 0]
        # 后续的ISP算法处理基本仅支持float类型，int类型不予以支持，但是保留了接口
        self.dtype = np.float32

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
            self.data = self.data.astype(self.dtype)
            self.__raw_bit_depth = bit_depth
            if(np.issubdtype(self.dtype, np.integer)):
                if (bit_depth < 14):
                    self.data = np.left_shift(self.data, self.__bit_depth - bit_depth)
                self.max_data = (1 << self.__bit_depth) - 1
            else:
                self.max_data = (1 << self.__raw_bit_depth) - 1
    
    def load_image_with_params(self, params):
        """
        function: 加载图像
        input: RawImageParams
        brief: 由于RAW图不同的bit深度，同样的ISP流程会导致出来的亮度不一样
        所以在RawImageInfor将原始raw图统一对齐为14bit
        """
        if(params.height > 0 and params.width > 0):
            self.data = np.fromfile(
                params.filename, dtype="uint16", sep="").reshape((params.height, params.width))

        if (self.data is not None):
            self.name = params.filename.split('/')[-1]
            self.__size = np.shape(self.data)
            self.data = self.data.astype(self.dtype)
            self.__raw_bit_depth = params.bit_depth
            if(np.issubdtype(self.dtype, np.integer)):
                if (params.bit_depth < 14):
                    self.data = np.left_shift(self.data, self.__bit_depth - params.bit_depth)
                self.max_data = (1 << self.__bit_depth) - 1
            else:
                self.max_data = (1 << self.__raw_bit_depth) - 1

    def create_image(self, name, raw, depth=1):
        """
        function: 根据原来的图像，创建一个空图像
        input: 图像名称和shape
        """
        if(depth > 1):
            shape = (raw.get_height(), raw.get_width(), depth)
        else:
            shape = raw.get_size()
        self.data = np.zeros(shape, dtype=raw.dtype)
        self.dtype = raw.dtype
        self.__raw_bit_depth = raw.get_raw_bit_depth()
        self.__bit_depth = raw.get_bit_depth()
        if(np.issubdtype(self.dtype, np.integer)):
            self.max_data = (1 << self.__bit_depth) - 1
        else:
            self.max_data = (1 << self.__raw_bit_depth) - 1
        if (len(shape) == 2):
            self.__color_space = "raw"
        elif (len(shape) == 3):
            self.__color_space = "RGB"

        if (self.data is not None):
            self.name = name
            self.__size = np.shape(self.data)

    def save_image(self, filename):
        # cv2.imwrite(filename, self.nowImage)
        # 解决中文路径的问题
        cv2.imencode('.jpg', self.show_data)[1].tofile(filename)

    def get_raw_data(self):
        return self.data

    def get_qimage(self):
        """
        function: convert to QImage
        brief: 把图像转换为QImage，用于显示
        """
        if (self.__color_space == "raw"):
            self.show_data = self.convert_bayer2color()
        elif (self.__color_space == "RGB"):
            self.show_data = self.convert_to_8bit()

        if(self.show_data is not None):
            return QImage(self.show_data, self.show_data.shape[1],
                          self.show_data.shape[0], QImage.Format_BGR888)
        else:
            return None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_size(self, size):
        self.__size = size

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
        self.max_data = (1 << self.__bit_depth) - 1

    def get_bit_depth(self):
        """
        获取当前raw图的位深
        """
        return self.__bit_depth

    def get_raw_bit_depth(self):
        """
        获取原始输入raw图的位深
        """
        return self.__raw_bit_depth

    def get_img_point(self, x, y):
        """
        获取图像中一个点的亮度值，注意颜色顺序是BGR
        如果是raw图，获取的就是当前颜色的亮度
        如果是RGB，获取的就是BGR
        如果是YUV，获取的就是YCRCB
        """
        if(x > 0 and x < self.get_width() and y > 0 and y < self.get_height()):
            if(np.issubdtype(self.dtype, np.integer)):
                right_shift_num = self.__bit_depth - self.__raw_bit_depth
                return np.right_shift(self.data[y, x], right_shift_num)
            else:
                return np.int32(self.data[y, x])
        else:
            return None

    def get_img_point_pattern(self, y, x):
        return self.__bayer_pattern[(y % 2) * 2 + x % 2]
    
    def clip_range(self):
        self.data = np.clip(self.data, 0, self.max_data)

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
        data = np.zeros(
            (self.get_height(), self.get_width(), 3), dtype="uint8")
        if (self.__bayer_pattern == "rggb" or self.__bayer_pattern == "grbg" 
            or self.__bayer_pattern == "gbrg" or self.__bayer_pattern == "bggr"):
            if(np.issubdtype(self.dtype, np.integer)):
                right_shift_num = self.get_bit_depth() - 8
                for channel, (y, x) in zip(self.__bayer_pattern, [(0, 0), (0, 1), (1, 0), (1, 1)]):
                    data[y::2, x::2, self.rgb_pattern_dict[channel]] = np.right_shift(
                        self.data[y::2, x::2], right_shift_num)
            else:
                ratio = 256/(self.max_data + 1)
                for channel, (y, x) in zip(self.__bayer_pattern, [(0, 0), (0, 1), (1, 0), (1, 1)]):
                    data[y::2, x::2, self.rgb_pattern_dict[channel]
                            ] = np.uint8(self.data[y::2, x::2] * ratio)
            return data
        else:
            print("pattern must be one of these: rggb, grbg, gbrg, bggr")
            return None

    def convert_to_8bit(self):
        data = np.zeros(
            (self.get_height(), self.get_width(), 3), dtype="uint8")
        if(np.issubdtype(self.dtype, np.integer)):
            right_shift_num = self.get_bit_depth() - 8
            data[:, :, 0] = np.right_shift(self.data[:, :, 0], right_shift_num)
            data[:, :, 1] = np.right_shift(self.data[:, :, 1], right_shift_num)
            data[:, :, 2] = np.right_shift(self.data[:, :, 2], right_shift_num)
        else:
            ratio = 256/(self.max_data + 1)
            data[:, :, 0] = np.uint8(ratio * self.data[:, :, 0])
            data[:, :, 1] = np.uint8(ratio * self.data[:, :, 1])
            data[:, :, 2] = np.uint8(ratio * self.data[:, :, 2])
        return data
    
    def convert_to_gray(self):
        data = np.zeros(
            (self.get_height(), self.get_width()), dtype=self.dtype)
        if (self.__color_space == "RGB"):
            data = 0.299 * self.data[:, :, 0] + 0.587 * self.data[:, :, 1] + 0.114 * self.data[:, :, 2]
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

    def get_raw_img_rect(self, rect):
        awb_value = dict()
        if (self.__color_space == "raw"):
            awb_value[self.get_img_point_pattern(rect[1], rect[0])] = np.mean(
                self.data[rect[1]:rect[3]:2, rect[0]:rect[2]:2])
            awb_value[self.get_img_point_pattern(
                rect[1], rect[0]+1)] = np.mean(self.data[rect[1]:rect[3]:2, (rect[0]+1):rect[2]:2])
            awb_value[self.get_img_point_pattern(
                rect[1]+1, rect[0])] = np.mean(self.data[(rect[1]+1):rect[3]:2, rect[0]:rect[2]:2])
            awb_value[self.get_img_point_pattern(rect[1]+1, rect[0]+1)] = np.mean(
                self.data[(rect[1] + 1): rect[3]:2, (rect[0] + 1): rect[2]:2])
            return (awb_value['g'] / awb_value['r'], awb_value['g'] / awb_value['b'])
        else:
            return None

    def masks_CFA_Bayer(self):
        """
        Returns the *Bayer* CFA red, green and blue masks for given pattern.
        """
        pattern = self.__bayer_pattern

        channels = dict((channel, np.zeros(self.__size, dtype=bool))
                        for channel in 'rgb')
        for channel, (y, x) in zip(pattern, [(0, 0), (0, 1), (1, 0), (1, 1)]):
            channels[channel][y::2, x::2] = True

        return tuple(channels[c] for c in 'rgb')