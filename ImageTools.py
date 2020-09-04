from PySide2.QtWidgets import QApplication, QMainWindow
from ui.windows.mainwindow import Ui_MainWindow
import sys
from ui.customwidget.customwidget import MainWindow
from tools.depth_of_focus.depth_of_focus import FieldDepthWindow
from tools.shake_test.shake_test import ShakeTestTool
from tools.imageeditor.imageeditor import ImageEditor


class ImageTools(object):
    def __init__(self):
        super().__init__()
        self.window = MainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.mdiArea.setStyleSheet("QTabBar::tab { height: 30px;}")
        self.ui.field_depth_tool.triggered.connect(
            self.add_field_depth_tool_window)
        self.ui.shake_tool.triggered.connect(self.add_shake_tool_window)
        self.ui.open_image.triggered.connect(self.add_image_editor_window)
        self.sub_window = None

    def add_field_depth_tool_window(self):
        self.sub_window = FieldDepthWindow()
        self.ui.mdiArea.addSubWindow(self.sub_window.window)
        self.sub_window.show()

    def add_shake_tool_window(self):
        self.sub_window = ShakeTestTool()
        self.ui.mdiArea.addSubWindow(self.sub_window.window)
        self.sub_window.show()
    
    def add_image_editor_window(self):
        self.sub_window = ImageEditor()
        self.ui.mdiArea.addSubWindow(self.sub_window.window)
        self.sub_window.show()


if __name__ == "__main__":
    apps = QApplication([])
    apps.setStyle('Fusion')
    appswindow = ImageTools()
    sys.exit(apps.exec_())
