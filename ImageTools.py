from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from ui.mainwindow import Ui_MainWindow
import sys
from ui.customwidget import MainWindow
from tools.depth_of_focus.depth_of_focus import FieldDepthWindow
from tools.shake_test.shake_test import ShakeTestTool
from tools.imageeditor.imageeditor import ImageEditor


class ImageTools(object):
    def __init__(self):
        super().__init__()
        self.window = MainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.subwindows_ui = self.ui.mdiArea
        self.subwindows_ui.setStyleSheet("QTabBar::tab { height: 30px;}")
        self.ui.field_depth_tool.triggered.connect(
            self.add_field_depth_tool_window)
        self.ui.shake_tool.triggered.connect(self.add_shake_tool_window)
        self.ui.imageeditor.triggered.connect(self.add_image_editor_window)
        self.window.show()
        self.sub_windows = list()

    def add_field_depth_tool_window(self):
        sub_window = FieldDepthWindow()
        self.subwindows_ui.addSubWindow(sub_window.window)
        sub_window.show()
        self.sub_windows.append(sub_window)

    def add_shake_tool_window(self):
        sub_window = ShakeTestTool()
        self.subwindows_ui.addSubWindow(sub_window.window)
        sub_window.show()
        self.sub_windows.append(sub_window)

    def add_image_editor_window(self):
        sub_window = ImageEditor()
        self.subwindows_ui.addSubWindow(sub_window.window)
        sub_window.show()
        self.sub_windows.append(sub_window)


if __name__ == "__main__":
    apps = QApplication([])
    apps.setStyle('Fusion')
    appswindow = ImageTools()
    sys.exit(apps.exec_())
