from distutils.command.config import config
from PySide2.QtWidgets import QGraphicsScene, QFileDialog, QDialog
from components.customwidget import ImageView, critical_win
from components.status_code_enum import *
from components.window import SubWindow
from components.histview import HistView
from os import remove
from .ui.yuvviewer_window import Ui_YUVEditor
from .ui.yuvconfig import Ui_YUVConfig
from components.BasicImage import ImageBasic
from logging import error
from traceback import format_exc


class YUVViewer(SubWindow):
    def __init__(self, name='YUVViewer', parent=None):
        super().__init__(name, parent, Ui_YUVEditor())
        self.scene = QGraphicsScene()
        self.imageview = ImageView(self.scene, parent)
        # 由于graphicsView被自定义了，需要重新定义一下UI，gridlayout还需要重新加一下widget
        self.ui.gridLayout.addWidget(self.imageview, 0, 1, 3, 1)
        self.imageview.sigDragEvent.connect(self.__init_img)
        self.imageview.sigMouseMovePoint.connect(self.show_point_rgb)
        self.imageview.sigWheelEvent.connect(self.update_wheel_ratio)
        self.ui.openimage.triggered.connect(self.on_open_img)
        self.ui.saveimage.triggered.connect(self.save_now_image)
        self.ui.actionstats.triggered.connect(self.on_calc_stats)
        self.ui.nextphoto.triggered.connect(self.switch_next_photo)
        self.ui.prephoto.triggered.connect(self.switch_pre_photo)
        self.imageview.rubberBandChanged.connect(self.update_stats_range)
        self.ui.deletephoto.triggered.connect(self.delete_photo)
        self.ui.rotateright.triggered.connect(self.rotate_photo)
        self.ui.yuvconfig.triggered.connect(self.on_config)
        self.img = ImageBasic()
        self.hist_window = None
        self.img_index_str = ''
        self.config_win = None
        self.x = 0
        self.y = 0

    def delete_photo(self):
        pre_imgpath = self.img.imgpath
        next_photo, index, files_nums = self.img.find_next_time_photo(1)
        self.img_index_str = "({}/{})".format(index, files_nums - 1)
        self.__init_img(next_photo, self.img_index_str)
        remove(pre_imgpath)

    def switch_next_photo(self):
        next_photo, index, files_nums = self.img.find_next_time_photo(1)
        self.img_index_str = "({}/{})".format(index + 1, files_nums)
        self.__init_img(next_photo, self.img_index_str)

    def switch_pre_photo(self):
        pre_photo, index, files_nums = self.img.find_next_time_photo(-1)
        self.img_index_str = "({}/{})".format(index + 1, files_nums)
        self.__init_img(pre_photo, self.img_index_str)

    def rotate_photo(self):
        try:
            self.img.rotate90()
            # TODO 是否需要加个配置项，是否旋转时保存图片
            self.__display_img(self.img_index_str)
            # self.img.save_image(self.img.imgpath)
        except Exception as e:
            error(format_exc())
            critical_win(str(e))

    def on_open_img(self):
        imagepath = QFileDialog.getOpenFileName(
            None, '打开图片', self.img.get_dir(), "Images (*.jpg *.png *.bmp)")
        self.__init_img(imagepath[0])

    def save_now_image(self):
        try:
            imagepath = QFileDialog.getSaveFileName(
                None, '保存图片', self.img.get_dir(), "Images (*.jpg)")
            self.img.save_image(imagepath[0])
        except Exception as e:
            error(format_exc())
            critical_win(str(e))

    def __init_img(self, filename, indexstr=''):
        try:
            self.img.load_file(filename)
            self.img.display_in_scene(self.scene)
            self.ui.photo_title.setTitle(indexstr + self.img.imgpath)
            if self.hist_window is not None and self.hist_window.enable is True:
                self.hist_window.update_rect_data(self.img.img, self.rect)
        except Exception as e:
            error(format_exc())
            critical_win(str(e))

    def __display_img(self, indexstr=''):
        try:
            self.img.display_in_scene(self.scene)
            self.ui.photo_title.setTitle(indexstr + self.img.imgpath)
            if self.hist_window is not None and self.hist_window.enable is True:
                self.hist_window.update_rect_data(self.img.img, self.rect)
        except Exception as e:
            error(format_exc())
            critical_win(str(e))

    def __show_point_stats(self):
        if self.img.img is not None:
            rgb = self.img.get_img_point(self.x, self.y)
            if (rgb is not None):
                scale_ratio = int(self.imageview.scale_ratio * 100)
                self.ui.statusBar.showMessage(
                    "x:{},y:{} : R:{} G:{} B:{} 缩放比例:{}%".format(self.x, self.y, rgb[2], rgb[1], rgb[0], scale_ratio))

    def update_stats_range(self, _, fromScenePoint, toScenePoint):
        if(toScenePoint.x() == 0 and toScenePoint.y() == 0
           and self.rect[2] > self.rect[0] and self.rect[3] > self.rect[1]):
            if self.hist_window is not None:
                self.hist_window.update_rect_data(self.img.img, self.rect)
        else:
            self.rect = [int(fromScenePoint.x()), int(fromScenePoint.y()), int(
                toScenePoint.x()), int(toScenePoint.y())]
        return

    def show_point_rgb(self, point):
        """
        func: 鼠标移动的回调
        """
        self.x = int(point.x())
        self.y = int(point.y())
        self.__show_point_stats()

    def update_wheel_ratio(self, _):
        """
        func: 鼠标滚轮的回调
        """
        self.__show_point_stats()

    def on_calc_stats(self):
        """
        打开统计信息的窗口
        """
        if self.img.img is not None:
            self.hist_window = HistView(self.imageview)
            self.rect = [0, 0, self.img.img.shape[1], self.img.img.shape[0]]
            self.hist_window.update_rect_data(self.img.img, self.rect)
            self.hist_window.show()

    def on_config(self):
        """
        打开配置的窗口
        """
        self.config_win = QDialog()
        config_win_ui = Ui_YUVConfig()
        config_win_ui.setupUi(self.config_win)
        self.config_win.show()
