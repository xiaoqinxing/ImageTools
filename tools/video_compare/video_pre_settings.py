# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_pre_settings.ui'
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


class Ui_video_pre_settings(object):
    def setupUi(self, video_pre_settings):
        if not video_pre_settings.objectName():
            video_pre_settings.setObjectName(u"video_pre_settings")
        video_pre_settings.resize(310, 220)
        video_pre_settings.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(video_pre_settings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(video_pre_settings)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.videoview = QHBoxLayout()
        self.videoview.setObjectName(u"videoview")

        self.gridLayout_3.addLayout(self.videoview, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(video_pre_settings)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 113))
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.path = QLineEdit(self.groupBox_2)
        self.path.setObjectName(u"path")
        self.path.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.path, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.skipframe = QSpinBox(self.groupBox_2)
        self.skipframe.setObjectName(u"skipframe")
        self.skipframe.setMaximumSize(QSize(16777215, 20))
        self.skipframe.setMaximum(10000)
        self.skipframe.setSingleStep(10)

        self.gridLayout.addWidget(self.skipframe, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.open_rtsp = QPushButton(self.groupBox_2)
        self.open_rtsp.setObjectName(u"open_rtsp")
        self.open_rtsp.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout.addWidget(self.open_rtsp)

        self.openvideo = QPushButton(self.groupBox_2)
        self.openvideo.setObjectName(u"openvideo")
        self.openvideo.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout.addWidget(self.openvideo)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(video_pre_settings)

        QMetaObject.connectSlotsByName(video_pre_settings)
    # setupUi

    def retranslateUi(self, video_pre_settings):
        video_pre_settings.setWindowTitle(QCoreApplication.translate("video_pre_settings", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("video_pre_settings", u"\u89c6\u9891\u9884\u89c8", None))
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("video_pre_settings", u"\u89c6\u9891\u8def\u5f84", None))
        self.label_2.setText(QCoreApplication.translate("video_pre_settings", u"\u8df3\u8fc7\u8fc7\u5e27\u6570", None))
        self.open_rtsp.setText(QCoreApplication.translate("video_pre_settings", u"\u6253\u5f00\u8bbe\u5907", None))
        self.openvideo.setText(QCoreApplication.translate("video_pre_settings", u"\u6253\u5f00\u6587\u4ef6", None))
    # retranslateUi

