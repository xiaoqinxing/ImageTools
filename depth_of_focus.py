import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
import sys
from field_depth_ui import Ui_MainWindow
import math

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class LenParameters(object):
    def __init__(self):
        '''
        @focus_length: 实际焦距(单位mm)
        @aperture: 光圈(F)
        @focus_distance: 对焦距离(单位mm)
        @effective_focus_length: 有效焦距(单位mm)
        @confusion_circle_diam: 弥散圈直径(单位mm)
        @cmos_size: sensor尺寸(单位mm)
        '''
        self.focus_length = 0
        self.aperture = 0
        self.focus_distance = 0
        self.effective_focus_length = 0
        self.focus_distance_range = [0, 0]
        self.confusion_circle_diam = 0
        self.cmos_size = 0

    def show(self):
        '''
        调试打印
        '''
        print('=========================================')
        print('实际焦距: ' + str(self.focus_length) + ' mm')
        print('光圈: F/' + str(self.aperture))
        print('对焦距离: ' + str(self.focus_distance) + ' mm')
        print('有效焦距: ' + str(self.effective_focus_length) + ' mm')
        print('弥散圈直径: ' + str(self.confusion_circle_diam) + ' mm')
        print('=========================================')

    def calc_front_field_depth(self):
        """
        计算前景深，有两种方法：本文用的https://wenku.baidu.com/view/2191302baf45b307e9719706.html的方法，更加准确一点
        """
        # a = self.aperture*self.confusion_circle_diam * \
        #     self.focus_distance*self.focus_distance
        # b = self.focus_length*self.focus_length + self.aperture * \
        #     self.confusion_circle_diam*self.focus_distance
        a = self.focus_length*self.focus_length*self.focus_distance
        b = self.focus_length*self.focus_length + \
            (self.focus_distance - self.focus_length) * \
            self.aperture*self.confusion_circle_diam
        return (a/b)

    def calc_back_field_depth(self):
        """
        计算后景深
        """
        # a = self.aperture*self.confusion_circle_diam * \
        #     self.focus_distance*self.focus_distance
        # b = self.focus_length*self.focus_length - self.aperture * \
        #     self.confusion_circle_diam*self.focus_distance
        a = self.focus_length*self.focus_length*self.focus_distance
        b = self.focus_length*self.focus_length - \
            (self.focus_distance - self.focus_length) * \
            self.aperture*self.confusion_circle_diam
        return (a/b)

    def calc_infinity_depth_distance(self):
        '''
        计算后景深无穷大时的像距
        '''
        return (self.focus_length*self.focus_length/self.aperture/self.confusion_circle_diam+self.focus_length)

    def calc_confusion_circle_diam(self):
        '''
        通过CMOS的尺寸计算弥散圈直径，默认是CMOS对角线尺寸除1000
        '''
        self.confusion_circle_diam = self.cmos_size/1000
        return self.confusion_circle_diam

    def calc_image_distance(self, step=10, unit=1000):
        '''
        计算不同物距范围内的像距
        '''
        y = list()
        x = range(self.focus_distance_range[0],
                  self.focus_distance_range[1], step*10)
        for self.focus_distance in x:
            y.append((self.focus_distance*self.focus_length) /
                     (self.focus_distance-self.focus_length))
        return (x, y)

    def calc_field_depth(self):
        '''
        计算总景深，后景深减去前景深
        '''
        return (self.calc_back_field_depth() - self.calc_front_field_depth())

    def calc_fov(self):
        '''
        计算对角线视场角
        '''
        image_distance = (self.focus_distance*self.focus_length)/(self.focus_distance-self.focus_length)
        alpha = math.atan((self.cmos_size/2)/image_distance)
        return (2*alpha*180/math.pi)

    def calc_depth_map(self, step=10, unit=1000):
        '''
        计算不同物距范围内的景深
        '''
        y1 = list()
        y2 = list()
        x = range(self.focus_distance_range[0],
                  self.focus_distance_range[1], step*10)
        for self.focus_distance in x:
            y1.append(self.calc_front_field_depth())
            value = self.calc_back_field_depth()
            # 防止后景深计算为负数
            if(value <= 0):
                value = float('inf')
            y2.append(value)
        y1 = np.array(y1)/unit
        y2 = np.array(y2)/unit
        x = np.array(x)/unit
        return (x, y1, y2)


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class App(object):
    def __init__(self):
        app = QApplication(sys.argv)
        app.setStyle('Fusion')
        window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(window)
        window.show()
        self.field_depth_figure = None
        self.image_distance_figure = None
        self.params = LenParameters()
        self.get_ui_params()
        self.params.show()
        self.pri_params = LenParameters()
        self.ui.pushButton.clicked.connect(self.finished_plot_cb)
        self.ui.sensor_size.editingFinished.connect(self.coms_size_changed_cb)

        print("前景深："+str(self.params.calc_front_field_depth()/1000) + 'm')
        print("后景深："+str(self.params.calc_back_field_depth()/1000) + 'm')
        print("总景深：" + str(self.params.calc_field_depth()/1000)+'m')
        self.params.focus_distance_range = [1000, 5000]
        self.plot_field_depth()
        self.plot_image_distance()
        self.updatePlot = False
        sys.exit(app.exec_())

    def plot_field_depth(self):
        (x, y1, y2) = self.params.calc_depth_map()
        field_depth_figure = MplCanvas()
        field_depth_figure.axes.plot(x, y1)
        field_depth_figure.axes.plot(x, y2)
        field_depth_figure.axes.plot(x, x)
        field_depth_figure.axes.fill_between(
            x, y1, y2, color='blue', alpha=0.25)
        if(self.field_depth_figure == None):
            self.ui.gridLayout.addWidget(field_depth_figure)
            self.field_depth_figure = field_depth_figure
        else:
            self.ui.gridLayout.replaceWidget(
                self.field_depth_figure, field_depth_figure)
            self.field_depth_figure = field_depth_figure

    def plot_image_distance(self):
        (x, y) = self.params.calc_image_distance()
        image_distance_figure = MplCanvas()
        image_distance_figure.axes.plot(x, y)
        if(self.image_distance_figure == None):
            self.ui.gridLayout.addWidget(image_distance_figure)
            self.image_distance_figure = image_distance_figure
        else:
            self.ui.gridLayout.replaceWidget(
                self.image_distance_figure, image_distance_figure)
            self.image_distance_figure = image_distance_figure

    def is_params_changed(self):
        self.get_ui_params()
        if(self.params.focus_length != self.pri_params or
            self.params.confusion_circle_diam != self.pri_params.confusion_circle_diam or
            self.params.aperture != self.pri_params.aperture or
            self.params.focus_distance != self.pri_params.focus_distance or
            self.params.cmos_size != self.pri_params.cmos_size
           ):
            return True
        else:
            return False

    def get_ui_params(self):
        self.params.focus_length = float(self.ui.focus_length.text())
        self.params.confusion_circle_diam = float(
            self.ui.confusion_circle_diam.text())
        self.params.aperture = float(self.ui.aperture.text())
        self.params.focus_distance = float(self.ui.focus_distance.text())*1000
        self.params.cmos_size = float(self.ui.sensor_size.text())

    # CALLBACKS
    def finished_plot_cb(self):
        if(self.is_params_changed() == True):
            self.pri_params = self.params
            self.plot_field_depth()
            self.plot_image_distance()
            print('视场角：'+str(self.params.calc_fov()))

    def coms_size_changed_cb(self):
        self.params.cmos_size = float(self.ui.sensor_size.text())
        value = self.params.calc_confusion_circle_diam()
        self.ui.confusion_circle_diam.setValue(value)

if __name__ == "__main__":
    app = App()
