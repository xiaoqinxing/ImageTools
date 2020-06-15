import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
import sys
from field_depth_ui import Ui_MainWindow
import math
from enum import Enum

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg,NavigationToolbar2QT
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

    def calc_equivalent_focus_length(self):
        '''
        计算等效焦距
        '''
        return (43.27/self.cmos_size*self.focus_length)

    def calc_hyperfocal_distance(self):
        '''
        计算超焦距，刚好后景深是无穷远时的对焦距离
        '''
        return (self.focus_length*self.focus_length/self.aperture/self.confusion_circle_diam+self.focus_length)

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
        plt.rcParams['font.family'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        #self.axes.hold(False) #每次绘图时都不保留上一次绘图的结果
        super(MplCanvas, self).__init__(fig)

class MatplotlibWidget(QWidget):
    def __init__(self, layout):
        self.plt = MplCanvas()
        self.layout = layout
    
    def draw(self):
        self.layout.addWidget(self.plt)
        self.mpl_ntb = NavigationToolbar2QT(self.plt,parent=None)
        self.layout.addWidget(self.mpl_ntb)
    
    def input(self,x,y):
        self.plt.axes.plot(x, y)

    def input_2line(self,x,y1,y2):
        self.plt.axes.plot(x, y1,color='yellow')
        self.plt.axes.plot(x, y2,color='red')
        self.plt.axes.fill_between(x, y1, y2, color='blue', alpha=0.25)
    
    def label(self,string_x,string_y):
        self.plt.axes.set_xlabel(string_x)
        self.plt.axes.set_ylabel(string_y)


class SettingParamters(object):
    def __init__(self):
        # input setting
        self.input_focus_length = False
        self.input_apeture = False
        self.input_distance = False
        # output setting
        self.output_field_depth = False
        self.output_image_distance = False
        self.output_params = False

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
        self.setting = SettingParamters()
        self.params = LenParameters()
        self.get_ui_params()
        self.params.show()
        self.pri_params = LenParameters()
        self.ui.pushButton.clicked.connect(self.finished_plot_cb)
        self.ui.sensor_size.editingFinished.connect(self.coms_size_changed_cb)
        self.ui.confusion_circle_diam_slide.sliderMoved.connect(self.confusion_circle_diam_changed_cb)
        print("前景深："+str(self.params.calc_front_field_depth()/1000) + 'm')
        print("后景深："+str(self.params.calc_back_field_depth()/1000) + 'm')
        print("总景深：" + str(self.params.calc_field_depth()/1000)+'m')
        self.params.focus_distance_range = [1000, 5000]
        # self.plot_field_depth()
        # self.plot_image_distance()
        self.plot()
        self.updatePlot = False
        sys.exit(app.exec_())

    def plot(self):
        if(self.setting.output_field_depth == True):
            if(self.setting.input_distance == True):
                (x, y1, y2) = self.params.calc_depth_map()
                field_depth_figure = MatplotlibWidget(self.ui.gridLayout)
                field_depth_figure.input_2line(x,y1,y2)
                field_depth_figure.label("x","hello")
                field_depth_figure.draw()

    def plot_field_depth(self):
        (x, y1, y2) = self.params.calc_depth_map()
        field_depth_figure = MplCanvas()
        field_depth_figure.axes.plot(x, y1,color='yellow')
        field_depth_figure.axes.plot(x, y2,color='red')
        field_depth_figure.axes.plot(x, x,color='blue')
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

    def calc_len_params(self):
        print('视场角：'+str(self.params.calc_fov())+'度')
        print('等效焦距：'+str(self.params.calc_equivalent_focus_length())+'mm')
        print('超焦距：'+str(self.params.calc_hyperfocal_distance()/1000) + 'm')

    # get params
    def get_ui_params(self):
        # basic setting
        self.params.focus_length = float(self.ui.focus_length.text())
        self.params.confusion_circle_diam = float(
            self.ui.confusion_circle_diam.text())
        self.params.aperture = float(self.ui.aperture.text())
        self.params.focus_distance = float(self.ui.focus_distance.text())*1000
        self.params.cmos_size = float(self.ui.sensor_size.text())
        # input setting
        self.setting.input_focus_length = self.ui.input_focus_length.isChecked()
        self.setting.input_apeture = self.ui.input_apeture.isChecked()
        self.setting.input_distance = self.ui.input_distance.isChecked()
        # output setting
        self.setting.output_field_depth = self.ui.output_field_depth.isChecked()
        self.setting.output_image_distance = self.ui.output_image_distance.isChecked()
        self.setting.output_params = self.ui.output_params.isChecked()

    # CALLBACKS
    def finished_plot_cb(self):
        self.get_ui_params()
        self.plot()
        self.calc_len_params()

    def coms_size_changed_cb(self):
        self.params.cmos_size = self.ui.sensor_size.value()
        self.confusion_circle_diam_changed_cb()
    
    def confusion_circle_diam_changed_cb(self):
        value = self.ui.confusion_circle_diam_slide.value()
        self.params.confusion_circle_diam = self.params.cmos_size/1000*(0.5+value/100)
        self.ui.confusion_circle_diam.setValue(self.params.confusion_circle_diam)

if __name__ == "__main__":
    app = App()
