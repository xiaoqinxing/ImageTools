from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QDir


class HelpDoc(QWebEngineView):

    def __init__(self, name='HelpDoc', parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.name = name
        self.setWindowTitle('帮助手册')
        self.load(QDir.current().filePath("Readme.html"))
    
    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        try:
            self.parent.sub_windows.remove(self)
        except Exception:
            print('{}窗口关闭错误'.format(self.name))
        self.name = None
        event.accept()