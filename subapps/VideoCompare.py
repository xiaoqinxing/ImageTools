import sys
sys.path.append("..")
from tools.video_compare.videocompare import VideoCompare
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    apps = QApplication([])
    apps.setStyle('Fusion')
    appswindow = VideoCompare()
    appswindow.show()
    sys.exit(apps.exec())
