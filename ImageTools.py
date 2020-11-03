from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt
from ui.mainwindow import Ui_MainWindow
import sys
from ui.customwidget import MainWindow
from tools.depth_of_focus.depth_of_focus import FieldDepthWindow
from tools.shake_test.shake_test import ShakeTestTool
from tools.imageeditor.imageeditor import ImageEditor
from tools.af_calc.af_calc import AfCalcTool
from ui.help_doc import HelpDoc
from tools.rawimageeditor.rawimageeditor import RawImageEditor
from tools.video_compare.videocompare import VideoCompare


class ImageTools(object):
    subwindow_function = {
        "FieldDepthWindow": FieldDepthWindow,
        "ShakeTestTool": ShakeTestTool,
        "ImageEditor": ImageEditor,
        "AfCalcTool": AfCalcTool,
        "RawImageEditor": RawImageEditor,
        "VideoCompare": VideoCompare,
        "HelpDoc": HelpDoc,
    }

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
        self.ui.af_calc_tool.triggered.connect(self.add_af_calc_window)
        self.ui.userguide.triggered.connect(self.add_userguide_window)
        self.ui.rawimageeditor.triggered.connect(
            self.add_raw_image_editor_window)
        self.ui.video_compare.triggered.connect(self.add_video_compare_window)
        self.window.show()
        for name in self.window.sub_windows_list:
            self.add_sub_window(name)

    def add_sub_window(self, sub_window_name):
        sub_window = self.subwindow_function[sub_window_name]()
        self.subwindows_ui.addSubWindow(sub_window.window)
        sub_window.show()
        self.window.sub_windows.append(sub_window)

    def add_field_depth_tool_window(self):
        sub_window_name = 'FieldDepthWindow'
        self.add_sub_window(sub_window_name)

    def add_shake_tool_window(self):
        sub_window_name = "ShakeTestTool"
        self.add_sub_window(sub_window_name)

    def add_image_editor_window(self):
        sub_window_name = "ImageEditor"
        self.add_sub_window(sub_window_name)

    def add_af_calc_window(self):
        sub_window_name = "AfCalcTool"
        self.add_sub_window(sub_window_name)

    def add_userguide_window(self):
        sub_window_name = "HelpDoc"
        self.add_sub_window(sub_window_name)

    def add_raw_image_editor_window(self):
        sub_window_name = "RawImageEditor"
        self.add_sub_window(sub_window_name)

    def add_video_compare_window(self):
        sub_window_name = "VideoCompare"
        self.add_sub_window(sub_window_name)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    apps = QApplication([])
    apps.setStyle('Fusion')
    appswindow = ImageTools()
    sys.exit(apps.exec_())
