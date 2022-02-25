import cv2
import numpy as np
from PySide2.QtGui import QPixmap, QImage

YUV_FORMAT_MAP = {
    'NV21': cv2.COLOR_YUV2BGR_NV21,
    'NV12': cv2.COLOR_YUV2BGR_NV12,
    'YUV420': cv2.COLOR_YUV2BGR_I420,
    'YUV422': cv2.COLOR_YUV2BGR_Y422,
    'UYVY': cv2.COLOR_YUV2BGR_UYVY,
    'YUYV': cv2.COLOR_YUV2BGR_YUYV,
    'YVYU': cv2.COLOR_YUV2BGR_YVYU,
}


class ImageBasic:
    img = None
    imgpath = None  # 图片路径
    height = 0
    width = 0
    depth = 0  # 通道数

    def __update_attr(self):
        if (self.img is not None):
            self.height = self.img.shape[0]
            self.width = self.img.shape[1]
            self.depth = self.img.shape[2]

    # load image
    def load_image(self, img):
        self.img = img
        self.__update_attr()

    def copy_image(self, img):
        self.img = img.copy()
        self.__update_attr()

    def load_imagefile(self, filename):
        # 防止有中文，因此不使用imread
        self.img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), 1)
        self.imgpath = filename
        self.__update_attr()

    def load_yuvfile(self, filename, height, width, cv_format=''):
        yuvdata = np.fromfile(filename, dtype=np.uint8)
        cvt_format = YUV_FORMAT_MAP.get(cv_format)
        if cvt_format is None:
            return False, 'YUV格式不支持'
        self.imgpath = filename
        self.img = cv2.cvtColor(yuvdata.reshape(
            (height*3//2, width)), cvt_format)
        self.__update_attr()
        return True

    # display
    def display_in_scene(self, scene):
        """
        return: true or error string
        """
        scene.clear()
        if self.img is not None:
            # numpy转qimage的标准流程
            if len(self.img.shape) == 2:
                bytes_per_line = self.img.shape[1]
                qimg = QImage(
                    self.img, self.img.shape[1], self.img.shape[0], bytes_per_line, QImage.Format_Grayscale8)
            elif self.img.shape[2] == 3:
                bytes_per_line = 3 * self.img.shape[1]
                qimg = QImage(
                    self.img, self.img.shape[1], self.img.shape[0], bytes_per_line, QImage.Format_BGR888)
            elif self.img.shape[2] == 4:
                bytes_per_line = 4 * self.img.shape[1]
                qimg = QImage(
                    self.img, self.img.shape[1], self.img.shape[0], bytes_per_line, QImage.Format_RGBA8888)
            else:
                return "图片格式不能解析"
            scene.addPixmap(QPixmap.fromImage(qimg))
            return True
        return '图片为空'

    # proc
    def save_image(self, filename):
        # 解决中文路径的问题, 不使用imwrite
        cv2.imencode('.jpg', self.img)[1].tofile(filename)

    def get_img_point(self, x, y):
        """
        获取图像中一个点的RGB值，注意颜色顺序是BGR
        """
        if(x > 0 and x < self.width and y > 0 and y < self.height):
            return self.img[y, x]
        else:
            return None
