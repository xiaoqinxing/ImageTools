from components.ui.histgramview import Ui_HistgramView
from PySide2.QtWidgets import QGraphicsView, QDialog
from components.customwidget import MatplotlibWidget
import numpy as np
import cv2


class HistView(QDialog):
    def __init__(self, parent):
        """
        func: 初始化直方图统计信息UI，把父类的指针变成选中方框模式
        """
        super().__init__(parent)
        self.parent = parent
        self.parent.setDragMode(QGraphicsView.RubberBandDrag)
        self.ui = Ui_HistgramView()
        self.ui.setupUi(self)
        self.ui.r_enable.stateChanged.connect(
            self.on_r_hist_enable)
        self.ui.g_enable.stateChanged.connect(
            self.on_g_hist_enable)
        self.ui.b_enable.stateChanged.connect(
            self.on_b_hist_enable)
        self.ui.y_enable.stateChanged.connect(
            self.on_y_hist_enable)
        self.histview = MatplotlibWidget(
            self.ui.gridLayout_10)
        self.x_axis = np.linspace(0, 255, num=256)
        self.r_hist_visible = 2
        self.g_hist_visible = 2
        self.b_hist_visible = 2
        self.y_hist_visible = 2
        self.enable = True

    def update_rect_data(self, img, rect):
        """
        func: 更新方框内的图像统计信息
        """
        (rect, image) = self.update_rect(img, rect)
        self.calcHist(image)
        self.hist_show()
        self.stats_show(self.calcStatics(image, rect))

    def closeEvent(self, event):
        """
        func: 关闭窗口的时候，把鼠标还原
        """
        self.parent.setDragMode(QGraphicsView.ScrollHandDrag)
        self.enable = False
        return super().closeEvent(event)

    def update_rect(self, img, rect):
        [x1, y1, x2, y2] = rect
        i1 = max(x1, 0)
        i2 = min(x2, img.shape[1])
        j1 = max(y1, 0)
        j2 = min(img.shape[0], y2)
        if (i2 > i1 and j2 > j1):
            img = img[j1:j2, i1:i2][:, :, :3]
            rect = [j1, i1, j2, i2]
        return (rect, img)

    def calcStatics(self, img, rect):
        [j1, i1, j2, i2] = rect
        (average_rgb, stddv_rgb) = cv2.meanStdDev(img)
        # TODO 信噪比的公式有些问题，当标准差为0的时候，信噪比该是无穷大
        snr_rgb = 20 * np.log10(average_rgb/stddv_rgb)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        (average_yuv, stddv_yuv) = cv2.meanStdDev(img)
        snr_yuv = 20 * np.log10(average_yuv/stddv_yuv)
        rgb_ratio = [0.0, 0.0]
        awb_gain = [0.0, 0.0, 0.0]
        rgb_ratio[0] = average_rgb[2]/average_rgb[1]
        rgb_ratio[1] = average_rgb[0]/average_rgb[1]
        awb_gain[0] = 1/rgb_ratio[0]
        awb_gain[1] = 1
        awb_gain[2] = 1/rgb_ratio[1]
        enable_rect = [i1, j1, i2-i1, j2-j1]
        return (average_rgb, snr_rgb, average_yuv, snr_yuv, rgb_ratio, awb_gain, enable_rect)

    def calcHist(self, img):
        chans = cv2.split(img)
        self.b_hist = (cv2.calcHist([chans[0]], [0], None, [
            256], [0, 256]))
        self.g_hist = (cv2.calcHist([chans[1]], [0], None, [
            256], [0, 256]))
        self.r_hist = (cv2.calcHist([chans[2]], [0], None, [
            256], [0, 256]))
        # 转为灰度图，然后算亮度直方图
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        self.y_hist = (cv2.calcHist([img], [0], None, [
            256], [0, 256]))
        self.r_hist.reshape(1, 256)
        self.g_hist.reshape(1, 256)
        self.b_hist.reshape(1, 256)
        self.y_hist.reshape(1, 256)

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
        self.ui.average_r.setValue(average_rgb[2])
        self.ui.average_g.setValue(average_rgb[1])
        self.ui.average_b.setValue(average_rgb[0])
        self.ui.average_y.setValue(average_yuv[0])
        self.ui.average_cr.setValue(average_yuv[1])
        self.ui.average_cb.setValue(average_yuv[2])
        self.ui.rg_ratio.setValue(rgb_ratio[0])
        self.ui.bg_ratio.setValue(rgb_ratio[1])
        self.ui.r_gain.setValue(awb_gain[0])
        self.ui.g_gain.setValue(awb_gain[1])
        self.ui.b_gain.setValue(awb_gain[2])
        self.ui.section_x.setValue(enable_rect[0])
        self.ui.section_y.setValue(enable_rect[1])
        self.ui.section_height.setValue(enable_rect[2])
        self.ui.section_width.setValue(enable_rect[3])
        self.ui.snr_r.setValue(snr_rgb[2])
        self.ui.snr_g.setValue(snr_rgb[1])
        self.ui.snr_b.setValue(snr_rgb[0])
        self.ui.snr_y.setValue(snr_yuv[0])
        self.ui.snr_cr.setValue(snr_yuv[1])
        self.ui.snr_cb.setValue(snr_yuv[2])
