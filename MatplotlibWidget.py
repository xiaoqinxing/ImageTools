from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        plt.rcParams['font.family'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # self.axes.hold(False) #每次绘图时都不保留上一次绘图的结果
        super(MplCanvas, self).__init__(fig)


class MatplotlibWidget(QWidget):
    def __init__(self, layout):
        self.plt = MplCanvas()
        self.layout = layout
        self.mpl_ntb = NavigationToolbar2QT(self.plt, parent=None)

    def draw(self, navigationBar=True):
        self.layout.addWidget(self.plt)
        if navigationBar == True:
            self.layout.addWidget(self.mpl_ntb)

    def clean(self, navigationBar=True):
        self.layout.removeWidget(self.plt)
        if navigationBar == True:
            self.layout.removeWidget(self.mpl_ntb)
        self.plt = MplCanvas()
        self.mpl_ntb = NavigationToolbar2QT(self.plt, parent=None)

    def input(self, x, y):
        self.plt.axes.plot(x, y)

    def input_2line(self, x, y1, y2):
        self.plt.axes.plot(x, y1, color='green')
        self.plt.axes.plot(x, y2, color='red')
        self.plt.axes.fill_between(x, y1, y2, color='blue', alpha=0.25)

    def label(self, string_x, string_y, enable_grid=True):
        self.plt.axes.set_xlabel(string_x)
        self.plt.axes.set_ylabel(string_y)
        if enable_grid == True:
            self.plt.axes.grid(True)