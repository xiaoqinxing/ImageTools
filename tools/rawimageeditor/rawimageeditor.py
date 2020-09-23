import cv2
from PySide2.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene, QMessageBox, QFileDialog, QDialog
from PySide2.QtGui import QPixmap, Qt
from PySide2.QtCore import Slot
from tools.rawimageeditor.rawimageeditor_window import Ui_ImageEditor
from ui.customwidget import ImageView, MatplotlibWidget
from tools.rawimageeditor.rawImage import RawImageInfo, RawImageParams
from tools.rawimageeditor.rawhistgramview import Ui_HistgramView
import numpy as np


class RawImageEditor(object):
    pipeline_dict = {
        "black level":  0,
        "rolloff":      1,
        "ABF":          2,
        "demosaic":     3,
        "awb":          4,
        "ccm":          5,
        "gamma":        6,
        "LTM":          7,
        "advanced chroma enhancement":  8,
        "wavelet denoise":              9,
        "adaptive spatial filter":      10
    }

    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_ImageEditor()
        self.ui.setupUi(self.window)
        self.scene = QGraphicsScene()
        self.imageview = ImageView(self.scene)
        # 由于graphicsView被自定义了，需要重新定义一下UI，gridlayout还需要重新加一下widget
        self.ui.graphicsView.addWidget(self.imageview, 0, 1, 3, 1)
        self.imageview.sigDragEvent.connect(self.__init_img)
        self.imageview.sigMouseMovePoint.connect(self.show_point_rgb)
        self.imageview.sigWheelEvent.connect(self.update_wheel_ratio)
        self.ui.width.editingFinished.connect(self.update_width)
        self.ui.height.editingFinished.connect(self.update_height)
        self.ui.bit.editingFinished.connect(self.update_bit_depth)
        self.ui.raw_format.currentTextChanged.connect(self.update_raw_format)
        self.ui.pattern.currentTextChanged.connect(self.update_pattern)
        self.ui.pipeline.doubleClicked.connect(self.update_img_index)
        self.ui.pipeline_ok.clicked.connect(self.update_pipeline)
        self.ui.open_image.clicked.connect(self.open_image)
        self.scale_ratio = 100
        self.img = RawImageInfo()
        self.img_params = RawImageParams()
        self.pipeline_list = []
        self.img_list = []
        self.img_list_start_index = 0
        self.img_list_end_index = 0
        self.img_index = 0

    def show(self):
        self.window.show()

    def update_width(self):
        self.img_params.set_width(self.ui.width.value())
        print(self.img_params.get_width())

    def update_height(self):
        self.img_params.set_height(self.ui.height.value())
        print(self.img_params.get_height())

    def update_bit_depth(self):
        self.img_params.set_bit_depth(self.ui.bit.value())
        print(self.img_params.get_bit_depth())

    def update_raw_format(self):
        self.img_params.set_raw_format(self.ui.raw_format.currentText())
        print(self.img_params.get_raw_format())

    def update_pattern(self):
        self.img_params.set_pattern(self.ui.pattern.currentText().lower())
        print(self.img_params.get_pattern())

    def displayImage(self, img):
        self.scene.clear()
        self.scene.addPixmap(QPixmap(img))
        self.now_image = img

    def update_pipeline(self, item):
        new_pipeline_list = []
        for i in range(self.ui.pipeline.count()):
            if (self.ui.pipeline.item(i).checkState() == Qt.Checked):
                new_pipeline_list.append(
                    self.pipeline_dict[self.ui.pipeline.item(i).data(0)])
        self.img_params.set_pipeline(new_pipeline_list)
        print(self.img_params.get_pipeline())

    def update_img_index(self, item):
        if (self.ui.pipeline.item(item.row()).checkState() == Qt.Checked):
            self.img_params.img_show_index = self.img_params.get_pipeline().index(
                self.pipeline_dict[item.data()])
            print(self.img_params.img_show_index)

    def open_image(self):
        imagepath = QFileDialog.getOpenFileName(
            None, '打开RAW图', './', "raw (*.raw)")
        self.__init_img(imagepath[0])

    def __init_img(self, filename):
        width = self.img_params.get_width()
        height = self.img_params.get_height()
        bit_depth = self.img_params.get_bit_depth()
        if (filename != "" and width != 0 and height != 0 and bit_depth != 0):
            self.img.load_image(filename, height, width, bit_depth)
            self.img.set_bayer_pattern(self.img_params.get_pattern())
            if (self.img.get_raw_data() is not None):
                self.displayImage(self.img.get_qimage())
            else:
                rely = QMessageBox.critical(
                    self.window, '警告', '打开图片失败,', QMessageBox.Yes, QMessageBox.Yes)
                return rely

    def save_now_image(self):
        if(self.img.get_raw_data() is not None):
            imagepath = QFileDialog.getSaveFileName(
                None, '保存图片', './', "Images (*.jpg)")
            if(imagepath[0] != ""):
                self.img.save_image(self.now_image, imagepath[0])

    # def compare_image(self):
    #     if(self.img.get_raw_data() is not None):
    #         if(self.now_image == self.img.get_dst_image()):
    #             self.displayImage(self.img.get_src_image())
    #         else:
    #             self.displayImage(self.img.get_dst_image())

    def update_stats_range(self, viewportRect, fromScenePoint, toScenePoint):
        if(toScenePoint.x() == 0 and toScenePoint.y() == 0
           and self.rect[2] > self.rect[0] and self.rect[3] > self.rect[1]):
            (self.r_hist, self.g_hist, self.b_hist,
             self.y_hist) = self.img.calcHist(self.now_image, self.rect)
            self.hist_show()
            msg = self.img.calcStatics(self.now_image, self.rect)
            self.stats_show(msg)
        else:
            self.rect = [int(fromScenePoint.x()), int(fromScenePoint.y()), int(
                toScenePoint.x()), int(toScenePoint.y())]
        return

    def show_point_rgb(self, point):
        self.x = int(point.x())
        self.y = int(point.y())
        if(self.img.get_raw_data() is not None):
            rgb = self.img.get_img_point(self.x, self.y)
            if (rgb is not None):
                self.rgb = rgb
                self.ui.statusBar.showMessage(
                    "x:{},y:{} : R:{} G:{} B:{} 缩放比例:{}%".format(self.x, self.y, self.rgb[0], self.rgb[1], self.rgb[2], self.scale_ratio))

    def update_wheel_ratio(self, ratio):
        if(self.img.get_raw_data() is not None):
            self.scale_ratio = int(ratio * 100)
            self.ui.statusBar.showMessage(
                "x:{},y:{} : R:{} G:{} B:{} 缩放比例:{}%".format(self.x, self.y, self.rgb[0], self.rgb[1], self.rgb[2], self.scale_ratio))

    def on_calc_stats(self):
        if(self.img.get_raw_data() is not None):
            self.rect = [0, 0, self.img.width, self.img.height]
            (self.r_hist, self.g_hist, self.b_hist,
                self.y_hist) = self.img.calcHist(self.now_image, self.rect)
            self.hist_window = HistViewDrag(self.imageview)
            self.hist_view_ui = Ui_HistgramView()
            self.hist_view_ui.setupUi(self.hist_window)
            self.hist_view_ui.r_enable.stateChanged.connect(
                self.on_r_hist_enable)
            self.hist_view_ui.g_enable.stateChanged.connect(
                self.on_g_hist_enable)
            self.hist_view_ui.b_enable.stateChanged.connect(
                self.on_b_hist_enable)
            self.hist_view_ui.y_enable.stateChanged.connect(
                self.on_y_hist_enable)
            self.histview = MatplotlibWidget(
                self.hist_view_ui.gridLayout_10)
            self.hist_window.show()
            self.x_axis = np.linspace(0, 255, num=256)
            self.r_hist_visible = 2
            self.g_hist_visible = 2
            self.b_hist_visible = 2
            self.y_hist_visible = 2
            self.hist_show()
            msg = self.img.calcStatics(self.now_image, self.rect)
            self.stats_show(msg)

    def on_r_hist_enable(self, type):
        self.r_hist_visible = type
        self.hist_show()

    def on_g_hist_enable(self, type):
        self.g_hist_visible = type
        self.hist_show()

    def on_b_hist_enable(self, type):
        self.b_hist_visible = type
        self.hist_show()

    def on_y_hist_enable(self, type):
        self.y_hist_visible = type
        self.hist_show()

    def hist_show(self):
        self.histview.clean()
        self.histview.label("亮度", "数量")
        if (self.r_hist_visible == 2):
            self.histview.input_r_hist(self.x_axis, self.r_hist)
        if (self.g_hist_visible == 2):
            self.histview.input_g_hist(self.x_axis, self.g_hist)
        if (self.b_hist_visible == 2):
            self.histview.input_b_hist(self.x_axis, self.b_hist)
        if (self.y_hist_visible == 2):
            self.histview.input_y_hist(self.x_axis, self.y_hist)
        self.histview.draw()

    def stats_show(self, value):
        (average_rgb, snr_rgb, average_yuv, snr_yuv,
         rgb_ratio, awb_gain, enable_rect) = value
        self.hist_view_ui.average_r.setValue(average_rgb[2])
        self.hist_view_ui.average_g.setValue(average_rgb[1])
        self.hist_view_ui.average_b.setValue(average_rgb[0])
        self.hist_view_ui.average_y.setValue(average_yuv[0])
        self.hist_view_ui.average_cr.setValue(average_yuv[1])
        self.hist_view_ui.average_cb.setValue(average_yuv[2])
        self.hist_view_ui.rg_ratio.setValue(rgb_ratio[0])
        self.hist_view_ui.bg_ratio.setValue(rgb_ratio[1])
        self.hist_view_ui.r_gain.setValue(awb_gain[0])
        self.hist_view_ui.g_gain.setValue(awb_gain[1])
        self.hist_view_ui.b_gain.setValue(awb_gain[2])
        self.hist_view_ui.section_x.setValue(enable_rect[0])
        self.hist_view_ui.section_y.setValue(enable_rect[1])
        self.hist_view_ui.section_height.setValue(enable_rect[2])
        self.hist_view_ui.section_width.setValue(enable_rect[3])
        self.hist_view_ui.snr_r.setValue(snr_rgb[2])
        self.hist_view_ui.snr_g.setValue(snr_rgb[1])
        self.hist_view_ui.snr_b.setValue(snr_rgb[0])
        self.hist_view_ui.snr_y.setValue(snr_yuv[0])
        self.hist_view_ui.snr_cr.setValue(snr_yuv[1])
        self.hist_view_ui.snr_cb.setValue(snr_yuv[2])


class HistViewDrag(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.parent.setDragMode(QGraphicsView.RubberBandDrag)

    def closeEvent(self, event):
        self.parent.setDragMode(QGraphicsView.ScrollHandDrag)
        return super().closeEvent(event)
