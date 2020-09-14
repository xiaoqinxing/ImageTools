from ui.help_window import Ui_HelpWindow
from PySide2.QtWidgets import QMainWindow

class HelpDoc(object):

    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self.window)
        with open("Readme.md", "r", encoding="utf-8") as input_file:
            text = input_file.read()
        self.ui.textBrowser.setMarkdown(text)

    def show(self):
        self.window.show()