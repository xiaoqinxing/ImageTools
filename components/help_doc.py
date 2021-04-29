from components.ui.help_window import Ui_HelpWindow
from components.window import SubWindow


class HelpDoc(SubWindow):

    def __init__(self, name='HelpDoc', parent=None):
        super().__init__(name, parent, Ui_HelpWindow())
        self.ui.textBrowser.setSource("Readme.md")