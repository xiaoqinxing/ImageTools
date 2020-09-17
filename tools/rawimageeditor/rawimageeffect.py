import cv2
from PySide2.QtGui import QImage
import numpy as np


class ImageEffect(object):
    def __init__(self):
        self.is_load_image = False
    
    def set_format(self, size, bayer_pattern, bit_depth, awb_gain, black_level, ccm, gamma):
        self.height,self.width = size
        self.bayer_pattern = bayer_pattern
        self.bit_depth = bit_depth
        self.awb_gain = awb_gain
        self.black_level = black_level
        self.ccm = ccm
        self.gamma = gamma

    
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
        if (self.srcImage is not None):
            self.height = self.srcImage.shape[0]
            self.width = self.srcImage.shape[1]
            self.depth = self.srcImage.shape[2]
            self.dstImage = self.srcImage.copy()
            self.nowImage = self.srcImage
            self.is_load_image = True

    def save_image(self, img, filename):
        self.imageconvert(img)
        # cv2.imwrite(filename, self.nowImage)
        # 解决中文路径的问题
        cv2.imencode('.jpg', self.nowImage)[1].tofile(filename)

    def imageconvert(self, img):
        if (img == self.srcImage):
            self.nowImage = self.srcImage
        elif (img == self.dstImage):
            self.nowImage = self.dstImage

    def get_img_point(self, x, y):
        if(x > 0 and x < self.width and y > 0 and y < self.height):
            return self.nowImage[y, x]
        else:
            return None

    def get_src_image(self):
        return self.convert_qImage(self.srcImage)

    def get_dst_image(self):
        return self.convert_qImage(self.dstImage)

    def convert_qImage(self, img):
        if self.depth == 3:
            return QImage(img, img.shape[1],
                          img.shape[0], QImage.Format_BGR888)
        elif self.depth == 4:
            return QImage(img, img.shape[1],
                          img.shape[0], QImage.Format_BGR32)
        else:
            return

    def blur(self, type):
        if (type == BlurType.BoxBlur):
            self.dstImage = cv2.boxFilter(self.srcImage, -1, BlurType.BlurSize)
        elif (type == BlurType.GaussianBlur):
            self.dstImage = cv2.GaussianBlur(self.srcImage, BlurType.BlurSize, 0, 0)
        elif (type == BlurType.MediaBlur):
            self.dstImage = cv2.medianBlur(self.srcImage, BlurType.medianSize)
        elif (type == BlurType.BilateralBlur):
            self.dstImage = cv2.bilateralFilter(self.srcImage, BlurType.BilateralSize,
                                BlurType.BilateralSize * 2, BlurType.BilateralSize / 2)

    def calcStatics(self, img, rect):
        x1, y1, x2, y2 = rect
        self.imageconvert(img)
        i1 = max(x1, 0)
        i2 = min(x2, self.width)
        j1 = max(y1, 0)
        j2 = min(self.height, y2)
        if (i2 > i1 and j2 > j1):
            image = self.nowImage[j1:j2, i1:i2]
            (average_rgb,stddv_rgb) = cv2.meanStdDev(image)
            snr_rgb = average_rgb/stddv_rgb
            image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
            (average_yuv,stddv_yuv) = cv2.meanStdDev(image)
            snr_yuv = average_yuv/stddv_yuv
            rgb_ratio = [0.0,0.0]
            awb_gain = [0.0,0.0,0.0]
            rgb_ratio[0] = average_rgb[2]/average_rgb[1]
            rgb_ratio[1] = average_rgb[0]/average_rgb[1]
            awb_gain[0] = 1/rgb_ratio[0]
            awb_gain[1] = 1
            awb_gain[2] = 1/rgb_ratio[1]
            enable_rect = [i1,j1,i2-i1,j2-j1]
            return (average_rgb,snr_rgb,average_yuv,snr_yuv,rgb_ratio,awb_gain,enable_rect)
            


    def calcHist(self, img, rect):
        x1, y1, x2, y2 = rect
        self.imageconvert(img)
        # height, width, depth = img.shape
        i1 = max(x1, 0)
        i2 = min(x2, self.width)
        j1 = max(y1, 0)
        j2 = min(self.height, y2)
        if (i2 > i1 and j2 > j1):
            image = self.nowImage[j1:j2, i1:i2]
            chans = cv2.split(image)
            b_hist = (cv2.calcHist([chans[0]], [0], None, [
                256], [0, 256]))
            g_hist = (cv2.calcHist([chans[1]], [0], None, [
                256], [0, 256]))
            r_hist = (cv2.calcHist([chans[2]], [0], None, [
                256], [0, 256]))
            # 转为灰度图，然后算亮度直方图
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            y_hist = (cv2.calcHist([image], [0], None, [
                256], [0, 256]))
            r_hist.reshape(1, 256)
            g_hist.reshape(1, 256)
            b_hist.reshape(1, 256)
            y_hist.reshape(1, 256)
            return (r_hist, g_hist, b_hist, y_hist)


class BlurType():
    BoxBlur = 0
    GaussianBlur = 1
    MediaBlur = 2
    BilateralBlur = 3
    BlurSize = (5, 5)
    medianSize = 5
    BilateralSize = 25

