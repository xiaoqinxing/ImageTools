from PySide2.QtWidgets import QDialog, QWidget, QGraphicsScene, QFileDialog, QMessageBox
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QTimer
from ui.customwidget import ImageView
from tools.video_compare.video_pre_settings import Ui_video_pre_settings
from tools.video_compare.rtspconfigview import Ui_RtspConfigView
import os
import cv2

class VideoCompareView(object):
    def __init__(self, parent=None):
        self.widget = QWidget()
        self.setting_widget = Ui_video_pre_settings()
        self.setting_widget.setupUi(self.widget)
        self.scene = QGraphicsScene()
        self.imageview = ImageView(self.scene, self.widget)
        self.setting_widget.videoview.addWidget(self.imageview)
        parent.addWidget(self.widget)
        # init params
        self.video_valid = False
        self.process_speed = 33
        self.skip_frames = 0
        self.video_timer = QTimer()
        # init func
        self.setting_widget.openvideo.clicked.connect(self.open_video)
        self.setting_widget.open_rtsp.clicked.connect(self.open_rtsp)
        self.setting_widget.skipframe.valueChanged.connect(self.set_skip_frame)
        self.imageview.sigDragEvent.connect(self.open_video_path)
    
    def set_skip_frame(self, value):
        # self.skip_frames = self.setting_widget.skipframe.value()
        self.skip_frames = value
        self.vertify_video()
    
    def open_video(self):
        videopath = QFileDialog.getOpenFileName(
            None, '打开文件', './', 'video files(*.mp4)')
        if(videopath[0] != ''):
            self.open_video_path(videopath[0])

    def open_video_path(self, str):
        self.setting_widget.path.setText(str)
        self.vertify_video()
        # self.set_ui_enable(True)
    
    def open_rtsp(self):
        self.rtsp_config_window = QDialog()
        self.rtsp_config_ui = Ui_RtspConfigView()
        self.rtsp_config_ui.setupUi(self.rtsp_config_window)
        self.rtsp_config_window.show()
        self.rtsp_config_ui.buttonBox.clicked.connect(self.rtsp_config)
    
    def rtsp_config(self):
        username = self.rtsp_config_ui.username.text()
        password = self.rtsp_config_ui.password.text()
        ip = self.rtsp_config_ui.ip.text()
        port = self.rtsp_config_ui.port.text()
        # 移动设备需要通过adb映射端口
        if(self.rtsp_config_ui.isphoto.isChecked() == True):
            command = "forward tcp:" + port + ' ' + "tcp:" + port
            os.system("adb " + command)
            os.system("kdb " + command)
        rtsp_path = "rtsp://"+username+":"+password+"@"+ip+":"+port
        self.open_video_path(rtsp_path)

    def vertify_video(self):
        # 输出参数初始化
        self.frame_count = 0
        self.vidcap = cv2.VideoCapture(self.setting_widget.path.text())
        # 片头调过多少帧
        self.vidcap.set(cv2.CAP_PROP_POS_FRAMES, self.skip_frames)
        success, frame = self.vidcap.read()
        if success:
            height = frame.shape[0]
            width = frame.shape[1]
            self.display(frame)
            self.video_valid = True
        else:
            self.critical_window_show('视频打不开')
            self.video_valid = False
            return
    
    def display(self, img):
        self.scene.clear()
        self.scene.addPixmap(QPixmap(QImage(img, img.shape[1], img.shape[0], QImage.Format_BGR888)))

    def open_frame(self):
        success, frame = self.vidcap.read()
        if success:
            self.frame_count += 1
            self.display(frame)
        else:
            self.video_timer.stop()
    
    def process_video(self):
        if(self.video_valid == True):
            self.vertify_video()
            # 增加定时器，每100ms进行一帧的处理
            self.video_timer.start(self.process_speed)
            self.video_timer.timeout.connect(self.open_frame)

    def cancel_process_video(self):
        self.video_timer.stop()
    
    def critical_window_show(self, str):
        reply = QMessageBox.critical(
            self.widget, '警告', str,
            QMessageBox.Yes, QMessageBox.Yes)
        return
