import numpy as np
import cv2

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
        if(params.rawformat.height > 0 and params.rawformat.width > 0):
            self.data = np.fromfile(
                params.rawformat.filename, dtype="uint16", sep="").reshape((params.rawformat.height, params.rawformat.width))

        if (self.data is not None):
            self.name = params.rawformat.filename.split('/')[-1]
            self.__size = np.shape(self.data)
            self.data = self.data.astype(self.dtype)
            self.__raw_bit_depth = params.rawformat.bit_depth
            if(np.issubdtype(self.dtype, np.integer)):
                if (params.rawformat.bit_depth < 14):
                    self.data = np.left_shift(self.data, self.__bit_depth - params.rawformat.bit_depth)
                self.max_data = (1 << self.__bit_depth) - 1
            else:
                self.max_data = (1 << self.__raw_bit_depth) - 1

    def create_image(self, name, raw, init_value=True, depth=1):
        """
        function: 根据原来的图像，创建一个空图像
        input: 图像名称和shape
        """
        if(depth > 1):
            shape = (raw.get_height(), raw.get_width(), depth)
        else:
            shape = raw.get_size()
        if(init_value is True):
            self.data = np.zeros(shape, dtype=raw.dtype)
        self.dtype = raw.dtype
        self.name = name
        self.__size = shape
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

    def save_image(self, filename):
        # cv2.imwrite(filename, self.nowImage)
        # 解决中文路径的问题
        cv2.imencode('.jpg', self.show_data)[1].tofile(filename)

    def get_raw_data(self):
        return self.data

    def get_showimage(self):
        """
        function: convert to QImage
        brief: 把图像转换为用于显示的正常图像
        """
        if(self.data is not None):
            if (self.__color_space == "raw"):
                self.show_data = self.convert_bayer2color()
            elif (self.__color_space == "RGB"):
                self.show_data = self.convert_to_8bit()
            elif (self.__color_space == "YCrCb"):
                ratio = 256/(self.max_data + 1)
                tmp = cv2.cvtColor(self.data, cv2.COLOR_YCrCb2BGR)
                tmp = np.clip(tmp, 0, self.max_data)
                self.show_data = np.uint8(ratio * tmp)
            return self.show_data
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
        if(self.__color_space == "YCrCb"):
            self.data[:,:,0] = np.clip(self.data[:,:,0], 0, self.max_data)
            self.data[:,:,1:] = np.clip(self.data[:,:,1:], -self.max_data/2, self.max_data/2)
        else:
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
            data = np.int8(ratio * self.data)
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