from PySide2.QtWidgets import QDialog
from PySide2.QtGui import Qt
from PySide2.QtCore import Signal
from .ui.yuvconfig import Ui_YUVConfig


class YUVConfig(QDialog):
    height = 2160
    width = 3840
    yuv_format = 'NV21'
    need_saveimg_in_rotate = True
    configUpdateEvent = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_YUVConfig()
        self.ui.setupUi(self)
        self.ui.buttonBox.clicked.connect(self.get)

    def set(self):
        self.ui.width.setValue(self.width)
        self.ui.height.setValue(self.height)
        index = self.ui.yuvformat.findText(self.yuv_format)
        self.ui.yuvformat.setCurrentIndex(index)
        self.ui.saveimg_in_rotate.setCheckState(
            Qt.Checked if self.need_saveimg_in_rotate else Qt.Unchecked)

    def get(self):
        self.height = self.ui.height.value()
        self.width = self.ui.width.value()
        self.yuv_format = self.ui.yuvformat.currentText()
        self.need_saveimg_in_rotate = (
            self.ui.saveimg_in_rotate.checkState() == Qt.Checked)
        self.configUpdateEvent.emit()
