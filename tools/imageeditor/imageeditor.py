import cv2
from PySide2.QtWidgets import QMainWindow, QGraphicsScene, QMessageBox
from PySide2.QtGui import QImage, QPixmap
from tools.imageeditor.imageeditor_window import Ui_ImageEditor
from ui.customwidget import ImageView
from tools.imageeditor.imageeffect import ImageEffect


class ImageEditor(object):
    def __init__(self, imagepath):
        self.img = ImageEffect(imagepath)
        self.window = QMainWindow()
        self.ui = Ui_ImageEditor()
        self.ui.setupUi(self.window)

        self.scene = QGraphicsScene()
        self.imageview = ImageView(self.scene, self.ui.graphicsView)
        # self.ui.graphicsView.setScene(self.scene)
        if (self.img.get_src_image() is not None):
            self.displayImage(imagepath)
        else:
            rely = QMessageBox.critical(
                self.window, '警告', '打开图片失败,', QMessageBox.Yes, QMessageBox.Yes)
            return

    def show(self):
        self.window.show()

    def displayImage(self, img):
        self.scene.clear()
        self.scene.addPixmap(QPixmap(img))
        self.now_image = img
