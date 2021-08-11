from PySide2.QtWidgets import QMessageBox, QMainWindow, QProgressBar, QLabel
from components.ui.mainwindow import Ui_MainWindow
import pickle
import os

CACHE_FILEPATH = './config'


class MainWindow(QMainWindow):
    """对QMainWindow类重写，实现一些功能"""

    def __init__(self):
        super().__init__()
        self.sub_windows = list()
        self.filename = './config/ImageToolsSubWindows.tmp'
        self.sub_windows_list = list()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.need_clear_cache = False
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as fp:
                self.sub_windows_list = pickle.load(fp)

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QMessageBox.question(self,
                                     'ImageTools',
                                     "是否要退出程序？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            if self.need_clear_cache == False:
                if not os.path.exists(CACHE_FILEPATH):
                    os.mkdir(CACHE_FILEPATH)
                sub_windows_list = list()
                while len(self.sub_windows) > 0:
                    if (self.sub_windows[0].name is not None):
                        sub_windows_list.append(self.sub_windows[0].name)
                        self.sub_windows[0].close()
                with open(self.filename, "wb") as fp:
                    pickle.dump(sub_windows_list, fp)
            else:
                # 清楚缓存
                if os.path.exists(CACHE_FILEPATH):
                    for files in os.listdir(CACHE_FILEPATH):
                        filepath = os.path.join(CACHE_FILEPATH, files)
                        if os.path.isfile(filepath):
                            os.remove(filepath)
            event.accept()
        else:
            event.ignore()


class SubWindow(QMainWindow):
    """对QMainWindow类重写，实现一些功能"""

    def __init__(self, name, parent, ui_view, need_processBar=False):
        super().__init__(parent)
        self.parent = parent
        self.name = name
        self.filename = "./config/" + name + ".tmp"
        self.__saved_params = None
        self.ui = ui_view
        self.ui.setupUi(self)
        # add 进度条和详细信息显示 需要在ui里面加入statusBar
        if(need_processBar == True):
            self.progress_bar = QProgressBar()
            self.info_bar = QLabel()
            self.time_bar = QLabel()
            self.ui.statusBar.addPermanentWidget(self.info_bar, stretch=8)
            self.ui.statusBar.addPermanentWidget(self.time_bar, stretch=1)
            self.ui.statusBar.addPermanentWidget(self.progress_bar, stretch=2)
            self.progress_bar.setRange(0, 100)  # 设置进度条的范围
            self.progress_bar.setValue(0)

    def load_params(self, init_value):
        """
        加载存储的类，返回的参数可以直接进行修改，会保存到本地，下一次打开会自动加载
        """
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as fp:
                self.__saved_params = pickle.load(fp)
        if (self.__saved_params is None):
            self.__saved_params = init_value
        return self.__saved_params

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        if not os.path.exists(CACHE_FILEPATH):
            os.mkdir(CACHE_FILEPATH)
        self.name = None
        with open(self.filename, "wb") as fp:
            pickle.dump(self.__saved_params, fp)
        try:
            self.parent.sub_windows.remove(self)
        except Exception:
            print('{}工具不支持记忆存储'.format(self.name))
        event.accept()
