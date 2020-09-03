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

        # 构建角点检测所需参数
        self.feature_params = dict(maxCorners=100,
                                   qualityLevel=0.3,
                                   minDistance=7)

        # lucas kanade参数
        self.lk_params = dict(winSize=(15, 15),
                              maxLevel=2)

    def show(self):
        self.window.show()

    def open_video(self):
        videopath = QFileDialog.getOpenFileName(
            None, '打开文件', './', 'video files(*.mp4)')
        self.ui.videopath.setText(videopath[0])

    def process_video(self):
        self.vidcap = cv2.VideoCapture(self.ui.videopath.text())
        success, frame = self.vidcap.read()
        if success:
            self.old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.p0 = cv2.goodFeaturesToTrack(
                self.old_gray, mask=None, **self.feature_params)
            self.mask = np.zeros_like(self.old_gray)
        self.video_timer.start(100)
        self.video_timer.timeout.connect(self.open_frame)

    def open_frame(self):
        keypoints = list()
        success, frame = self.vidcap.read()
        if success:
            new_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 随机颜色条
            color = np.random.randint(0, 255, (100, 3))

            pl, st, err = cv2.calcOpticalFlowPyrLK(
                self.old_gray, new_gray, self.p0, None, **self.lk_params)

            good_new = pl[st == 1]
            good_old = self.p0[st == 1]

            # # 第九步：绘制轨迹
            for i, (new, old) in enumerate(zip(good_new, good_old)):
                a, b = new.ravel()
                c, d = old.ravel()
                self.mask = cv2.line(
                    self.mask, (a, b), (c, d), color[i].tolist(), 2)
                frame = cv2.circle(new_gray, (a, b), 5, color[i].tolist(), -1)

            # 第十步：将两个图片进行结合，并进行图片展示
            img = cv2.add(frame, self.mask)
            # 更新前一帧图片和角点的位置
            self.old_gray = new_gray.copy()

            self.p0 = good_new.reshape(-1, 1, 2)
            # corners = cv2.goodFeaturesToTrack(new_gray, 100, 0.2, 100)
            # if corners is not None and len(corners) > 0:
            #     for x, y in np.float32(corners).reshape(-1, 2):
            #         keypoints.append((x, y))
            # if keypoints is not None and len(keypoints) > 0:
            #     for x, y in keypoints:
            #         cv2.circle(new_gray, (int(x + 200), y), 3, (255, 255, 0))

            # display
            image = QImage(
                img.data, img.shape[1], img.shape[0], QImage.Format_Indexed8)
            temp_pixmap = QPixmap.fromImage(image)
            self.ui.videoview.setPixmap(temp_pixmap)
            self.ui.videoview.setScaledContents(True)

    def cancel_process_video(self):
        self.video_timer.stop()
