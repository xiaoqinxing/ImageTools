from PySide2.QtCore import Signal, QPoint
from PySide2.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QGraphicsView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from PySide2.QtWidgets import QMessageBox, QMainWindow


class MainWindow(QMainWindow):
    """对QMainWindow类重写，实现一些功能"""

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QMessageBox.question(self,
                                     'ImageTools',
                                     "是否要退出程序？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


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


class ParamsTable(QWidget):
    def __init__(self, layout):
        # 6行3列
        self.tableWidget = QTableWidget(6, 3)
        self.tableWidget.setHorizontalHeaderLabels(["参数", "值", "单位"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.line = 0
        self.layout = layout

    def append(self, name, value, uint):
        newItem = QTableWidgetItem(name)
        self.tableWidget.setItem(self.line, 0, newItem)
        newItem = QTableWidgetItem(value)
        self.tableWidget.setItem(self.line, 1, newItem)
        newItem = QTableWidgetItem(uint)
        self.tableWidget.setItem(self.line, 2, newItem)
        self.line += 1

    def show(self):
        self.layout.addWidget(self.tableWidget)

    def clean(self):
        self.layout.removeWidget(self.tableWidget)
        self.tableWidget = QTableWidget(6, 3)
        self.tableWidget.setHorizontalHeaderLabels(["参数", "值", "单位"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.line = 0


class ImageView(QGraphicsView):
    sigMouseMovePoint = Signal(QPoint)
    sigWheelEvent = Signal(float)

    def __init__(self, scene, parent):
        super().__init__(scene, parent)
        self.setMouseTracking(True)
        self.scale_ratio = 1.0

    def mouseMoveEvent(self, event):
        self.sceneMousePos = self.mapToScene(event.pos())
        self.sigMouseMovePoint.emit(self.sceneMousePos)
        print(self.sceneMousePos)
        return super().mouseMoveEvent(event)

    def wheelEvent(self, event):
        # return super().wheelEvent(event)
        angle = event.angleD.y()
        # self.centerOn(self.sceneMousePos)
        if (angle > 0):
            self.scale(1.2, 1.2)
            self.scale_ratio *= 1.2
        else:
            self.scale(1 / 1.2, 1 / 1.2)
            self.scale_ratio /= 1.2
        self.viewport().update()
        self.sigWheelEvent.emit(self.scale_ratio)
        return super().wheelEvent(event)
