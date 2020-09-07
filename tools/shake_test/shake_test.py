import cv2
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QTimer
from tools.shake_test.shake_test_window import Ui_ShakeTestWindow
from ui.customwidget import VideoView
import numpy as np
import math


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
    video_valid = False
    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_ShakeTestWindow()
        self.ui.setupUi(self.window)
        self.videoview = VideoView(self.ui.videoview)
        self.ui.gridLayout_2.addWidget(self.videoview, 0, 0, 1, 1)
        self.videoview.sigDragEvent.connect(self.open_video_path)
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
        self.lk_params = dict(winSize=(25, 25),
                              maxLevel=2)

    def show(self):
        self.window.show()

    def open_video(self):
        videopath = QFileDialog.getOpenFileName(
            None, '打开文件', './', 'video files(*.mp4)')
        if(videopath[0] != ''):
            self.ui.videopath.setText(videopath[0])
            self.vertify_video()

    def open_video_path(self, str):
        self.ui.videopath.setText(str)
        self.vertify_video()

    def find_center_point_index(self, x, y, winSize=90000):
        """
        寻找到中心最近的特征点
        """
        center_index = -1
        for i, point in enumerate(self.p0):
            now_distance = (point[0][0]-x)*(point[0][0]-x) + \
                (point[0][1]-y)*(point[0][1]-y)
            if(now_distance < winSize):
                center_index = i
                winSize = now_distance
        return center_index

    def calc_distance_anypoint(self, input_array):
        """
        计算每个特征点到中心的距离
        """
        distance_anypoint = list()
        for i, point in enumerate(input_array):
            if(i != self.center_index):
                now_point = point.ravel()
                center_point = input_array[self.center_index].ravel()
                distance_anypoint.append(math.sqrt((now_point[0]-center_point[0])*(now_point[0]-center_point[0])
                                                   + (now_point[1]-center_point[1])*(now_point[1]-center_point[1])))
        return distance_anypoint
    
    def vertify_video(self):
        # 输出参数初始化
        self.dewarp_sum = 0
        self.dewarp_count = 0
        self.vidcap = cv2.VideoCapture(self.ui.videopath.text())
        success, frame = self.vidcap.read()
        if success:
            self.old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 返回所有检测特征点，需要输入图片，角点的最大数量，品质因子，minDistance=7如果这个角点里有比这个强的就不要这个弱的
            self.p0 = cv2.goodFeaturesToTrack(
                self.old_gray, mask=None, **self.feature_params)

            # 获取角点的精确坐标
            self.p0 = cv2.cornerSubPix(self.old_gray, self.p0, (5, 5), (-1, -1),
                                       criteria=(cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.001))
            # 创建一个mask, 用于进行横线的绘制
            self.mask = np.zeros_like(self.old_gray)

            # 寻找到中心最近的特征点
            center_x = frame.shape[1]/2
            center_y = frame.shape[0]/2
            self.center_index = self.find_center_point_index(
                center_x, center_y, (frame.shape[1]/10)*(frame.shape[1]/10))

            # 如果在距离中心直径300px的范围内没有找到，那么退出
            if(self.center_index == -1):
                reply = QMessageBox.critical(
                    self.window, '警告', '图像中心没有找到特征点，请重新拍摄视频',
                    QMessageBox.Yes, QMessageBox.Yes)
                self.video_valid = False
                return

            # 初始化横纵方向上的坐标
            self.min_y_coord = self.max_y_coord = self.p0[self.center_index].ravel()[
                1]
            self.min_x_coord = self.max_x_coord = self.p0[self.center_index].ravel()[
                0]

            # 计算每个特征点到中心的距离
            self.old_distance_anypoint = self.calc_distance_anypoint(self.p0)
            self.display(self.old_gray)
            self.video_valid = True
        else:
            reply = QMessageBox.critical(
                self.window, '警告', '视频打不开',
                QMessageBox.Yes, QMessageBox.Yes)
            self.video_valid = False
            return

    def process_video(self):
        if(self.video_valid == True):
            # 增加定时器，每100ms进行一帧的处理
            self.video_timer.start(100)
            self.video_timer.timeout.connect(self.open_frame)

    def display(self, img):
        image = QImage(
            img.data, img.shape[1], img.shape[0], QImage.Format_Indexed8)
        temp_pixmap = QPixmap.fromImage(image)
        self.ui.videoview.setPixmap(temp_pixmap)
        self.ui.videoview.setScaledContents(True)

    def draw_track(self, good_new, new_gray):
        for i, (new, old) in enumerate(zip(good_new, self.p0)):
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
        self.display(img)

    def open_frame(self):
        self.dewarp_count += 1
        success, frame = self.vidcap.read()
        if success:
            new_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 进行光流检测需要输入前一帧和当前图像及前一帧检测到的角点
            pl, st, err = cv2.calcOpticalFlowPyrLK(
                self.old_gray, new_gray, self.p0, None, **self.lk_params)
            # 在原角点的基础上寻找亚像素角点，其中，criteria是设置寻找亚像素角点的参数，
            # 采用的停止准则是最大循环次数30和最大误差容限0.001
            pl = cv2.cornerSubPix(new_gray, pl, (5, 5), (-1, -1),
                                  criteria=(cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.001))

            now_distance_anypoint = self.calc_distance_anypoint(pl)

            # 绘制轨迹
            self.draw_track(pl, new_gray)

            # 计算每个点与中心点的距离，将之与第一帧对比，得出变形程度
            distance_diff_sum = 0
            for (old, new) in zip(self.old_distance_anypoint, now_distance_anypoint):
                distance_diff = abs((old-new)/old)
                distance_diff_sum += distance_diff
            print(distance_diff_sum/len(self.old_distance_anypoint))

            if(self.dewarp_sum < distance_diff_sum/len(self.old_distance_anypoint)):
                self.dewarp_sum = distance_diff_sum / \
                    len(self.old_distance_anypoint)
                self.ui.warp_ratio.setValue(self.dewarp_sum)

            self.calc_center_distance(pl)
            self.ui.center_max_y_distance.setValue(
                self.max_y_coord-self.min_y_coord)
            self.ui.center_max_x_distance.setValue(
                self.max_x_coord-self.min_x_coord)
            # self.dewarp_sum += distance_diff_sum / \
            #     len(self.old_distance_anypoint)
            # dewarp_ratio = self.dewarp_sum/self.dewarp_count
            # print(dewarp_ratio)
            # self.ui.warp_ratio.setValue(dewarp_ratio)

    def cancel_process_video(self):
        self.video_timer.stop()

    def calc_center_distance(self, input_array):
        center_point = input_array[self.center_index].ravel()
        if(self.min_y_coord > center_point[1]):
            self.min_y_coord = center_point[1]
        elif(self.max_y_coord < center_point[1]):
            self.max_y_coord = center_point[1]
        if(self.min_x_coord > center_point[0]):
            self.min_x_coord = center_point[0]
        elif(self.max_x_coord < center_point[0]):
            self.max_x_coord = center_point[0]
