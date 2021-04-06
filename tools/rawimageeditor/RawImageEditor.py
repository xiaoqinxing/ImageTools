from PySide2.QtWidgets import QGraphicsView, QGraphicsScene, QMessageBox, QFileDialog
from PySide2.QtGui import QPixmap, Qt, QImage
from components.customwidget import ImageView, critical
from components.window import SubWindow
from tools.rawimageeditor.ui.rawimageeditor_window import Ui_ImageEditor
from tools.rawimageeditor.RawImageParams import RawImageParams
from tools.rawimageeditor.RawImageInfo import RawImageInfo
from tools.rawimageeditor.isppipeline import IspPipeline
from components.histview import HistView
import numpy as np
import os


class RawImageEditor(SubWindow):
    def __init__(self, name='RawImageEditor', parent=None):
        super().__init__(name, parent, Ui_ImageEditor(), need_processBar=True)

        self.scene = QGraphicsScene()
        self.imageview = ImageView(self.scene, parent)
        self.img_params = RawImageParams()
        self.img_params = self.load_params(RawImageParams())
        self.img_pipeline = IspPipeline(
            self.img_params, process_bar=self.progress_bar)
        self.img = RawImageInfo()
        self.point_data = np.array([0])
        self.scale_ratio = 100
        self.histShow = None
        self.show_img = None
        self.select_awb = False

        # 由于graphicsView被自定义了，需要重新定义一下UI，gridlayout还需要重新加一下widget
        self.ui.graphicsView.addWidget(self.imageview, 0, 1, 3, 1)
        self.imageview.sigDragEvent.connect(self.__init_img)
        self.imageview.sigMouseMovePoint.connect(self.show_point_rgb)
        self.imageview.sigWheelEvent.connect(self.update_wheel_ratio)
        # 回调函数初始化
        self.ui.pipeline.doubleClicked.connect(self.update_img_index)
        self.ui.pipeline_ok.clicked.connect(self.update_pipeline)
        self.ui.open_image.clicked.connect(self.open_image)
        self.ui.analysis_img.clicked.connect(self.openHistView)
        self.ui.select_from_raw.clicked.connect(self.select_awb_from_raw)
        self.imageview.rubberBandChanged.connect(self.update_awb_from_raw)
        self.ui.save_image.clicked.connect(self.save_now_image)
        self.ui.reload.clicked.connect(self.img_pipeline.reload_isp)
        self.ui.inputflatphoto.clicked.connect(self.img_params.rolloff.set_flatphoto)
        # ISP 处理线程回调
        self.img_pipeline.ispProcthread.doneCB.connect(self.update_img)
        self.img_pipeline.ispProcthread.processRateCB.connect(
            self.update_process_bar)
        self.img_pipeline.ispProcthread.costTimeCB.connect(
            self.update_time_bar)
        self.img_pipeline.ispProcthread.errorCB.connect(self.error_report)
    
    def error_report(self, value):
        """
        func: 报告ISP算法错误
        """
        critical(value, self)

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
        self.ui.filename.repaint()
        if (self.img_params.rawformat.filename != ""):
            self.update_pipeline()
            self.img = self.img_pipeline.get_image(-1)
            self.displayImage(self.img)
            self.rect = [0, 0, self.img_params.rawformat.width, self.img_params.rawformat.height]

    def displayImage(self, img):
        """
        显示图像 输入需要是RawImageInfo
        """
        self.scene.clear()
        self.img = img
        self.show_img = img.get_showimage()
        if(self.show_img is not None):
            showimg = QImage(self.show_img, self.show_img.shape[1],
                          self.show_img.shape[0], QImage.Format_BGR888)
            self.scene.addPixmap(QPixmap(showimg))
            self.ui.photo_title.setTitle(img.get_name())

    def select_awb_from_raw(self):
        """
        func: 进入raw图选择模式，修改鼠标类型
        """
        self.imageview.setDragMode(QGraphicsView.RubberBandDrag)
        self.select_awb = True

    def update_awb_from_raw(self, viewportRect, fromScenePoint, toScenePoint):
        """
        func: 鼠标选中事件的回调：执行AWB的选择区域或者图像分析的选择区域
        """
        if(toScenePoint.x() == 0 and toScenePoint.y() == 0
                and self.rect[2] > self.rect[0] and self.rect[3] > self.rect[1]):
            if(self.select_awb == True):
                self.imageview.setDragMode(QGraphicsView.ScrollHandDrag)
                self.select_awb = False
                awb_ratio = self.img.get_raw_img_rect(self.rect)
                if(awb_ratio is not None):
                    self.img_params.awb.set_awb_ratio(awb_ratio)
                    awb_gain = self.img_params.awb.get_awb_gain()
                    self.ui.awb_r.setValue(awb_gain[0])
                    self.ui.awb_g.setValue(awb_gain[1])
                    self.ui.awb_b.setValue(awb_gain[2])
                else:
                    critical("请在raw图上进行选择")
            else:
                if(self.histView is not None):
                    self.histView.update_rect_data(self.show_img, self.rect)
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
        if (self.img_params.rawformat.filename != ''):
            now_path = os.path.dirname(self.img_params.rawformat.filename)
        else:
            now_path = './'
        imagepath = QFileDialog.getOpenFileName(
            None, '打开RAW图', now_path, "raw (*.raw)")
        self.__init_img(imagepath[0])

    def __init_img(self, filename):
        if(filename != ''):
            self.ui.filename.setText(filename)
            self.ui.filename.repaint()
            self.update_pipeline()
            self.img = self.img_pipeline.get_image(-1)
            self.rect = [0, 0, self.img_params.rawformat.width, self.img_params.rawformat.height]

    def save_now_image(self):
        """
        func: 保存图片的回调
        """
        if(self.img.get_raw_data() is not None):
            imagepath = QFileDialog.getSaveFileName(
                None, '保存图片', './', "Images (*.jpg)")
            if(imagepath[0] != ""):
                self.img.save_image(imagepath[0])

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
            if(self.img.get_color_space() == 'RGB'):
                self.info_bar.setText(
                    "x:{},y:{} : R:{} G:{} B:{} 缩放比例:{}%".format(self.x, self.y, self.point_data[2], self.point_data[1], self.point_data[0], self.scale_ratio))
            else:
                self.info_bar.setText(
                    "x:{},y:{} : Y:{} Cr:{} Cb:{} 缩放比例:{}%".format(self.x, self.y, self.point_data[0], self.point_data[1], self.point_data[2], self.scale_ratio))
    
    def openHistView(self):
        self.histView = HistView(self.imageview)
        rect = [0, 0, self.show_img.shape[1], self.show_img.shape[0]]
        self.histView.update_rect_data(self.show_img, rect)
        self.histView.show()