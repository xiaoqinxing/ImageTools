import cv2
from PySide2.QtWidgets import QGraphicsView, QGraphicsScene, QMessageBox, QFileDialog, QDialog
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Slot
from tools.imageeditor.imageeditor_window import Ui_ImageEditor
from ui.customwidget import ImageView, MatplotlibWidget, SubWindow, critical
from tools.imageeditor.imageeffect import ImageEffect, BlurType
from tools.imageeditor.histgramview import Ui_HistgramView
from tools.imageeditor.watermarkview import Ui_WaterMarkView
import numpy as np

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
        self.imageview.rubberBandChanged.connect(self.update_stats_range)
        self.ui.watermark.triggered.connect(self.open_watermark_win)
        self.scale_ratio = 100
        self.img = ImageEffect()

    def displayImage(self, img):
        self.scene.clear()
        self.scene.addPixmap(QPixmap(img))
        self.now_image = img

    def on_open_img(self):
        imagepath = QFileDialog.getOpenFileName(
            None, '打开图片', './', "Images (*.jpg *.png *.bmp)")
        self.__init_img(imagepath[0])

    def __init_img(self, filename):
        if (filename != ''):
            self.img.load_image(filename)
            if (self.img.get_src_image() is not None):
                self.displayImage(self.img.get_src_image())
            else:
                rely = QMessageBox.critical(
                    self, '警告', '打开图片失败,', QMessageBox.Yes, QMessageBox.Yes)
                return

    def open_watermark_win(self):
        if(self.img.is_load_image == True):
            self.watermark_win = QDialog(self.imageview)
            self.watermark_ui = Ui_WaterMarkView()
            self.watermark_ui.setupUi(self.watermark_win)
            self.watermark_win.show()
            self.watermark_ui.open_watermark.clicked.connect(self.open_watermark_path)
            self.overlap_weight = 0
            self.watermark_ui.change_transparent.valueChanged.connect(self.change_transparent_func)
            self.watermark_ui.change_watermark_size.valueChanged.connect(self.change_size_func)
        else:
            critical('打开原图片失败，请先导入图片')
    
    def open_watermark_path(self):
        watermarkpath = QFileDialog.getOpenFileName(
            None, '打开图片', './', "Images (*.jpg *.png *.bmp)")
        self.watermark_path = watermarkpath[0]
        if (self.watermark_path != ''):
            self.watermark_ui.watermark_path.setText(self.watermark_path)
            self.img.set_watermark_img(self.watermark_path)
            self.img.set_watermark_transparent(0)
            self.displayImage(self.img.get_dst_image())
        else:
            critical('打开水印图片失败')

    def change_transparent_func(self):
        transparent = self.watermark_ui.change_transparent.value()
        self.overlap_weight = transparent/100
        self.img.set_watermark_transparent(self.overlap_weight)
        self.displayImage(self.img.get_dst_image())
    
    def change_size_func(self):
        size = self.watermark_ui.change_watermark_size.value()
        self.img.set_watermark_size(size)
        self.img.set_watermark_transparent(self.overlap_weight)
        self.displayImage(self.img.get_dst_image())

    def boxblur_image(self):
        if(self.img.is_load_image == True):
            self.img.blur(BlurType.BoxBlur)
            self.displayImage(self.img.get_dst_image())

    def guassian_image(self):
        if(self.img.is_load_image == True):
            self.img.blur(BlurType.GaussianBlur)
            self.displayImage(self.img.get_dst_image())

    def medianblur_image(self):
        if(self.img.is_load_image == True):
            self.img.blur(BlurType.MediaBlur)
            self.displayImage(self.img.get_dst_image())

    def bilateralblur_image(self):
        if(self.img.is_load_image == True):
            self.img.blur(BlurType.BilateralBlur)
            self.displayImage(self.img.get_dst_image())

    def save_now_image(self):
        if(self.img.is_load_image == True):
            imagepath = QFileDialog.getSaveFileName(
                None, '保存图片', './', "Images (*.jpg)")
            if(imagepath[0] != ''):
                self.img.save_image(self.now_image, imagepath[0])

    def compare_image(self):
        if(self.img.is_load_image == True):
            if(self.now_image == self.img.get_dst_image()):
                self.displayImage(self.img.get_src_image())
            else:
                self.displayImage(self.img.get_dst_image())

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
        if(self.img.is_load_image == True):
            rgb = self.img.get_img_point(self.x, self.y)
            if (rgb is not None):
                self.rgb = rgb
                self.ui.statusBar.showMessage(
                    "x:{},y:{} : R:{} G:{} B:{} 缩放比例:{}%".format(self.x, self.y, self.rgb[2], self.rgb[1], self.rgb[0], self.scale_ratio))

    def update_wheel_ratio(self, ratio):
        if(self.img.is_load_image == True):
            self.scale_ratio = int(ratio * 100)
            self.ui.statusBar.showMessage(
                "x:{},y:{} : R:{} G:{} B:{} 缩放比例:{}%".format(self.x, self.y, self.rgb[2], self.rgb[1], self.rgb[0], self.scale_ratio))

    def on_calc_stats(self):
        if(self.img.is_load_image == True):
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
