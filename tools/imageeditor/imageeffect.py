import cv2
from PySide2.QtGui import QImage
import numpy as np


class ImageEffect(object):
    def __init__(self, filename):
        # self.srcImage = cv2.imread(filename)
        # 防止有中文
        self.srcImage = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), -1)
        self.srcImage = cv2.cvtColor(self.srcImage, cv2.COLOR_BGR2RGB)
        if (self.srcImage is not None):
            self.srcqImage = self.convert_qImage(self.srcImage)
            self.dstImage = self.srcImage.copy()
            self.dstqImage = self.convert_qImage(self.dstImage)
            self.nowImage = self.srcImage

    def save_image(self, img, filename):
        self.imageconvert(img)
        #cv2.imwrite(filename, self.nowImage)
        # 解决中文路径的问题
        cv2.imencode('.jpg', img)[1].tofile(filename)

    def imageconvert(self, img):
        if (img == self.srcImage):
            self.nowImage = self.srcImage
        elif (img == self.dstImage):
            self.nowImage = self.srcImage

    def get_img_point(self, img, x, y):
        return img.at(x, y)

    def get_src_image(self):
        return self.srcqImage

    def get_dst_image(self):
        return self.dstqImage

    def convert_qImage(self, img):
        return QImage(img, img.shape[1],
                      img.shape[0], img.shape[2], QImage.Format_RGB888)

    def blur(self, type):
        if (type == BlurType.BoxBlur):
            cv2.boxFilter(self.srcImage, self.dstImage, -1, BlurType.BlurSize)
        elif (type == BlurType.GaussianBlur):
            cv2.GaussianBlur(self.srcImage, self.dstImage,
                             BlurType.BlurSize, 0, 0)
        elif (type == BlurType.MediaBlur):
            cv2.medianBlur(self.srcImage, self.dstImage, BlurType.BlurSize)
        elif (type == BlurType.BilateralBlur):
            cv2.bilateralFilter(self.srcImage, self.dstImage, BlurType.BilateralSize,
                                BlurType.BilateralSize * 2, BlurType.BilateralSize / 2)

    def calcStatics(self, img, x1, y1, x2, y2):
        self.imageconvert(img)

    def calcHist(self, img, x1, y1, x2, y2):
        self.imageconvert(img)


class BlurType():
    BoxBlur = 0
    GaussianBlur = 1
    MediaBlur = 2
    BilateralBlur = 3
    BlurSize = (5, 5)
    BilateralSize = 25
