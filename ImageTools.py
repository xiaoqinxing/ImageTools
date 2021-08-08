from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt
import sys
from components.window import MainWindow
from components.customwidget import info
from tools.depth_of_focus.depth_of_focus import FieldDepthWindow
from tools.shake_test.shake_test import ShakeTestTool
from tools.imageeditor.imageeditor import ImageEditor
from components.help_doc import HelpDoc
from tools.rawimageeditor.RawImageEditor import RawImageEditor
from tools.video_compare.videocompare import VideoCompare
from tools.pqtools_to_code.pqtools_to_code import PQtoolsToCode
import components.logconfig as log


class ImageTools(MainWindow):
    subwindow_function = {
        "FieldDepthWindow": FieldDepthWindow,
        "ShakeTestTool": ShakeTestTool,
        "ImageEditor": ImageEditor,
        "RawImageEditor": RawImageEditor,
        "VideoCompare": VideoCompare,
        "HelpDoc": HelpDoc,
        "PQtoolsToCode": PQtoolsToCode
    }

    def __init__(self):
        super().__init__()
        self.subwindows_ui = self.ui.mdiArea
        self.subwindows_ui.setStyleSheet("QTabBar::tab { height: 30px;}")
        self.ui.field_depth_tool.triggered.connect(
            self.add_field_depth_tool_window)
        self.ui.shake_tool.triggered.connect(self.add_shake_tool_window)
        self.ui.imageeditor.triggered.connect(self.add_image_editor_window)
        self.ui.userguide.triggered.connect(self.add_userguide_window)
        self.ui.rawimageeditor.triggered.connect(
            self.add_raw_image_editor_window)
        self.ui.video_compare.triggered.connect(self.add_video_compare_window)
        self.ui.pqtools2code.triggered.connect(self.add_pqtools2code_window)
        self.ui.clearcache.triggered.connect(self.clear_cache)

    def load_saved_windows(self):
        for name in self.sub_windows_list:
            self.add_sub_window(name)

    def add_sub_window(self, sub_window_name):
        sub_window = self.subwindow_function[sub_window_name](parent=self)
        self.subwindows_ui.addSubWindow(sub_window)
        self.sub_windows.append(sub_window)
        sub_window.show()

    def add_field_depth_tool_window(self):
        self.add_sub_window("FieldDepthWindow")

    def add_shake_tool_window(self):
        self.add_sub_window("ShakeTestTool")

    def add_image_editor_window(self):
        self.add_sub_window("ImageEditor")

    def add_userguide_window(self):
        self.add_sub_window("HelpDoc")

    def add_raw_image_editor_window(self):
        self.add_sub_window("RawImageEditor")

    def add_video_compare_window(self):
        self.add_sub_window("VideoCompare")

    def add_pqtools2code_window(self):
        self.add_sub_window("PQtoolsToCode")

    def clear_cache(self):
        self.need_clear_cache = True
        info('缓存删除成功！\r\n请重启软件', self)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    apps = QApplication([])
    apps.setStyle('Fusion')
    log.clean_old_log()
    log.init_log()
    appswindow = ImageTools()
    appswindow.show()
    appswindow.load_saved_windows()
    sys.exit(apps.exec_())
