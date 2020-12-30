import sys
sys.path.append("..")
from tools.pqtools_to_code.pqtools_to_code import PQtoolsToCode
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    apps = QApplication([])
    apps.setStyle('Fusion')
    appswindow = PQtoolsToCode()
    appswindow.show()
    sys.exit(apps.exec_())
