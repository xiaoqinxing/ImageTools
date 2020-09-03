from PySide2.QtWidgets import QApplication, QMainWindow
from ui.windows.mainwindow import Ui_MainWindow
import sys
from ui.customwidget.customwidget import MainWindow
from tools.depth_of_focus.depth_of_focus import FieldDepthWindow

class ImageTools(object):
    def __init__(self):
        super().__init__()
        self.window = MainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.field_depth_tool.triggered.connect(self.add_field_depth_tool_window)
        self.sub_window = None

    def add_field_depth_tool_window(self):
        self.sub_window = FieldDepthWindow()
        self.ui.mdiArea.addSubWindow(self.sub_window.get_window())
        self.sub_window.show()

if __name__ == "__main__":
    apps = QApplication([])
    apps.setStyle('Fusion')
    appswindow = ImageTools()
    sys.exit(apps.exec_())