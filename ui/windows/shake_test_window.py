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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.videoview = QLabel(self.centralwidget)
        self.videoview.setObjectName(u"videoview")
        self.videoview.setMinimumSize(QSize(441, 0))

        self.gridLayout.addWidget(self.videoview, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(48, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.videopath = QLineEdit(self.centralwidget)
        self.videopath.setObjectName(u"videopath")
        self.videopath.setMaximumSize(QSize(133, 16777215))

        self.horizontalLayout.addWidget(self.videopath)

        self.openvideo = QPushButton(self.centralwidget)
        self.openvideo.setObjectName(u"openvideo")
        self.openvideo.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.openvideo)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.isok = QPushButton(self.centralwidget)
        self.isok.setObjectName(u"isok")
        self.isok.setMaximumSize(QSize(131, 16777215))

        self.horizontalLayout_2.addWidget(self.isok)

        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMaximumSize(QSize(131, 16777215))

        self.horizontalLayout_2.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(270, 16777215))

        self.verticalLayout.addWidget(self.textBrowser)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

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
        self.videoview.setText("")
        self.label.setText(QCoreApplication.translate("ShakeTestWindow", u"\u89c6\u9891\u6587\u4ef6", None))
        self.openvideo.setText(QCoreApplication.translate("ShakeTestWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.isok.setText(QCoreApplication.translate("ShakeTestWindow", u"\u5f00\u59cb", None))
        self.cancel_button.setText(QCoreApplication.translate("ShakeTestWindow", u"\u505c\u6b62", None))
    # retranslateUi

