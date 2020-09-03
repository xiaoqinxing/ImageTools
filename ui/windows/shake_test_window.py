# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shake_test_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_ShakeTestWindow(object):
    def setupUi(self, ShakeTestWindow):
        if not ShakeTestWindow.objectName():
            ShakeTestWindow.setObjectName(u"ShakeTestWindow")
        ShakeTestWindow.resize(800, 600)
        self.centralwidget = QWidget(ShakeTestWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(510, 80, 270, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.videopath = QLineEdit(self.layoutWidget)
        self.videopath.setObjectName(u"videopath")

        self.horizontalLayout.addWidget(self.videopath)

        self.openvideo = QPushButton(self.layoutWidget)
        self.openvideo.setObjectName(u"openvideo")

        self.horizontalLayout.addWidget(self.openvideo)

        self.isok = QPushButton(self.centralwidget)
        self.isok.setObjectName(u"isok")
        self.isok.setGeometry(QRect(510, 130, 75, 23))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(510, 180, 256, 192))
        self.videoview = QLabel(self.centralwidget)
        self.videoview.setObjectName(u"videoview")
        self.videoview.setGeometry(QRect(30, 30, 441, 471))
        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(620, 130, 75, 23))
        ShakeTestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ShakeTestWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        ShakeTestWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ShakeTestWindow)
        self.statusbar.setObjectName(u"statusbar")
        ShakeTestWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ShakeTestWindow)

        QMetaObject.connectSlotsByName(ShakeTestWindow)
    # setupUi

    def retranslateUi(self, ShakeTestWindow):
        ShakeTestWindow.setWindowTitle(QCoreApplication.translate("ShakeTestWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("ShakeTestWindow", u"\u89c6\u9891\u6587\u4ef6", None))
        self.openvideo.setText(QCoreApplication.translate("ShakeTestWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.isok.setText(QCoreApplication.translate("ShakeTestWindow", u"\u786e\u8ba4", None))
        self.videoview.setText("")
        self.cancel_button.setText(QCoreApplication.translate("ShakeTestWindow", u"\u53d6\u6d88", None))
    # retranslateUi

