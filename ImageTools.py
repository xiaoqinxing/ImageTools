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
from tools.yuv_viewer.yuv_viewer import YUVViewer
from components.check_update import CheckUpdate, simple_check_is_need_update
import components.logconfig as log
from logging import info
from components.property import get_persist, IS_NEED_AUTO_UPDATE


class ImageTools(MainWindow):
    def __init__(self):
        super().__init__()
        self.subwindow_function = {
            "FieldDepthWindow": [self.ui.field_depth_tool, FieldDepthWindow],
            "ShakeTestTool": [self.ui.shake_tool, ShakeTestTool],
            "ImageEditor": [self.ui.imageeditor, ImageEditor],
            "RawImageEditor": [self.ui.rawimageeditor, RawImageEditor],
            "VideoCompare": [self.ui.video_compare, VideoCompare],
            "HelpDoc": [self.ui.userguide, HelpDoc],
            "PQtoolsToCode": [self.ui.pqtools2code, PQtoolsToCode],
            "YUVViewer": [self.ui.yuv_viewer, YUVViewer],
        }
        self.subwindows_ui = self.ui.mdiArea
        self.subwindows_ui.setStyleSheet("QTabBar::tab { height: 30px;}")
        self.ui.clearcache.triggered.connect(self.clear_cache)
        self.ui.checkupdate.triggered.connect(self.add_checkupdate_window)
        for (key, value) in self.subwindow_function.items():
            # 注意，这个lambda表达式必须要先赋值才能使用，否则connect的永远是最后的一个类
            value[0].triggered.connect(
                lambda win_name=key, win_object=value[1]: self.add_sub_window(win_name, win_object))

        info('ImageTools 工具初始化成功')

    def add_sub_window(self, name, win_object):
        sub_window = win_object(parent=self)
        self.subwindows_ui.addSubWindow(sub_window)
        self.sub_windows.append(sub_window)
        sub_window.show()
        info('打开{}工具 success'.format(name))

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
            self.add_sub_window(name, self.subwindow_function[name][1])

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
