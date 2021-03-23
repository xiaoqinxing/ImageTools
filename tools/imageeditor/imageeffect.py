import cv2
import numpy as np
from components.customwidget import critical


class WaterMarkType():
    """
    水印的类型
    """
    NoWaterMark = -1
    TransparentWaterMark = 0
    SpaceWaterMark = 1
    FrequencyWaterMark = 2


class WaterMarkParams():
    """
    水印的参数
    transparent：透明度 范围：0-100
    watermark_type：水印的类型 范围：WaterMarkType
    threshold：水印二值化的阈值 范围：0-255
    size：水印的缩放大小 范围：0-1000
    """
    transparent = 0
    watermark_type = WaterMarkType.NoWaterMark
    threshold = 50
    size = 100
    filename = ""


class ImageEffect(object):
    nowImage = None
    img_index = 0
    def __init__(self):
        self.is_load_image = False

    def load_image(self, filename):
        # 防止有中文
        # self.srcImage = cv2.imread(filename)
        self.srcImage = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), -1)

        # 根据不同的颜色通道，进行不同的颜色转换
        # if(self.depth == 3):
        #     self.srcImage = cv2.cvtColor(self.srcImage, cv2.COLOR_BGR2RGB)
        # elif(self.depth == 4):
        #     self.srcImage = cv2.cvtColor(self.srcImage, cv2.COLOR_BGR2BGRA)
        # else:
        #     self.srcImage == None
        self.depth = 0
        if (self.srcImage is not None):
            self.height = self.srcImage.shape[0]
            self.width = self.srcImage.shape[1]
            self.depth = self.srcImage.shape[2]
            self.dstImage = self.srcImage.copy()
            self.nowImage = self.srcImage
            self.is_load_image = True

    def save_image(self, img, filename):
        # cv2.imwrite(filename, self.nowImage)
        # 解决中文路径的问题
        cv2.imencode('.jpg', self.nowImage)[1].tofile(filename)

    def imageconvert(self, index):
        """
        func: 切换需要操作的img， 0 为原图，1为目标图
        """
        if (index == 0):
            self.nowImage = self.srcImage
            self.img_index = 0
        elif (index == 1):
            self.nowImage = self.dstImage
            self.img_index = 1
    
    def get_img_index(self):
        return self.img_index

    def get_img_point(self, x, y):
        """
        获取图像中一个点的RGB值，注意颜色顺序是BGR
        """
        if(x > 0 and x < self.width and y > 0 and y < self.height):
            return self.nowImage[y, x]
        else:
            return None

    def get_src_image(self):
        return self.srcImage

    def get_dst_image(self):
        return self.dstImage

    def blur(self, type):
        if (type == BlurType.BoxBlur):
            self.dstImage = cv2.boxFilter(self.srcImage, -1, BlurType.BlurSize)
        elif (type == BlurType.GaussianBlur):
            self.dstImage = cv2.GaussianBlur(
                self.srcImage, BlurType.BlurSize, 0, 0)
        elif (type == BlurType.MediaBlur):
            self.dstImage = cv2.medianBlur(self.srcImage, BlurType.medianSize)
        elif (type == BlurType.BilateralBlur):
            self.dstImage = cv2.bilateralFilter(self.srcImage, BlurType.BilateralSize,
                                                BlurType.BilateralSize * 2, BlurType.BilateralSize / 2)

    def set_watermark_img(self, filename):
        self.watermark_img = cv2.imdecode(
            np.fromfile(filename, dtype=np.uint8), -1)
        if (self.watermark_img is not None):
            self.watermark_img_height = self.watermark_img.shape[0]
            self.watermark_img_width = self.watermark_img.shape[1]
        else:
            critical('水印图片无法打开')

    def set_watermark_show(self, params: WaterMarkParams):
        """
        func: 设置水印的显示
        先进行水印的缩放，如果是空域水印，就进行转换成灰度图二值化，如果是半透明水印，就进行透明化处理，最后和原图进行融合
        """
        if(params.watermark_type != WaterMarkType.NoWaterMark):
            watermark_img_tmp = self.watermark_img.copy()
            self.dstImage = self.srcImage.copy()
            if(params.size <= 1000 and params.size > 0):
                watermark_img_tmp = cv2.resize(watermark_img_tmp, (int(
                    self.watermark_img_width*params.size/100), int(self.watermark_img_height*params.size/100)), interpolation=cv2.INTER_AREA)
            if(params.watermark_type == WaterMarkType.SpaceWaterMark and params.threshold <= 255 and params.threshold >= 0):
                watermark_img_tmp = cv2.cvtColor(
                    watermark_img_tmp, cv2.COLOR_BGR2GRAY)
                watermark_img_tmp = cv2.threshold(
                    watermark_img_tmp, params.threshold, 255, cv2.THRESH_BINARY)[1]
                watermark_img_tmp = cv2.cvtColor(
                    watermark_img_tmp, cv2.COLOR_GRAY2BGR)
            width = min(watermark_img_tmp.shape[1], self.width)
            height = min(watermark_img_tmp.shape[0], self.height)
            w_start = int((self.width - width)/2)
            h_start = int((self.height - height)/2)
            clip_img = self.dstImage[h_start:height +
                                     h_start, w_start:width+w_start]
            if(params.watermark_type == WaterMarkType.TransparentWaterMark and params.transparent <= 100 and params.transparent >= 0):
                self.dstImage[h_start:height+h_start, w_start:width+w_start] = cv2.addWeighted(
                    watermark_img_tmp[:height, :width], 1-params.transparent/100, clip_img, params.transparent/100, 0)
            else:
                self.dstImage[h_start:height+h_start, w_start:width +
                              w_start] = watermark_img_tmp[:height, :width]

    def generate_watermark(self, params: WaterMarkParams):
        if(params.watermark_type == WaterMarkType.SpaceWaterMark):
            watermark_img_tmp = self.watermark_img.copy()
            self.dstImage = self.srcImage.copy()
            watermark_img_tmp = cv2.cvtColor(watermark_img_tmp, cv2.COLOR_BGR2GRAY)
            watermark_img_tmp = cv2.threshold(
                    watermark_img_tmp, params.threshold, 1, cv2.THRESH_BINARY)[1]
            width = min(watermark_img_tmp.shape[1], self.width)
            height = min(watermark_img_tmp.shape[0], self.height)
            w_start = int((self.width - width)/2)
            h_start = int((self.height - height)/2)
            self.dstImage[h_start:height+h_start, w_start:width+w_start, 0] &= 254
            self.dstImage[h_start:height+h_start, w_start:width+w_start, 0] |= watermark_img_tmp[:height, :width]
    
    def analysis_space_watermark(self):
        tmp = cv2.threshold(self.nowImage[:,:,0], 0, 255, cv2.THRESH_BINARY)[1]
        self.dstImage = cv2.cvtColor(tmp, cv2.COLOR_GRAY2BGR)

class BlurType():
    BoxBlur = 0
    GaussianBlur = 1
    MediaBlur = 2
    BilateralBlur = 3
    BlurSize = (5, 5)
    medianSize = 5
    BilateralSize = 25
