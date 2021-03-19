import cv2
from PySide2.QtWidgets import QGraphicsView, QGraphicsScene, QMessageBox, QFileDialog, QDialog, QProgressBar, QLabel
from PySide2.QtGui import QPixmap, Qt
from PySide2.QtCore import Slot
from tools.rawimageeditor.rawimageeditor_window import Ui_ImageEditor
from ui.customwidget import ImageView, MatplotlibWidget, SubWindow, critical
from tools.rawimageeditor.rawImage import RawImageInfo, RawImageParams
from tools.rawimageeditor.isppipeline import IspPipeline
from tools.rawimageeditor.rawhistgramview import Ui_HistgramView
import numpy as np
import os


class RawImageEditor(SubWindow):
    def __init__(self, name='RawImageEditor', parent=None):
        super().__init__(name, parent, Ui_ImageEditor())

        # add 进度条和详细信息显示
        self.progress_bar = QProgressBar()
        self.info_bar = QLabel()
        self.time_bar = QLabel()
        self.ui.statusBar.addPermanentWidget(self.info_bar, stretch=8)
        self.ui.statusBar.addPermanentWidget(self.time_bar, stretch=1)
        self.ui.statusBar.addPermanentWidget(self.progress_bar, stretch=2)
        self.progress_bar.setRange(0, 100)  # 设置进度条的范围
        self.progress_bar.setValue(0)

        self.scene = QGraphicsScene()
        self.imageview = ImageView(self.scene, parent)
        self.img_params = RawImageParams()
        self.img_params = self.load_params(RawImageParams())
        self.img_pipeline = IspPipeline(
            self.img_params, process_bar=self.progress_bar)
        self.img = self.img_pipeline.get_image(0)
        self.point_data = 0
        self.scale_ratio = 100

        # 由于graphicsView被自定义了，需要重新定义一下UI，gridlayout还需要重新加一下widget
        self.ui.graphicsView.addWidget(self.imageview, 0, 1, 3, 1)
        self.imageview.sigDragEvent.connect(self.__init_img)
        self.imageview.sigMouseMovePoint.connect(self.show_point_rgb)
        self.imageview.sigWheelEvent.connect(self.update_wheel_ratio)
        # 回调函数初始化
        self.ui.pipeline.doubleClicked.connect(self.update_img_index)
        self.ui.pipeline_ok.clicked.connect(self.update_pipeline)
        self.ui.open_image.clicked.connect(self.open_image)
        self.ui.select_from_raw.clicked.connect(self.select_awb_from_raw)
        self.imageview.rubberBandChanged.connect(self.update_awb_from_raw)
        self.ui.save_image.clicked.connect(self.save_now_image)
        self.ui.reload.clicked.connect(self.img_pipeline.reload_isp)
        # ISP 处理线程回调
        self.img_pipeline.ispProcthread.doneCB.connect(self.update_img)
        self.img_pipeline.ispProcthread.processRateCB.connect(
            self.update_process_bar)
        self.img_pipeline.ispProcthread.costTimeCB.connect(
            self.update_time_bar)

    def update_img(self):
        """
        func: ISP 处理完成后的显示回调函数
        """
        self.displayImage(self.img_pipeline.get_image(-1))

    def update_process_bar(self, value):
        """
        func: ISP 处理进度回调
        """
        self.progress_bar.setValue(value)

    def update_time_bar(self, value):
        """
        func：ISP 处理时长回调
        """
        self.time_bar.setText(value)

    def show(self):
        """
        func: 显示初始化
        """
        super().show()
        self.img_params.set_img_params_ui(self.ui)
        if (self.img_params.filename != "" and self.img_params.get_width() != 0 
            and self.img_params.get_height() != 0 and self.img_params.get_bit_depth() != 0):
            if(self.img_pipeline.pipeline_reset() == True):
                self.img = self.img_pipeline.get_image(0)
                for i in range(1, self.ui.pipeline.count()):
                    self.ui.pipeline.item(i).setCheckState(Qt.Unchecked)
            self.img.load_image_with_params(self.img_params)
            self.img.set_bayer_pattern(self.img_params.get_pattern())
            self.rect = [0, 0, self.img_params.width, self.img_params.height]
            if (self.img.get_raw_data() is not None):
                self.displayImage(self.img)

    def displayImage(self, img):
        """
        显示图像 输入需要是RawImageInfo
        """
        self.scene.clear()
        self.img = img
        qimage = img.get_qimage()
        if(qimage is not None):
            self.scene.addPixmap(QPixmap(qimage))
            self.ui.photo_title.setTitle(img.get_name())

    def select_awb_from_raw(self):
        """
        func: 进入raw图选择模式，修改鼠标类型
        """
        self.imageview.setDragMode(QGraphicsView.RubberBandDrag)

    def update_awb_from_raw(self, viewportRect, fromScenePoint, toScenePoint):
        """
        func: 更新AWB参数
        """
        if(toScenePoint.x() == 0 and toScenePoint.y() == 0
                and self.rect[2] > self.rect[0] and self.rect[3] > self.rect[1]):
            self.imageview.setDragMode(QGraphicsView.ScrollHandDrag)
            awb_ratio = self.img.get_raw_img_rect(self.rect)
            if(awb_ratio is not None):
                self.img_params.set_awb_ratio(awb_ratio)
                awb_gain = self.img_params.get_awb_gain()
                self.ui.awb_r.setValue(awb_gain[0])
                self.ui.awb_g.setValue(awb_gain[1])
                self.ui.awb_b.setValue(awb_gain[2])
            else:
                critical("请在raw图上进行选择")
        else:
            self.rect = [int(fromScenePoint.x()), int(fromScenePoint.y()), int(
                toScenePoint.x()), int(toScenePoint.y())]

    def update_pipeline(self):
        """
        func: 运行ISP pipeline
        """
        self.img_params.get_img_params(self.ui)
        self.img_pipeline.pipeline_clear()
        for i in range(self.ui.pipeline.count()):
            if (self.ui.pipeline.item(i).checkState() == Qt.Checked):
                self.img_pipeline.add_pipeline_node(
                    self.ui.pipeline.item(i).data(0))
        self.img_pipeline.run_pipeline()
        print(self.img_pipeline.pipeline)

    def update_img_index(self, item):
        """
        func: 更新当前画面的序号
        """
        if (self.ui.pipeline.item(item.row()).checkState() == Qt.Checked):
            index = self.img_pipeline.get_pipeline_node_index(item.data())+1
            self.displayImage(self.img_pipeline.get_image(index))

    def open_image(self):
        """
        func: 打开图片的回调函数
        """
        if (self.img_params.filename != ''):
            now_path = os.path.dirname(self.img_params.filename)
        else:
            now_path = './'
        self.img_params.get_img_params(self.ui)
        imagepath = QFileDialog.getOpenFileName(
            None, '打开RAW图', now_path, "raw (*.raw)")
        self.__init_img(imagepath[0])

    def __init_img(self, filename):
        width = self.img_params.get_width()
        height = self.img_params.get_height()
        bit_depth = self.img_params.get_bit_depth()
        if (filename != "" and width != 0 and height != 0 and bit_depth != 0):
            if(self.img_pipeline.pipeline_reset() == True):
                self.img = self.img_pipeline.get_image(0)
                for i in range(1, self.ui.pipeline.count()):
                    self.ui.pipeline.item(i).setCheckState(Qt.Unchecked)
            self.img.load_image(filename, height, width, bit_depth)
            self.img.set_bayer_pattern(self.img_params.get_pattern())
            self.img_params.filename = filename
            self.rect = [0, 0, self.img_params.width, self.img_params.height]
            if (self.img.get_raw_data() is not None):
                self.displayImage(self.img)
            else:
                critical("打开图片失败,图片格式错误")
        else:
            critical("打开图片失败,图片格式错误")

    def save_now_image(self):
        """
        func: 保存图片的回调
        """
        if(self.img.get_raw_data() is not None):
            imagepath = QFileDialog.getSaveFileName(
                None, '保存图片', './', "Images (*.jpg)")
            if(imagepath[0] != ""):
                self.img.save_image(imagepath[0])

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
        """
        func: 鼠标移动的回调
        """
        self.x = int(point.x())
        self.y = int(point.y())
        if(self.img.get_raw_data() is not None):
            point_data = self.img.get_img_point(self.x, self.y)
            if (point_data is not None):
                self.point_data = point_data
                self.set_img_info_show()

    def update_wheel_ratio(self, ratio):
        """
        func: 鼠标滚轮的回调
        """
        if(self.img.get_raw_data() is not None):
            self.scale_ratio = int(ratio * 100)
            self.set_img_info_show()
    
    def set_img_info_show(self):
        """
        func: 显示像素点的值以及缩放比例
        """
        if(self.point_data.size == 1):
            self.info_bar.setText(
                "x:{},y:{} : {}: 亮度:{} 缩放比例:{}%".format(self.x, self.y, self.img.get_img_point_pattern(self.y, self.x).upper(), self.point_data, self.scale_ratio))
        elif(self.point_data.size == 3):
            self.info_bar.setText(
                "x:{},y:{} : R:{} G:{} B:{} 缩放比例:{}%".format(self.x, self.y, self.point_data[2], self.point_data[1], self.point_data[0], self.scale_ratio))

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