import sys
sys.path.append("..")
from tools.depth_of_focus.depth_of_focus import FieldDepthWindow
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    apps = QApplication([])
    apps.setStyle('Fusion')
    appswindow = FieldDepthWindow()
    appswindow.show()
    sys.exit(apps.exec_())
