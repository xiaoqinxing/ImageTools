from PySide2.QtWidgets import QGraphicsScene, QFileDialog, QDialog
from isort import file
from components.customwidget import ImageView, sceneDisplayImage, critical
from components.window import SubWindow
from components.histview import HistView
from os import listdir, remove
from os.path import isfile, join, getmtime, dirname, basename
from .ui.yuvviewer_window import Ui_YUVEditor
from components.BasicImage import ImageBasic


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
        # self.ui.historgram.triggered.connect(self.on_calc_hist)
        self.ui.actionstats.triggered.connect(self.on_calc_stats)
        self.ui.nextphoto.triggered.connect(self.switch_next_photo)
        self.ui.prephoto.triggered.connect(self.switch_pre_photo)
        self.imageview.rubberBandChanged.connect(self.update_stats_range)
        self.ui.deletephoto.triggered.connect(self.delete_photo)
        self.img = ImageBasic()
        self.scale_ratio = 100
        # self.img = ImageEffect()
        self.hist_window = None

    def displayImage(self, img):
        if sceneDisplayImage(self.scene, img) is True:
            if(self.hist_window is not None and self.hist_window.enable is True):
                self.hist_window.update_rect_data(self.img.nowImage, self.rect)

    def delete_photo(self):
        current_photo = join(self.filepath, self.imgfilename)
        next_photo, index, files_nums = self.find_next_photo(self.filepath, 1)
        indexstr = "({}/{})".format(index, files_nums - 1)
        self.__init_img(next_photo, indexstr)
        remove(current_photo)

    def find_next_photo(self, path, nextIndex):
        ret = ''
        index = 0
        filelist = [f for f in listdir(path) if isfile(
            join(path, f)) and f.split('.')[-1] in ["jpg", "png", "bmp"]]
        filelist = sorted(
            filelist,  key=lambda x: getmtime(join(path, x)))
        files_nums = len(filelist)
        if(self.imgfilename in filelist):
            index = filelist.index(self.imgfilename) + nextIndex
            if(index > len(filelist) - 1):
                index = 0
            elif(index < 0):
                index = len(filelist) - 1
            ret = join(path, filelist[index])
        return (ret, index, files_nums)

    def switch_next_photo(self):
        next_photo, index, files_nums = self.find_next_photo(self.filepath, 1)
        indexstr = "({}/{})".format(index + 1, files_nums)
        self.__init_img(next_photo, indexstr)

    def switch_pre_photo(self):
        pre_photo, index, files_nums = self.img.find_next_photo(-1)
        indexstr = "({}/{})".format(index + 1, files_nums)
        self.__init_img(pre_photo, indexstr)

    def on_open_img(self):
        imagepath = QFileDialog.getOpenFileName(
            None, '打开图片', self.filepath, "Images (*.jpg *.png *.bmp)")
        self.__init_img(imagepath[0])

    def __init_img(self, filename, indexstr=''):
        if filename != '':
            self.img.load_imagefile(filename)
            ret = self.img.display_in_scene(self.scene)
            if ret is not True:
                critical(ret)
                return
            self.ui.photo_title.setTitle(indexstr + self.img.imgpath)

    def update_stats_range(self, viewportRect, fromScenePoint, toScenePoint):
        if(toScenePoint.x() == 0 and toScenePoint.y() == 0
           and self.rect[2] > self.rect[0] and self.rect[3] > self.rect[1]):
            if(self.hist_window is not None):
                self.hist_window.update_rect_data(self.img.nowImage, self.rect)
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
        if(self.img.is_load_image == True):
            rgb = self.img.get_img_point(self.x, self.y)
            if (rgb is not None):
                self.rgb = rgb
                self.ui.statusBar.showMessage(
                    "x:{},y:{} : R:{} G:{} B:{} 缩放比例:{}%".format(self.x, self.y, self.rgb[2], self.rgb[1], self.rgb[0], self.scale_ratio))

    def update_wheel_ratio(self, ratio):
        """
        func: 鼠标滚轮的回调
        """
        if(self.img.is_load_image == True):
            self.scale_ratio = int(ratio * 100)
            self.ui.statusBar.showMessage(
                "x:{},y:{} : R:{} G:{} B:{} 缩放比例:{}%".format(self.x, self.y, self.rgb[2], self.rgb[1], self.rgb[0], self.scale_ratio))

    def on_calc_stats(self):
        if(self.img.is_load_image == True):
            self.hist_window = HistView(self.imageview)
            rect = [0, 0, self.img.nowImage.shape[1],
                    self.img.nowImage.shape[0]]
            self.hist_window.update_rect_data(self.img.nowImage, rect)
            self.hist_window.show()
