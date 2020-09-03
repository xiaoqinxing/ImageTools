import cv2
from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QTimer
from ui.windows.shake_test_window import Ui_ShakeTestWindow
import numpy as np


class ShakeTestTool(object):
    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_ShakeTestWindow()
        self.ui.setupUi(self.window)
        self.ui.openvideo.clicked.connect(self.open_video)
        self.ui.isok.clicked.connect(self.process_video)
        self.ui.cancel_button.clicked.connect(self.cancel_process_video)
        self.video_timer = QTimer()

    def show(self):
        self.window.show()

    def open_video(self):
        videopath = QFileDialog.getOpenFileName(
            None, '打开文件', './', 'video files(*.mp4)')
        self.ui.videopath.setText(videopath[0])

    def process_video(self):
        self.vidcap = cv2.VideoCapture(self.ui.videopath.text())
        self.video_timer.start(100)
        self.video_timer.timeout.connect(self.open_frame)

    def open_frame(self):
        keypoints = list()
        success, frame = self.vidcap.read()
        if success:
            new_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            corners = cv2.goodFeaturesToTrack(new_gray, 100, 0.01, 30)
            if corners is not None and len(corners) > 0:
                for x, y in np.float32(corners).reshape(-1, 2):
                    keypoints.append((x, y))
            if keypoints is not None and len(keypoints) > 0:
                for x, y in keypoints:
                    cv2.circle(new_gray, (int(x + 200), y), 3, (255, 255, 0))

            # display
            image = QImage(
                new_gray.data, new_gray.shape[1], new_gray.shape[0], QImage.Format_Indexed8)
            temp_pixmap = QPixmap.fromImage(image)
            self.ui.videoview.setPixmap(temp_pixmap)
            self.ui.videoview.setScaledContents(True)

    def cancel_process_video(self):
        self.video_timer.stop()
