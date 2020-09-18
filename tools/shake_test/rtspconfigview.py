# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rtspconfigview.ui'
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


class Ui_RtspConfigView(object):
    def setupUi(self, RtspConfigView):
        if not RtspConfigView.objectName():
            RtspConfigView.setObjectName(u"RtspConfigView")
        RtspConfigView.resize(174, 186)
        self.gridLayout = QGridLayout(RtspConfigView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(RtspConfigView)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.username = QLineEdit(RtspConfigView)
        self.username.setObjectName(u"username")

        self.gridLayout_2.addWidget(self.username, 0, 1, 1, 1)

        self.label_2 = QLabel(RtspConfigView)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(RtspConfigView)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.port = QLineEdit(RtspConfigView)
        self.port.setObjectName(u"port")

        self.gridLayout_2.addWidget(self.port, 3, 1, 1, 1)

        self.ip = QLineEdit(RtspConfigView)
        self.ip.setObjectName(u"ip")

        self.gridLayout_2.addWidget(self.ip, 2, 1, 1, 1)

        self.label_4 = QLabel(RtspConfigView)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.password = QLineEdit(RtspConfigView)
        self.password.setObjectName(u"password")

        self.gridLayout_2.addWidget(self.password, 1, 1, 1, 1)

        self.label = QLabel(RtspConfigView)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.isphoto = QCheckBox(RtspConfigView)
        self.isphoto.setObjectName(u"isphoto")
        self.isphoto.setChecked(True)

        self.gridLayout_2.addWidget(self.isphoto, 4, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(RtspConfigView)
        self.buttonBox.accepted.connect(RtspConfigView.accept)
        self.buttonBox.rejected.connect(RtspConfigView.reject)

        QMetaObject.connectSlotsByName(RtspConfigView)
    # setupUi

    def retranslateUi(self, RtspConfigView):
        RtspConfigView.setWindowTitle(QCoreApplication.translate("RtspConfigView", u"\u6253\u5f00\u8bbe\u5907(RTSP)", None))
        self.username.setText(QCoreApplication.translate("RtspConfigView", u"admin", None))
        self.label_2.setText(QCoreApplication.translate("RtspConfigView", u"\u5bc6\u7801", None))
        self.label_3.setText(QCoreApplication.translate("RtspConfigView", u"IP", None))
        self.port.setText(QCoreApplication.translate("RtspConfigView", u"1554", None))
        self.ip.setText(QCoreApplication.translate("RtspConfigView", u"127.0.0.1", None))
        self.label_4.setText(QCoreApplication.translate("RtspConfigView", u"\u7aef\u53e3", None))
        self.password.setText(QCoreApplication.translate("RtspConfigView", u"admin123", None))
        self.label.setText(QCoreApplication.translate("RtspConfigView", u"\u7528\u6237\u540d", None))
        self.isphoto.setText(QCoreApplication.translate("RtspConfigView", u"\u79fb\u52a8\u8bbe\u5907", None))
    # retranslateUi

