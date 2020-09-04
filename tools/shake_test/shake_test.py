import cv2
from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QTimer
from ui.windows.shake_test_window import Ui_ShakeTestWindow
import numpy as np

class Direction():
    """
    角点运动的方向
    source是方向不动
    """
    left = 0
    right = 1
    up = 2
    down = 4
    source = 8

class ShakeTestTool(object):
    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_ShakeTestWindow()
        self.ui.setupUi(self.window)
        self.ui.openvideo.clicked.connect(self.open_video)
        self.ui.isok.clicked.connect(self.process_video)
        self.ui.cancel_button.clicked.connect(self.cancel_process_video)
        self.video_timer = QTimer()
        self.direction = Direction.source

        # 构建角点检测所需参数
        self.feature_params = dict(maxCorners=30,
                                   qualityLevel=0.4,
                                   minDistance=50)

        # lucas kanade参数
        # 如果发现跟踪跟丢的问题，可能是光流法搜索的区域不够大
        self.lk_params = dict(winSize=(20, 20),
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
            # 返回所有检测特征点，需要输入图片，角点的最大数量，品质因子，minDistance=7如果这个角点里有比这个强的就不要这个弱的
            self.p0 = cv2.goodFeaturesToTrack(
                self.old_gray, mask=None, **self.feature_params)
            # 创建一个mask, 用于进行横线的绘制
            self.mask = np.zeros_like(self.old_gray)
            # 随机颜色条
            # self.color = np.random.randint(0, 255, (50, 3))
            self.video_timer.start(100)
            self.video_timer.timeout.connect(self.open_frame)

    def open_frame(self):
        success, frame = self.vidcap.read()
        if success:
            new_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # 进行光流检测需要输入前一帧和当前图像及前一帧检测到的角点
            pl, st, err = cv2.calcOpticalFlowPyrLK(
                self.old_gray, new_gray, self.p0, None, **self.lk_params)
            # 在原角点的基础上寻找亚像素角点，其中，criteria是设置寻找亚像素角点的参数，
			# 采用的停止准则是最大循环次数30和最大误差容限0.001
            pl = cv2.cornerSubPix(new_gray, pl, (5, 5), (-1, -1),
								criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.001))

            # 读取运动了的角点st == 1表示检测到的运动物体，即v和u表示为0
            good_new = pl[st == 1]
            good_old = self.p0[st == 1]

            # 绘制轨迹
            for i, (new, old) in enumerate(zip(good_new, good_old)):
                a, b = new.ravel()
                c, d = old.ravel()
                
                self.mask = cv2.line(
                    self.mask, (a, b), (c, d), 255, 2)
                frame = cv2.circle(new_gray, (a, b), 5, 255, -1)

            # 将两个图片进行结合，并进行图片展示
            img = cv2.add(frame, self.mask)

            # 更新前一帧图片和角点的位置
            self.old_gray = new_gray.copy()

            self.p0 = good_new.reshape(-1, 1, 2)

            # display
            image = QImage(
                img.data, img.shape[1], img.shape[0], QImage.Format_Indexed8)
            temp_pixmap = QPixmap.fromImage(image)
            self.ui.videoview.setPixmap(temp_pixmap)
            self.ui.videoview.setScaledContents(True)

    def cancel_process_video(self):
        self.video_timer.stop()
