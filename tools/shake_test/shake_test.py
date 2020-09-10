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
    """
    left = 0
    right = 1
    up = 2
    down = 4
    horizon = 8
    vertical = 16


class ShakeTestTool(object):
    video_valid = False
    only_select_move_point = False
    roi_up_crop = 0
    roi_down_crop = 0
    horizon_direction = Direction.left
    vertical_direction = Direction.up
    max_x_pl = None
    min_x_pl = None
    max_y_pl = None
    min_y_pl = None

    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_ShakeTestWindow()
        self.ui.setupUi(self.window)
        self.videoview = VideoView()
        self.ui.gridLayout_2.addWidget(self.videoview, 0, 0, 1, 1)
        self.videoview.sigDragEvent.connect(self.open_video_path)
        self.ui.openvideo.clicked.connect(self.open_video)
        self.ui.isok.clicked.connect(self.process_video)
        self.ui.cancel_button.clicked.connect(self.cancel_process_video)
        self.ui.skipframes.editingFinished.connect(self.set_skip_frames)
        self.ui.corner_num.valueChanged.connect(self.set_corner_num)
        self.ui.corner_size.valueChanged.connect(self.set_corner_size)
        self.ui.remove_move_point_enable.stateChanged.connect(
            self.set_find_move_point)
        self.ui.set_roi_up.editingFinished.connect(self.set_roi_up)
        self.ui.set_roi_down.editingFinished.connect(self.set_roi_down)
        self.video_timer = QTimer()
        self.skip_frames = 0

        # 构建角点检测所需参数
        self.feature_params = dict(maxCorners=30,
                                   qualityLevel=0.4,
                                   minDistance=50)

        # lucas kanade参数
        # 如果发现跟踪跟丢的问题，可能是光流法搜索的区域不够大
        self.lk_params = dict(winSize=(50, 50),
                              maxLevel=2)

    #######################################################################################
    # UI相关的函数
    #######################################################################################

    def show(self):
        self.window.show()

    def set_roi_up(self):
        self.roi_up_crop = self.ui.set_roi_up.value()
        self.vertify_video()

    def set_roi_down(self):
        self.roi_down_crop = self.ui.set_roi_down.value()
        self.vertify_video()

    def set_corner_num(self, num):
        self.feature_params = dict(maxCorners=30,
                                   qualityLevel=(num/100),
                                   minDistance=40)
        self.vertify_video()

    def set_corner_size(self, size):
        self.lk_params = dict(winSize=(size, size),
                              maxLevel=2)
        self.vertify_video()

    def set_skip_frames(self):
        self.skip_frames = self.ui.skipframes.value()
        self.vertify_video()

    def set_find_move_point(self, type):
        self.only_select_move_point = type
        self.vertify_video()

    def process_video(self):
        if(self.video_valid == True):
            self.vertify_video()
            # 增加定时器，每100ms进行一帧的处理
            self.video_timer.start(100)
            self.video_timer.timeout.connect(self.open_frame)

    def cancel_process_video(self):
        self.video_timer.stop()

    def open_video(self):
        videopath = QFileDialog.getOpenFileName(
            None, '打开文件', './', 'video files(*.mp4)')
        if(videopath[0] != ''):
            self.ui.videopath.setText(videopath[0])
            self.vertify_video()

    def open_video_path(self, str):
        self.ui.videopath.setText(str)
        self.vertify_video()

    #######################################################################################
    # 主要运行逻辑
    #######################################################################################
    def vertify_video(self):
        # 输出参数初始化
        self.dewarp_sum = 0
        self.dewarp_count = 0
        self.vidcap = cv2.VideoCapture(self.ui.videopath.text())
        # 片头调过多少帧
        self.vidcap.set(cv2.CAP_PROP_POS_FRAMES, self.skip_frames)
        success, frame = self.vidcap.read()
        if success:
            height = frame.shape[0]
            width = frame.shape[1]
            self.old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 进行ROI的选取
            mask = np.zeros_like(self.old_gray)
            if(self.roi_up_crop + self.roi_down_crop < height):
                mask[self.roi_up_crop:(height-self.roi_down_crop), :] = 1
            else:
                critical_window_show('裁剪区域过大，请重新选取ROI区域')
                self.video_valid = False
                return

            # 返回所有检测特征点，需要输入图片，角点的最大数量，品质因子，minDistance=7如果这个角点里有比这个强的就不要这个弱的
            self.p0 = cv2.goodFeaturesToTrack(
                self.old_gray, mask=mask, **self.feature_params)

            # 获取角点的精确坐标
            self.p0 = cv2.cornerSubPix(self.old_gray, self.p0, (5, 5), (-1, -1),
                                       criteria=(cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.001))

            # 与下一帧进行对比，找到运动的点，排除掉静止的点
            if(self.only_select_move_point == 2):
                self.p0 = self.find_move_points(self.p0)

            # 创建一个mask, 用于进行横线的绘制
            self.mask = np.zeros_like(self.old_gray)

            # 画出ROI区域
            cv2.line(self.mask, (0, self.roi_up_crop),
                     (width, self.roi_up_crop), 255, thickness=2)
            cv2.line(self.mask, (0, height-self.roi_down_crop),
                     (width, height-self.roi_down_crop), 255, thickness=2)

            # 寻找到中心最近的特征点
            center_x = width/2
            center_y = height/2
            self.center_index = self.find_center_point_index(
                center_x, center_y, (width/8)*(width/8))

            # 显示特征点的位置
            for i, point in enumerate(self.p0):
                a, b = point.ravel()
                if(i != self.center_index):
                    frame = cv2.circle(self.old_gray, (a, b), 4, 255, -1)
                else:
                    frame = cv2.circle(self.old_gray, (a, b), 8, 255, -1)
            img = cv2.add(frame, self.mask)
            self.display(img)

            # 如果在距离中心直径300px的范围内没有找到，那么退出
            if (self.center_index == -1):
                critical_window_show('图像中心没有找到特征点，请重新拍摄视频')
                self.video_valid = False
            else:
                # 初始化横纵方向上的坐标
                self.min_y_coord = self.max_y_coord = self.p0[self.center_index].ravel()[
                    1]
                self.min_x_coord = self.max_x_coord = self.p0[self.center_index].ravel()[
                    0]
                self.video_valid = True
                # 计算每个特征点到中心的距离
                self.old_distance_anypoint = self.calc_distance_anypoint(
                    self.p0)

        else:
            critical_window_show('视频打不开')
            self.video_valid = False
            return

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

            # 计算图片运动方向,并更新图像最左与最右的值
            (horizon_trig, vertical_trig) = self.calc_center_direction(pl)
            if(horizon_trig == 1):
                ret = self.calc_direction_result(
                    Direction.horizon, self.max_x_pl, self.min_x_pl)
                self.set_result(Direction.horizon, ret)

            if (vertical_trig == 1):
                ret = self.calc_direction_result(
                    Direction.vertical, self.max_y_pl, self.min_y_pl)
                self.set_result(Direction.vertical, ret)

            # 绘制轨迹
            self.draw_track(pl, new_gray)

            # self.calc_center_distance(pl)

        else:
            self.video_timer.stop()

    #######################################################################################
    # 计算相关的函数
    #######################################################################################
    def calc_direction_result(self, direction, max_pl, min_pl):
        diff_sum = 0
        max_move = 0
        variance_sum = 0

        # 求中心点的位移
        if(direction == Direction.horizon):
            # 横向位移计算
            diff_center = max_pl[self.center_index].ravel(
            )[0] - min_pl[self.center_index].ravel()[0]
        else:
            # 纵向位移计算
            diff_center = max_pl[self.center_index].ravel(
            )[1] - min_pl[self.center_index].ravel()[1]

        for i, (max_point, min_point) in enumerate(zip(max_pl, min_pl)):
            a, b = max_point.ravel()
            c, d = min_point.ravel()
            if(direction == Direction.horizon):
                diff = a - c
            else:
                diff = b - d

            diff_sum += diff
            # 求各点最大位移
            if (diff > max_move):
                max_move = diff

            # 求方差
            variance_sum += (diff - diff_center) * (diff - diff_center)

        # 求各点的平均位移
        diff_average = diff_sum / max_pl.shape[0]
        variance = variance_sum / \
            ((max_pl.shape[0]-1)*diff_center*diff_center)
        return (diff_center, max_move, diff_average, variance)

    def find_move_points(self, p0):
        success, frame = self.vidcap.read()
        if success:
            new_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 进行光流检测需要输入前一帧和当前图像及前一帧检测到的角点
            pl, st, err = cv2.calcOpticalFlowPyrLK(
                self.old_gray, new_gray, p0, None, **self.lk_params)
            return p0[st == 1]

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

    def calc_center_direction(self, input_array):
        """
        通过中心点的位移，计算图片运动的方向
        """
        center_point_x, center_point_y = input_array[self.center_index].ravel()
        old_center_point_x, old_center_point_y = self.p0[self.center_index].ravel(
        )
        vertical_once_trig = 0
        horizon_once_trig = 0
        if (self.horizon_direction == Direction.left):
            if (center_point_x - old_center_point_x > 0):
                self.horizon_direction = Direction.right
                self.min_x_pl = self.p0
        else:
            if (center_point_x - old_center_point_x < 0):
                self.horizon_direction = Direction.left
                self.max_x_pl = self.p0
                horizon_once_trig = 1

        if (self.vertical_direction == Direction.up):
            if (center_point_y - old_center_point_y < 0):
                self.vertical_direction = Direction.down
                self.max_y_pl = self.p0
        else:
            if (center_point_y - old_center_point_y > 0):
                self.vertical_direction = Direction.up
                self.min_y_pl = self.p0
                vertical_once_trig = 1
        return (horizon_once_trig, vertical_once_trig)

    def set_result(self, direction, ret):
        # self.ui.center_max_y_distance.setValue(
        #     self.max_y_coord-self.min_y_coord)
        # self.ui.center_max_x_distance.setValue(
        #     self.max_x_coord - self.min_x_coord)

        # 计算每个点与中心点的距离，将之与第一帧对比，得出变形程度
        # now_distance_anypoint = self.calc_distance_anypoint(pl)
        # distance_diff_sum = 0
        # for (old, new) in zip(self.old_distance_anypoint, now_distance_anypoint):
        #     distance_diff = abs((old-new)/old)
        #     distance_diff_sum += distance_diff
        # print(distance_diff_sum/len(self.old_distance_anypoint))

        # if(self.dewarp_sum < distance_diff_sum/len(self.old_distance_anypoint)):
        #     self.dewarp_sum = distance_diff_sum / \
        #         len(self.old_distance_anypoint)
        #     self.ui.warp_ratio.setValue(self.dewarp_sum)
        (diff_center, max_move, diff_average, variance) = ret
        if (direction == Direction.horizon):
            (diff_center, max_move, diff_average, variance) = ret
            self.ui.center_max_x_distance.setValue(diff_center)
            self.ui.any_max_x_distance.setValue(max_move)
            self.ui.any_average_x_distance.setValue(diff_average)
            self.ui.photo_warp_ratio_x.setValue(variance)
        else:
            (diff_center, max_move, diff_average, variance) = ret
            self.ui.center_max_y_distance.setValue(diff_center)
            self.ui.any_max_y_distance.setValue(max_move)
            self.ui.any_average_y_distance.setValue(diff_average)
            self.ui.photo_warp_ratio_y.setValue(variance)

    def find_center_point_index(self, x, y, winSize=90000):
        """
        寻找到中心最近的特征点
        """
        center_index = -1
        for i, point in enumerate(self.p0):
            a, b = point.ravel()
            now_distance = (a-x)*(a-x) + (b-y)*(b-y)
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

    #######################################################################################
    # 功能相关函数
    #######################################################################################

    def critical_window_show(self, str):
        reply = QMessageBox.critical(
            self.window, '警告', str,
            QMessageBox.Yes, QMessageBox.Yes)
        return

    def display(self, img):
        image = QImage(
            img.data, img.shape[1], img.shape[0], QImage.Format_Indexed8)
        temp_pixmap = QPixmap.fromImage(image)
        self.videoview.setPixmap(temp_pixmap)
        self.videoview.setScaledContents(True)

    def draw_track(self, good_new, new_gray):
        for i, (new, old) in enumerate(zip(good_new, self.p0)):
            a, b = new.ravel()
            c, d = old.ravel()

            self.mask = cv2.line(
                self.mask, (a, b), (c, d), 255, 2)
            if(i != self.center_index):
                frame = cv2.circle(new_gray, (a, b), 4, 255, -1)
            else:
                frame = cv2.circle(new_gray, (a, b), 8, 255, -1)

        # 将两个图片进行结合，并进行图片展示
        img = cv2.add(frame, self.mask)

        # 更新前一帧图片和角点的位置
        self.old_gray = new_gray.copy()
        self.p0 = good_new.reshape(-1, 1, 2)

        # display
        self.display(img)
