from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QDir


class HelpDoc(QWebEngineView):

    def __init__(self, name='HelpDoc', parent=None):
        super().__init__()
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
        self.name = None
        try:
            self.parent.sub_windows.remove(self)
        except Exception:
            print('{}不支持记忆存储'.format(self.name))
        event.accept()