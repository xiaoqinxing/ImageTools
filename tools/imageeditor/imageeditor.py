import cv2
from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QImage, QPixmap
from ui.windows.imageeditor import Ui_ImageEditor

class ImageEditor(object):
    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_ImageEditor()
        self.ui.setupUi(self.window)

    def show(self):
        self.window.show()
