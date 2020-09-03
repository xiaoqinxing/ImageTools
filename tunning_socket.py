from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QHeaderView, QMessageBox
import socket
from threading import Thread
import time
class MainWindow(QMainWindow):
    """对QMainWindow类重写，实现一些功能"""
    def __init__(self):
        super().__init__()
        self.preview_socket_thread_running = True
        Thread(target=self.preview_socket_routine).start()

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        print("test")
        reply = QMessageBox.question(self,
                                     '本程序',
                                     "是否要退出程序？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.preview_socket_thread_running = False
            event.accept()
        else:
            event.ignore()

    def preview_socket_routine(self):
        preview_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
        host = socket.gethostname() # 获取本地主机名
        port = 12345                # 设置端口号
        send_buf = "hello\n"
        # try:
        preview_socket.connect(("localhost",port))
        # except:
        #     preview_socket.close()
        #     print("socket connect error")
        while True:
            preview_socket.sendall(send_buf.encode())
            try:
                a = preview_socket.recv(10)
                print(a.decode())
            except:
                print("socket recv error")
                break
            if(self.preview_socket_thread_running == False):
                break
            time.sleep(5)
        preview_socket.close()