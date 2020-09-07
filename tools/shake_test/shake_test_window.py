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
        ShakeTestWindow.resize(758, 858)
        self.centralwidget = QWidget(ShakeTestWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(270, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(48, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.videopath = QLineEdit(self.groupBox_2)
        self.videopath.setObjectName(u"videopath")
        self.videopath.setMaximumSize(QSize(133, 16777215))

        self.horizontalLayout.addWidget(self.videopath)

        self.openvideo = QPushButton(self.groupBox_2)
        self.openvideo.setObjectName(u"openvideo")
        self.openvideo.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.openvideo)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(270, 16777215))
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.warp_ratio = QDoubleSpinBox(self.groupBox_3)
        self.warp_ratio.setObjectName(u"warp_ratio")
        self.warp_ratio.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.warp_ratio.setDecimals(4)
        self.warp_ratio.setMaximum(10.000000000000000)

        self.horizontalLayout_5.addWidget(self.warp_ratio)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.center_max_x_distance = QDoubleSpinBox(self.groupBox_3)
        self.center_max_x_distance.setObjectName(u"center_max_x_distance")
        self.center_max_x_distance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.center_max_x_distance.setDecimals(4)
        self.center_max_x_distance.setMaximum(1000.000000000000000)

        self.horizontalLayout_4.addWidget(self.center_max_x_distance)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.center_max_y_distance = QDoubleSpinBox(self.groupBox_3)
        self.center_max_y_distance.setObjectName(u"center_max_y_distance")
        self.center_max_y_distance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.center_max_y_distance.setDecimals(4)
        self.center_max_y_distance.setMaximum(1000.000000000000000)

        self.horizontalLayout_6.addWidget(self.center_max_y_distance)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(271, 16777215))
        self.groupBox_4.setFlat(True)
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.isok = QPushButton(self.groupBox_4)
        self.isok.setObjectName(u"isok")
        self.isok.setMaximumSize(QSize(121, 16777215))

        self.horizontalLayout_2.addWidget(self.isok)

        self.cancel_button = QPushButton(self.groupBox_4)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMaximumSize(QSize(121, 16777215))

        self.horizontalLayout_2.addWidget(self.cancel_button)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.videoview = QLabel(self.groupBox)
        self.videoview.setObjectName(u"videoview")
        self.videoview.setMinimumSize(QSize(441, 0))

        self.gridLayout_2.addWidget(self.videoview, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        ShakeTestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ShakeTestWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 758, 23))
        ShakeTestWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ShakeTestWindow)
        self.statusbar.setObjectName(u"statusbar")
        ShakeTestWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ShakeTestWindow)

        QMetaObject.connectSlotsByName(ShakeTestWindow)
    # setupUi

    def retranslateUi(self, ShakeTestWindow):
        ShakeTestWindow.setWindowTitle(QCoreApplication.translate("ShakeTestWindow", u"\u9632\u6296\u6d4b\u8bd5\u5de5\u5177", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ShakeTestWindow", u"\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("ShakeTestWindow", u"\u89c6\u9891\u6587\u4ef6", None))
        self.openvideo.setText(QCoreApplication.translate("ShakeTestWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ShakeTestWindow", u"\u7ed3\u679c", None))
        self.label_3.setText(QCoreApplication.translate("ShakeTestWindow", u"\u56fe\u7247\u6700\u5927\u53d8\u5f62\u7a0b\u5ea6", None))
        self.label_2.setText(QCoreApplication.translate("ShakeTestWindow", u"\u4e2d\u5fc3\u70b9\u6700\u5927\u6a2a\u5411\u4f4d\u79fb", None))
        self.label_4.setText(QCoreApplication.translate("ShakeTestWindow", u"\u4e2d\u5fc3\u70b9\u6700\u5927\u7eb5\u5411\u4f4d\u79fb", None))
        self.groupBox_4.setTitle("")
        self.isok.setText(QCoreApplication.translate("ShakeTestWindow", u"\u5f00\u59cb", None))
        self.cancel_button.setText(QCoreApplication.translate("ShakeTestWindow", u"\u505c\u6b62", None))
        self.groupBox.setTitle(QCoreApplication.translate("ShakeTestWindow", u"\u89c6\u9891\u9884\u89c8", None))
        self.videoview.setText("")
    # retranslateUi

