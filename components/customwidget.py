from PySide2.QtCore import Signal, QPointF, Qt, QSize
from PySide2.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QGraphicsView, QAbstractScrollArea, QLabel, QProgressBar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from PySide2.QtWidgets import QMessageBox, QGraphicsScene
from PySide2.QtGui import QPixmap, QImage


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        plt.rcParams['font.family'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # self.axes.hold(False) #每次绘图时都不保留上一次绘图的结果
        super(MplCanvas, self).__init__(fig)


class MatplotlibLayout(QWidget):
    """
    自定义的matplot窗口
    """

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


class MatplotlibWidget(QWidget):
    """
    自定义的matplot窗口
    """

    def __init__(self, layout):
        super().__init__()
        self.layout = layout
        self.plt = MplCanvas()
        self.first_draw = 0
        self.setMinimumSize(QSize(352, 0))
        # self.mpl_ntb = NavigationToolbar2QT(self.plt, parent=None)

    def draw(self, navigationBar=True):
        self.layout.addWidget(self.plt, 1, 1, 1, 1)
        self.first_draw = 1

    def clean(self, navigationBar=True):
        if self.first_draw == 1:
            self.layout.removeWidget(self.plt)
            self.plt = MplCanvas()

    def input(self, x, y):
        self.plt.axes.plot(x, y)

    def input_2line(self, x, y1, y2):
        self.plt.axes.plot(x, y1, color='green')
        self.plt.axes.plot(x, y2, color='red')
        self.plt.axes.fill_between(x, y1, y2, color='blue', alpha=0.25)

    def input_r_hist(self, x, y):
        self.plt.axes.plot(x, y, color='red')

    def input_g_hist(self, x, y):
        self.plt.axes.plot(x, y, color='green')

    def input_b_hist(self, x, y):
        self.plt.axes.plot(x, y, color='blue')

    def input_y_hist(self, x, y):
        self.plt.axes.plot(x, y, color='black')

    def label(self, string_x, string_y, enable_grid=True):
        self.plt.axes.set_xlabel(string_x)
        self.plt.axes.set_ylabel(string_y)
        if enable_grid == True:
            self.plt.axes.grid(True)


class ParamsTable(QWidget):
    """
    自定义的镜头参数表
    """

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
    """
    自定义的图片显示（可以获取到鼠标位置和放大比例）
    """
    sigMouseMovePoint = Signal(QPointF)
    sigWheelEvent = Signal(float)
    sigDragEvent = Signal(str)
    sceneMousePos = None

    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.setUi()

    def setUi(self):
        self.setMouseTracking(True)
        self.scale_ratio = 1.0
        self.setAcceptDrops(True)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setToolTipDuration(-1)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
        self.setTransformationAnchor(
            QGraphicsView.AnchorViewCenter)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)

    def mouseMoveEvent(self, event):
        self.sceneMousePos = self.mapToScene(event.pos())
        self.sigMouseMovePoint.emit(self.sceneMousePos)
        return super().mouseMoveEvent(event)

    def wheelEvent(self, event):
        angle = event.angleD.y()
        self.centerOn(self.sceneMousePos)
        if (angle > 0):
            self.scale(1.25, 1.25)
            self.scale_ratio *= 1.25
        else:
            self.scale(0.8, 0.8)
            self.scale_ratio *= 0.8
        self.sigWheelEvent.emit(self.scale_ratio)
        return super().wheelEvent(event)

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            try:
                for url in event.mimeData().urls():
                    self.sigDragEvent.emit(url.path()[1:])
            except Exception as e:
                print(e)


class VideoView(QLabel):
    sigDragEvent = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            try:
                for url in event.mimeData().urls():
                    self.sigDragEvent.emit(url.path()[1:])
            except Exception as e:
                print(e)


def sceneDisplayImage(scene: QGraphicsScene, img):
    """
    img: opencv的图像数据
    """
    scene.clear()
    if img is not None:
        # numpy转qimage的标准流程
        if len(img.shape) == 2:
            bytes_per_line = img.shape[1]
            qimg = QImage(img, img, img.shape[1],
                          img.shape[0], QImage.Format_Grayscale8)
        elif img.shape[2] == 3:
            bytes_per_line = 3 * img.shape[1]
            qimg = QImage(img, img.shape[1],
                          img.shape[0], bytes_per_line, QImage.Format_BGR888)
        elif img.shape[2] == 4:
            bytes_per_line = 4 * img.shape[1]
            qimg = QImage(img, img.shape[1],
                          img.shape[0], bytes_per_line, QImage.Format_RGBA8888)
        else:
            critical("图片格式不能解析")
        scene.addPixmap(QPixmap.fromImage(qimg))
        return True
    return False


def critical(string: str, parent=None):
    if(string is not None):
        QMessageBox.critical(
            parent, '警告', string, QMessageBox.Yes, QMessageBox.Yes)
    return


def info(string: str, parent=None):
    if(string is not None):
        QMessageBox.information(
            parent, '提示', string, QMessageBox.Yes, QMessageBox.Yes)
    return
