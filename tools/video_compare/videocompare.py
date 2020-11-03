import cv2
from PySide2.QtWidgets import QFileDialog, QMessageBox, QDialog, QWidget
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QTimer
from tools.video_compare.shake_test_window import Ui_ShakeTestWindow
from tools.video_compare.rtspconfigview import Ui_RtspConfigView
from ui.customwidget import VideoView, SubWindow
from tools.video_compare.videoview import VideoCompareView
import numpy as np
import math
import os


class VideoCompare(object):
    def __init__(self):
        self.window = SubWindow("VideoCompare")
        self.ui = Ui_ShakeTestWindow()
        self.ui.setupUi(self.window)
        self.videoview = [VideoCompareView(self.ui.horizontalLayout)]
        self.videoview.append(VideoCompareView(self.ui.horizontalLayout))
        #self.videoview[0].setupCbFunc(self.open_video, self.open_rtsp, self.open_video_path)
        self.ui.actionstart.triggered.connect(self.start_video)
        self.ui.actionpause.triggered.connect(self.pause_video)
        self.ui.actionrestart.triggered.connect(self.restart_video)
        self.ui.actionadd.triggered.connect(self.add_video)
        self.ui.actionsubtract.triggered.connect(self.remove_video)
        self.ui.actionspeedup.triggered.connect(self.speed_up_video)
        self.ui.actionspeeddown.triggered.connect(self.speed_down_video)
        self.speed = 1.0
        self.ui.statusbar.showMessage("播放速度 {}".format(self.speed))

    def speed_down_video(self):
        if(self.speed < 3):
            self.speed += 0.1
            self.ui.statusbar.showMessage("播放速度 {:.2f}".format(1/self.speed))
            for video in self.videoview:
                video.set_speed(self.speed)
        else:
            return

    def speed_up_video(self):
        if(self.speed > 0.3):
            self.speed -= 0.1
            self.ui.statusbar.showMessage("播放速度 {:.2f}".format(1/self.speed))
            for video in self.videoview:
                video.set_speed(self.speed)
        else:
            return

    def add_video(self):
        self.videoview.append(VideoCompareView(self.ui.horizontalLayout))

    def remove_video(self):
        remove_widget = self.videoview.pop()
        # 必须要加这一句才能彻底移除！
        remove_widget.widget.setParent(None)
        self.ui.horizontalLayout.removeWidget(remove_widget.widget)

    def start_video(self):
        for video in self.videoview:
            video.start_video()

    def pause_video(self):
        for video in self.videoview:
            video.stop_video()

    def restart_video(self):
        for video in self.videoview:
            video.restart_video()

    def set_ui_enable(self, value):
        self.ui.set_roi_up.setEnabled(value)
        self.ui.set_roi_down.setEnabled(value)
        self.ui.direction_select.setEnabled(value)
        self.ui.skipframes.setEnabled(value)
        self.ui.remove_move_point_enable.setEnabled(value)
        self.ui.calc_inter_frams.setEnabled(value)

    def show(self):
        self.window.show()


class RtspConfigView(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def closeEvent(self, event):
        return super().closeEvent(event)
