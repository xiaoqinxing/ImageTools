import cv2
from PySide2.QtWidgets import QGraphicsView, QGraphicsScene, QMessageBox, QFileDialog, QDialog, QProgressBar, QLabel
from PySide2.QtGui import QPixmap, Qt
from PySide2.QtCore import Slot
from tools.rawimageeditor.rawimageeditor_window import Ui_ImageEditor
from ui.customwidget import ImageView, MatplotlibWidget, SubWindow
from tools.rawimageeditor.rawImage import RawImageInfo, RawImageParams
from tools.rawimageeditor.isppipeline import IspPipeline
from tools.rawimageeditor.rawhistgramview import Ui_HistgramView
import numpy as np


class RawImageEditor(SubWindow):
    def __init__(self, name, parent=None):
        super().__init__(name, parent, Ui_ImageEditor())

        # add 进度条和详细信息显示
        self.progress_bar = QProgressBar()
        self.info_bar = QLabel()
        self.ui.statusBar.addPermanentWidget(self.info_bar, stretch=4)
        self.ui.statusBar.addPermanentWidget(self.progress_bar, stretch=1)
        self.progress_bar.setRange(0, 100)  # 设置进度条的范围
        self.progress_bar.setValue(0)

        self.scene = QGraphicsScene()
        self.imageview = ImageView(self.scene, parent)
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
        self.ui.blc_r.editingFinished.connect(self.update_black_level)
        self.ui.blc_gr.editingFinished.connect(self.update_black_level)
        self.ui.blc_gb.editingFinished.connect(self.update_black_level)
        self.ui.blc_b.editingFinished.connect(self.update_black_level)
        self.ui.awb_r.editingFinished.connect(self.update_awb)
        self.ui.awb_g.editingFinished.connect(self.update_awb)
        self.ui.awb_b.editingFinished.connect(self.update_awb)
        self.ui.gamma_ratio.editingFinished.connect(self.update_gamma)
        self.scale_ratio = 100

        self.img_pipeline = IspPipeline()
        self.img = self.img_pipeline.get_image(0)
        self.img_index = 0
        self.point_data = 0

        self.img_params = self.load_params(self.img_pipeline.params)
        self.set_img_params()

    def set_img_params(self):
        self.ui.width.setValue(self.img_params.get_width())
        self.ui.height.setValue(self.img_params.get_height())
        self.ui.bit.setValue(self.img_params.get_bit_depth())
        # self.ui.pattern.setValue(self.img_params.get_pattern())

    def update_width(self):
        self.img_params.set_width(self.ui.width.value())

    def update_height(self):
        self.img_params.set_height(self.ui.height.value())

    def update_bit_depth(self):
        self.img_params.set_bit_depth(self.ui.bit.value())

    def update_raw_format(self):
        self.img_params.set_raw_format(self.ui.raw_format.currentText())

    def update_pattern(self):
        self.img_params.set_pattern(self.ui.pattern.currentText().lower())

    def displayImage(self, img):
        """
        显示图像 输入需要是RawImageInfo
        """
        self.scene.clear()
        self.img = img
        self.scene.addPixmap(QPixmap(img.get_qimage()))
        self.ui.photo_title.setTitle(img.get_name())

    def update_black_level(self):
        self.img_params.set_black_level([self.ui.blc_r.value(
        ), self.ui.blc_gr.value(), self.ui.blc_gb.value(), self.ui.blc_b.value()])
        self.img_pipeline.flush_pipeline()

    def update_awb(self):
        self.img_params.set_awb_gain(
            (self.ui.awb_r.value(), self.ui.awb_g.value(), self.ui.awb_b.value()))
        self.img_pipeline.flush_pipeline()

    def update_gamma(self):
        self.img_params.set_gamma(self.ui.gamma_ratio.value())
        self.img_pipeline.flush_pipeline()

    def update_pipeline(self):
        self.img_pipeline.pipeline_clear()
        for i in range(self.ui.pipeline.count()):
            if (self.ui.pipeline.item(i).checkState() == Qt.Checked):
                self.img_pipeline.add_pipeline_node(
                    self.ui.pipeline.item(i).data(0))
        self.img_pipeline.run_pipeline(self.progress_bar)
        self.displayImage(self.img_pipeline.get_image(0))
        print(self.img_pipeline.get_pipeline())
        print(self.img_pipeline.compare_pipeline())

    def update_img_index(self, item):
        if (self.ui.pipeline.item(item.row()).checkState() == Qt.Checked):
            index = self.img_pipeline.get_pipeline_node_index(item.data())+1
            self.displayImage(self.img_pipeline.get_image(index))

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
                self.displayImage(self.img)
            else:
                rely = QMessageBox.critical(
                    self, '警告', '打开图片失败,图片格式错误', QMessageBox.Yes, QMessageBox.Yes)
                return
        else:
            rely = QMessageBox.critical(
                self, '警告', '打开图片失败,图片格式错误', QMessageBox.Yes, QMessageBox.Yes)
            return

    def save_now_image(self):
        if(self.img.get_raw_data() is not None):
            imagepath = QFileDialog.getSaveFileName(
                None, '保存图片', './', "Images (*.jpg)")
            if(imagepath[0] != ""):
                self.img.save_image(self.now_image, imagepath[0])

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
            point_data = self.img.get_img_point(self.x, self.y)
            if (point_data is not None):
                self.point_data = point_data
                self.set_img_info_show()

    def update_wheel_ratio(self, ratio):
        if(self.img.get_raw_data() is not None):
            self.scale_ratio = int(ratio * 100)
            self.set_img_info_show()

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

    def set_img_info_show(self):
        if(self.point_data.size == 1):
            self.info_bar.setText(
                "x:{},y:{} : 亮度:{} 缩放比例:{}%".format(self.x, self.y, self.point_data, self.scale_ratio))
        elif(self.point_data.size == 3):
            self.info_bar.setText(
                "x:{},y:{} : R:{} G:{} B:{} 缩放比例:{}%".format(self.x, self.y, self.point_data[2], self.point_data[1], self.point_data[0], self.scale_ratio))


class HistViewDrag(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.parent.setDragMode(QGraphicsView.RubberBandDrag)

    def closeEvent(self, event):
        self.parent.setDragMode(QGraphicsView.ScrollHandDrag)
        return super().closeEvent(event)
