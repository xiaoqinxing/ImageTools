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
from components.check_update import CheckUpdate, simple_check_is_need_update
import components.logconfig as log
from logging import info
from components.property import get_persist, IS_NEED_AUTO_UPDATE


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
        self.ui.checkupdate.triggered.connect(self.add_checkupdate_window)
        info('ImageTools 工具初始化成功')

    def check_version(self):
        is_need_auto_update = get_persist(IS_NEED_AUTO_UPDATE, False)
        info('是否需要自动更新 {}'.format(is_need_auto_update))
        if is_need_auto_update is True:
            if(simple_check_is_need_update() == True):
                info('软件需要更新')
                self.add_checkupdate_window()
            else:
                info('软件不需要更新')

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
        info('打开镜头计算器工具 success')

    def add_shake_tool_window(self):
        self.add_sub_window("ShakeTestTool")
        info('打开图像防抖测试工具 sucess')

    def add_image_editor_window(self):
        self.add_sub_window("ImageEditor")
        info('打开图像查看工具 sucess')

    def add_userguide_window(self):
        self.add_sub_window("HelpDoc")
        info('打开帮助工具 sucess')

    def add_raw_image_editor_window(self):
        self.add_sub_window("RawImageEditor")
        info('打开RAW图编辑工具 sucess')

    def add_video_compare_window(self):
        self.add_sub_window("VideoCompare")
        info('打开视频对比工具 sucess')

    def add_pqtools2code_window(self):
        self.add_sub_window("PQtoolsToCode")
        info('打开pqtools转代码工具 sucess')

    def add_checkupdate_window(self):
        sub_win = CheckUpdate(parent=self)
        sub_win.show()

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
    appswindow.check_version()
    sys.exit(apps.exec_())
