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
        ShakeTestWindow.resize(1034, 653)
        self.centralwidget = QWidget(ShakeTestWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(16777215, 104))
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.cancel_button = QPushButton(self.groupBox_2)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.cancel_button, 2, 1, 1, 1)

        self.view_speed = QSlider(self.groupBox_2)
        self.view_speed.setObjectName(u"view_speed")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_speed.sizePolicy().hasHeightForWidth())
        self.view_speed.setSizePolicy(sizePolicy)
        self.view_speed.setSliderPosition(50)
        self.view_speed.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.view_speed, 0, 1, 1, 1)

        self.isok = QPushButton(self.groupBox_2)
        self.isok.setObjectName(u"isok")
        self.isok.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.isok, 2, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)

        self.restart = QPushButton(self.groupBox_2)
        self.restart.setObjectName(u"restart")

        self.gridLayout_6.addWidget(self.restart, 2, 2, 1, 1)

        self.speed_value = QDoubleSpinBox(self.groupBox_2)
        self.speed_value.setObjectName(u"speed_value")
        sizePolicy.setHeightForWidth(self.speed_value.sizePolicy().hasHeightForWidth())
        self.speed_value.setSizePolicy(sizePolicy)
        self.speed_value.setValue(1.000000000000000)

        self.gridLayout_6.addWidget(self.speed_value, 0, 2, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_6.addWidget(self.pushButton, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_6.addWidget(self.pushButton_2, 1, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_6, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)

        ShakeTestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ShakeTestWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1034, 23))
        ShakeTestWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ShakeTestWindow)
        self.statusbar.setObjectName(u"statusbar")
        ShakeTestWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ShakeTestWindow)

        QMetaObject.connectSlotsByName(ShakeTestWindow)
    # setupUi

    def retranslateUi(self, ShakeTestWindow):
        ShakeTestWindow.setWindowTitle(QCoreApplication.translate("ShakeTestWindow", u"\u89c6\u9891\u5bf9\u6bd4\u5de5\u5177", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ShakeTestWindow", u"\u8bbe\u7f6e", None))
        self.cancel_button.setText(QCoreApplication.translate("ShakeTestWindow", u"\u6682\u505c", None))
        self.isok.setText(QCoreApplication.translate("ShakeTestWindow", u"\u5f00\u59cb", None))
        self.label_6.setText(QCoreApplication.translate("ShakeTestWindow", u"\u64ad\u653e\u901f\u5ea6", None))
        self.restart.setText(QCoreApplication.translate("ShakeTestWindow", u"\u91cd\u65b0\u5f00\u59cb", None))
        self.label.setText(QCoreApplication.translate("ShakeTestWindow", u"\u64ad\u653e\u7a97\u53e3", None))
        self.pushButton.setText(QCoreApplication.translate("ShakeTestWindow", u"\u589e\u52a0", None))
        self.pushButton_2.setText(QCoreApplication.translate("ShakeTestWindow", u"\u51cf\u5c11", None))
    # retranslateUi

