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
        # self.ui.graphicsView.setScene(self.scene)
        self.imageview.sigDragEvent.connect(self.__init_img)
        self.ui.openimage.triggered.connect(self.on_open_img)

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
