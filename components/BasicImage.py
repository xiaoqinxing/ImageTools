from posixpath import splitext
import cv2
import numpy as np
from PySide2.QtGui import QPixmap, QImage
from os import listdir, remove
from os.path import isfile, join, getmtime, dirname, basename, isdir
from natsort import natsorted
from components.status_code_enum import *

YUV_FORMAT_MAP = {
    'NV21': cv2.COLOR_YUV2BGR_NV21,
    'NV12': cv2.COLOR_YUV2BGR_NV12,
    'YCrCb': cv2.COLOR_YCrCb2BGR,
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
    yuv_format = ''

    def __update_attr(self):
        if (self.img is not None):
            self.height = self.img.shape[0]
            self.width = self.img.shape[1]
            self.depth = self.img.shape[2]

    def get_dir(self):
        if self.imgpath is None:
            return '.'
        return dirname(self.imgpath)

    def remove_image(self):
        if isfile(self.imgpath) is False:
            raise FileNotFoundErr
        remove(self.imgpath)
        self.img = None

    def load_yuv_config(self, width, height, yuv_format):
        self.width = width
        self.height = height
        self.yuv_format = yuv_format

    def load_file(self, filname):
        if splitext(filname)[-1] in ['.jpg', '.png', '.bmp']:
            self.__load_imagefile(filname)
        elif splitext(filname)[-1] in ['.yuv']:
            self.__load_yuvfile(filname)
        else:
            raise ImageFormatNotSupportErr

    def __load_imagefile(self, filename):
        if isfile(filename) is False:
            raise FileNotFoundErr
        # 防止有中文，因此不使用imread
        self.img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), 1)
        if self.img is None:
            raise ImageReadErr
        self.imgpath = filename
        self.__update_attr()

    def __load_yuvfile(self, filename):
        yuv_format = YUV_FORMAT_MAP.get(self.yuv_format)
        if yuv_format is None:
            raise ImageFormatNotSupportErr
        if isfile(filename) is False:
            raise FileNotFoundErr
        yuvdata = np.fromfile(filename, dtype=np.uint8)
        self.imgpath = filename
        self.img = cv2.cvtColor(yuvdata.reshape(
            (self.height*3//2, self.width)), self.yuv_format)
        self.__update_attr()

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
                raise ImageFormatNotSupportErr
            scene.addPixmap(QPixmap.fromImage(qimg))
            return
        raise ImageNoneErr

    # proc
    def save_image(self, filename):
        if self.img is None:
            raise ImageNoneErr
        if isdir(dirname(filename)) is False:
            raise FilePathNotValidErr
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

    def rotate90(self):
        """
        顺时针旋转90度
        """
        if self.img is None:
            raise ImageNoneErr
        self.img = cv2.rotate(self.img, cv2.ROTATE_90_CLOCKWISE)
        self.__update_attr()

    def find_next_time_photo(self, nextIndex):
        """
        获取下一个或者上一个图片(按照时间顺序排列)
        """
        next_photo_name = ''
        index = 0
        path = dirname(self.imgpath)
        img_name = basename(self.imgpath)
        filelist = [f for f in listdir(path) if isfile(
            join(path, f)) and f.split('.')[-1] in ["jpg", "png", "bmp"]]
        filelist = sorted(
            filelist,  key=lambda x: getmtime(join(path, x)))
        files_nums = len(filelist)
        if img_name in filelist:
            index = filelist.index(img_name) + nextIndex
            if(index > len(filelist) - 1):
                index = 0
            elif(index < 0):
                index = len(filelist) - 1
            next_photo_name = join(path, filelist[index])
        return (next_photo_name, index, files_nums)

    def find_next_nat_photo(self, nextIndex):
        """
        获取下一个或者上一个图片(按照自然顺序排列)
        """
        next_photo_name = ''
        index = 0
        path = dirname(self.imgpath)
        img_name = basename(self.imgpath)
        filelist = [f for f in listdir(path) if isfile(
            join(path, f)) and f.split('.')[-1] in ["jpg", "png", "bmp"]]
        natsorted(filelist)
        files_nums = len(filelist)
        if img_name in filelist:
            index = filelist.index(img_name) + nextIndex
            if(index > len(filelist) - 1):
                index = 0
            elif(index < 0):
                index = len(filelist) - 1
            next_photo_name = join(path, filelist[index])
        return (next_photo_name, index, files_nums)
