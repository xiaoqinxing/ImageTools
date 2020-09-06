import cv2
from PySide2.QtWidgets import QMainWindow, QGraphicsScene, QMessageBox, QFileDialog
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Slot
from tools.imageeditor.imageeditor_window import Ui_ImageEditor
from ui.customwidget import ImageView
from tools.imageeditor.imageeffect import ImageEffect


class ImageEditor(object):
    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_ImageEditor()
        self.ui.setupUi(self.window)
        self.scene = QGraphicsScene()
        self.imageview = ImageView(self.scene, self.ui.graphicsView)
        # 由于graphicsView被自定义了，需要重新定义一下UI，gridlayout还需要重新加一下widget
        self.ui.gridLayout.addWidget(self.imageview, 0, 1, 3, 1)
        self.imageview.sigDragEvent.connect(self.__init_img)
        self.imageview.sigMouseMovePoint.connect(self.show_point_rgb)
        self.imageview.sigWheelEvent.connect(self.update_wheel_ratio)
        self.ui.openimage.triggered.connect(self.on_open_img)
        self.img = None
        self.scale_ratio = 100

    def show(self):
        self.window.show()

    def displayImage(self, img):
        self.scene.clear()
        self.scene.addPixmap(QPixmap(img))
        self.now_image = img

    def on_open_img(self):
        imagepath = QFileDialog.getOpenFileName(
            None, '打开图片', './', "Images (*.jpg *.png *.bmp)")
        self.__init_img(imagepath[0])

    def __init_img(self, filename):
        if (filename != ''):
            self.img = ImageEffect(filename)
            if (self.img.get_src_image() is not None):
                self.displayImage(self.img.get_src_image())
            else:
                rely = QMessageBox.critical(
                    self.window, '警告', '打开图片失败,', QMessageBox.Yes, QMessageBox.Yes)
                return

    def show_point_rgb(self, point):
        self.x = int(point.x())
        self.y = int(point.y())
        # print(str(x) + ' ' + str(y))
        if (self.img is not None):
            rgb = self.img.get_img_point(self.x, self.y)
            if (rgb is not None):
                self.rgb = rgb
                self.ui.statusBar.showMessage(
                    "x:{},y:{} : R:{} G:{} B:{} 缩放比例:{}%".format(self.x, self.y, self.rgb[0], self.rgb[1], self.rgb[2], self.scale_ratio))

    def update_wheel_ratio(self, ratio):
        self.scale_ratio = int(ratio * 100)
        self.ui.statusBar.showMessage(
            "x:{},y:{} : R:{} G:{} B:{} 缩放比例:{}%".format(self.x, self.y, self.rgb[0], self.rgb[1], self.rgb[2], self.scale_ratio))
