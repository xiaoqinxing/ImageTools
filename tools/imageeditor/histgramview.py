# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'histgramview.ui'
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


class Ui_HistgramView(object):
    def setupUi(self, HistgramView):
        if not HistgramView.objectName():
            HistgramView.setObjectName(u"HistgramView")
        HistgramView.resize(531, 385)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HistgramView.sizePolicy().hasHeightForWidth())
        HistgramView.setSizePolicy(sizePolicy)
        HistgramView.setSizeGripEnabled(True)
        self.gridLayout = QGridLayout(HistgramView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(HistgramView)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(381, 0))

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.r_enable = QCheckBox(HistgramView)
        self.r_enable.setObjectName(u"r_enable")
        self.r_enable.setMaximumSize(QSize(60, 16777215))
        self.r_enable.setChecked(True)

        self.verticalLayout.addWidget(self.r_enable)

        self.g_enable = QCheckBox(HistgramView)
        self.g_enable.setObjectName(u"g_enable")
        self.g_enable.setMaximumSize(QSize(60, 16777215))
        self.g_enable.setChecked(True)

        self.verticalLayout.addWidget(self.g_enable)

        self.b_enable = QCheckBox(HistgramView)
        self.b_enable.setObjectName(u"b_enable")
        self.b_enable.setMaximumSize(QSize(60, 16777215))
        self.b_enable.setChecked(True)

        self.verticalLayout.addWidget(self.b_enable)

        self.y_enable = QCheckBox(HistgramView)
        self.y_enable.setObjectName(u"y_enable")
        self.y_enable.setMaximumSize(QSize(60, 16777215))
        self.y_enable.setChecked(True)

        self.verticalLayout.addWidget(self.y_enable)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.retranslateUi(HistgramView)

        QMetaObject.connectSlotsByName(HistgramView)
    # setupUi

    def retranslateUi(self, HistgramView):
        HistgramView.setWindowTitle(QCoreApplication.translate("HistgramView", u"\u76f4\u65b9\u56fe", None))
        self.r_enable.setText(QCoreApplication.translate("HistgramView", u"R", None))
        self.g_enable.setText(QCoreApplication.translate("HistgramView", u"G", None))
        self.b_enable.setText(QCoreApplication.translate("HistgramView", u"B", None))
        self.y_enable.setText(QCoreApplication.translate("HistgramView", u"Y", None))
    # retranslateUi

