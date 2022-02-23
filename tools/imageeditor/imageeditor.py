from PySide2.QtWidgets import QGraphicsScene, QFileDialog, QDialog
from components.customwidget import ImageView, sceneDisplayImage, critical
from components.window import SubWindow
from components.histview import HistView
from os import listdir, remove
from os.path import isfile, join, getmtime, dirname, basename
from .ui.imageeditor_window import Ui_ImageEditor
from .imageeffect import ImageEffect, BlurType, WaterMarkParams
from .ui.watermarkview import Ui_WaterMarkView


class ImageEditor(SubWindow):
    def __init__(self, name='ImageEditor', parent=None):
        super().__init__(name, parent, Ui_ImageEditor())
        self.scene = QGraphicsScene()
        self.imageview = ImageView(self.scene, parent)
        # 由于graphicsView被自定义了，需要重新定义一下UI，gridlayout还需要重新加一下widget
        self.ui.gridLayout.addWidget(self.imageview, 0, 1, 3, 1)
        self.imageview.sigDragEvent.connect(self.__init_img)
        self.imageview.sigMouseMovePoint.connect(self.show_point_rgb)
        self.imageview.sigWheelEvent.connect(self.update_wheel_ratio)
        self.ui.openimage.triggered.connect(self.on_open_img)
        self.ui.saveimage.triggered.connect(self.save_now_image)
        self.ui.compareimage.triggered.connect(self.compare_image)
        self.ui.boxblur.triggered.connect(self.boxblur_image)
        self.ui.guassian.triggered.connect(self.guassian_image)
        self.ui.medianblur.triggered.connect(self.medianblur_image)
        self.ui.bilateralblur.triggered.connect(self.bilateralblur_image)
        # self.ui.historgram.triggered.connect(self.on_calc_hist)
        self.ui.actionstats.triggered.connect(self.on_calc_stats)
        self.ui.nextphoto.triggered.connect(self.switch_next_photo)
        self.ui.prephoto.triggered.connect(self.switch_pre_photo)
        self.imageview.rubberBandChanged.connect(self.update_stats_range)
        self.ui.watermark.triggered.connect(self.open_watermark_win)
        self.ui.deletephoto.triggered.connect(self.delete_photo)
        self.scale_ratio = 100
        self.img = ImageEffect()
        self.filepath = './'
        self.imgfilename = ''
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
        pre_photo, index, files_nums = self.find_next_photo(self.filepath, -1)
        indexstr = "({}/{})".format(index + 1, files_nums)
        self.__init_img(pre_photo, indexstr)

    def on_open_img(self):
        imagepath = QFileDialog.getOpenFileName(
            None, '打开图片', self.filepath, "Images (*.jpg *.png *.bmp)")
        self.__init_img(imagepath[0])

    def __init_img(self, filename, indexstr=''):
        if (filename != ''):
            self.img.load_image(filename)
            self.filepath = dirname(filename)
            self.imgfilename = basename(filename)
            self.img.imageconvert(0)
            if (self.img.nowImage is not None):
                self.displayImage(self.img.nowImage)
                self.ui.photo_title.setTitle(indexstr + self.imgfilename)
            else:
                critical('打开图片失败')
                return

    def open_watermark_win(self):
        if(self.img.is_load_image == True):
            self.watermark_win = QDialog(self.imageview)
            self.watermark_ui = Ui_WaterMarkView()
            self.watermark_ui.setupUi(self.watermark_win)
            self.watermark_win.show()
            self.watermark_ui.open_watermark.clicked.connect(
                self.open_watermark_path)
            self.watermark_ui.change_transparent.valueChanged.connect(
                self.set_watermark_params)
            self.watermark_ui.change_watermark_size.valueChanged.connect(
                self.set_watermark_params)
            self.watermark_ui.change_watermark_th.valueChanged.connect(
                self.set_watermark_params)
            self.watermark_ui.change_watermark_type.currentIndexChanged.connect(
                self.set_watermark_params)
            self.watermark_ui.generate.clicked.connect(self.generate_watermark)
            self.watermark_ui.analysis.clicked.connect(
                self.analysis_space_watermark)
        else:
            critical('打开原图片失败，请先导入图片')

    def open_watermark_path(self):
        watermarkpath = QFileDialog.getOpenFileName(
            None, '打开图片', './', "Images (*.jpg *.png *.bmp)")
        self.watermark_path = watermarkpath[0]
        if (self.watermark_path != ''):
            self.watermark_ui.watermark_path.setText(self.watermark_path)
            self.img.set_watermark_img(self.watermark_path)
            self.set_watermark_params()
        else:
            critical('打开水印图片失败')

    def get_watermark_parmas(self):
        watermark_params = WaterMarkParams()
        watermark_params.transparent = self.watermark_ui.change_transparent.value()
        watermark_params.size = self.watermark_ui.change_watermark_size.value()
        watermark_params.threshold = self.watermark_ui.change_watermark_th.value()
        watermark_params.watermark_type = self.watermark_ui.change_watermark_type.currentIndex()
        return watermark_params

    def set_watermark_params(self):
        self.img.set_watermark_show(self.get_watermark_parmas())
        self.img.imageconvert(1)
        self.displayImage(self.img.dstImage)

    def generate_watermark(self):
        self.img.imageconvert(1)
        self.img.generate_watermark(self.get_watermark_parmas())
        self.displayImage(self.img.dstImage)

    def analysis_space_watermark(self):
        self.img.analysis_space_watermark()
        self.img.imageconvert(1)
        self.displayImage(self.img.dstImage)

    def boxblur_image(self):
        if(self.img.is_load_image == True):
            self.img.blur(BlurType.BoxBlur)
            self.img.imageconvert(1)
            self.displayImage(self.img.nowImage)

    def guassian_image(self):
        if(self.img.is_load_image == True):
            self.img.blur(BlurType.GaussianBlur)
            self.img.imageconvert(1)
            self.displayImage(self.img.nowImage)

    def medianblur_image(self):
        if(self.img.is_load_image == True):
            self.img.blur(BlurType.MediaBlur)
            self.img.imageconvert(1)
            self.displayImage(self.img.nowImage)

    def bilateralblur_image(self):
        if(self.img.is_load_image == True):
            self.img.blur(BlurType.BilateralBlur)
            self.img.imageconvert(1)
            self.displayImage(self.img.nowImage)

    def save_now_image(self):
        if(self.img.is_load_image == True):
            imagepath = QFileDialog.getSaveFileName(
                None, '保存图片', './', "Images (*.jpg)")
            if(imagepath[0] != ''):
                self.img.save_image(self.img.nowImage, imagepath[0])

    def compare_image(self):
        if(self.img.is_load_image == True):
            if(self.img.get_img_index() == 0):
                self.img.imageconvert(1)
            else:
                self.img.imageconvert(0)
            self.displayImage(self.img.nowImage)

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
