import sys
sys.path.append("..")
from tools.shake_test.shake_test import ShakeTestTool
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    apps = QApplication([])
    apps.setStyle('Fusion')
    appswindow = ShakeTestTool()
    appswindow.show()
    sys.exit(apps.exec_())
