from PySide2.QtWidgets import QMessageBox, QMainWindow, QProgressBar, QLabel
from components.ui.mainwindow import Ui_MainWindow
import pickle
import os

class MainWindow(QMainWindow):
    """对QMainWindow类重写，实现一些功能"""

    def __init__(self):
        super().__init__()
        self.sub_windows = list()
        self.filename = './config/ImageToolsSubWindows.txt'
        self.sub_windows_list = list()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
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
            if not os.path.exists("./config"):
                os.mkdir("./config")
            sub_windows_list = list()
            for win in self.sub_windows:
                if (win.name is not None):
                    sub_windows_list.append(win.name)
                    win.close()
            with open(self.filename, "wb") as fp:
                pickle.dump(sub_windows_list, fp)
            event.accept()
        else:
            event.ignore()


class SubWindow(QMainWindow):
    """对QMainWindow类重写，实现一些功能"""

    def __init__(self, name, parent, ui_view, need_processBar=False):
        super().__init__(parent)
        self.name = name
        self.filename = "./config/" + name + ".txt"
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
        if not os.path.exists("./config"):
            os.mkdir("./config")
        self.name = None
        with open(self.filename, "wb") as fp:
            pickle.dump(self.__saved_params, fp)
        event.accept()