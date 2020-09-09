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
        HistgramView.resize(777, 482)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HistgramView.sizePolicy().hasHeightForWidth())
        HistgramView.setSizePolicy(sizePolicy)
        HistgramView.setSizeGripEnabled(True)
        self.gridLayout = QGridLayout(HistgramView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(HistgramView)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.snr_r = QDoubleSpinBox(self.groupBox_2)
        self.snr_r.setObjectName(u"snr_r")
        self.snr_r.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.snr_r.setMaximum(256.000000000000000)

        self.horizontalLayout_9.addWidget(self.snr_r)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.snr_g = QDoubleSpinBox(self.groupBox_2)
        self.snr_g.setObjectName(u"snr_g")
        self.snr_g.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.snr_g.setMaximum(256.000000000000000)

        self.horizontalLayout_10.addWidget(self.snr_g)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.snr_b = QDoubleSpinBox(self.groupBox_2)
        self.snr_b.setObjectName(u"snr_b")
        self.snr_b.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.snr_b.setMaximum(256.000000000000000)

        self.horizontalLayout_11.addWidget(self.snr_b)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.snr_y = QDoubleSpinBox(self.groupBox_2)
        self.snr_y.setObjectName(u"snr_y")
        self.snr_y.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.snr_y.setMaximum(256.000000000000000)

        self.horizontalLayout_12.addWidget(self.snr_y)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.snr_cr = QDoubleSpinBox(self.groupBox_2)
        self.snr_cr.setObjectName(u"snr_cr")
        self.snr_cr.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.snr_cr.setMaximum(256.000000000000000)

        self.horizontalLayout_13.addWidget(self.snr_cr)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.snr_cb = QDoubleSpinBox(self.groupBox_2)
        self.snr_cb.setObjectName(u"snr_cb")
        self.snr_cb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.snr_cb.setMaximum(256.000000000000000)

        self.horizontalLayout_14.addWidget(self.snr_cb)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)


        self.gridLayout_3.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_3.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.average_r = QDoubleSpinBox(self.groupBox_3)
        self.average_r.setObjectName(u"average_r")
        self.average_r.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.average_r.setMaximum(256.000000000000000)

        self.horizontalLayout.addWidget(self.average_r)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.average_g = QDoubleSpinBox(self.groupBox_3)
        self.average_g.setObjectName(u"average_g")
        self.average_g.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.average_g.setMaximum(256.000000000000000)

        self.horizontalLayout_2.addWidget(self.average_g)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.average_b = QDoubleSpinBox(self.groupBox_3)
        self.average_b.setObjectName(u"average_b")
        self.average_b.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.average_b.setMaximum(256.000000000000000)

        self.horizontalLayout_3.addWidget(self.average_b)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.average_y = QDoubleSpinBox(self.groupBox_3)
        self.average_y.setObjectName(u"average_y")
        self.average_y.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.average_y.setMaximum(256.000000000000000)

        self.horizontalLayout_4.addWidget(self.average_y)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.average_cr = QDoubleSpinBox(self.groupBox_3)
        self.average_cr.setObjectName(u"average_cr")
        self.average_cr.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.average_cr.setMaximum(256.000000000000000)

        self.horizontalLayout_5.addWidget(self.average_cr)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.average_cb = QDoubleSpinBox(self.groupBox_3)
        self.average_cb.setObjectName(u"average_cb")
        self.average_cb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.average_cb.setMaximum(256.000000000000000)

        self.horizontalLayout_6.addWidget(self.average_cb)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_18.addWidget(self.label_15)

        self.r_gain = QDoubleSpinBox(self.groupBox_4)
        self.r_gain.setObjectName(u"r_gain")
        self.r_gain.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.r_gain.setDecimals(3)

        self.horizontalLayout_18.addWidget(self.r_gain)


        self.verticalLayout_11.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_19.addWidget(self.label_16)

        self.g_gain = QDoubleSpinBox(self.groupBox_4)
        self.g_gain.setObjectName(u"g_gain")
        self.g_gain.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.g_gain.setDecimals(3)

        self.horizontalLayout_19.addWidget(self.g_gain)


        self.verticalLayout_11.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_20.addWidget(self.label_17)

        self.b_gain = QDoubleSpinBox(self.groupBox_4)
        self.b_gain.setObjectName(u"b_gain")
        self.b_gain.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.b_gain.setDecimals(3)

        self.horizontalLayout_20.addWidget(self.b_gain)


        self.verticalLayout_11.addLayout(self.horizontalLayout_20)


        self.gridLayout_6.addLayout(self.verticalLayout_11, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.rg_ratio = QDoubleSpinBox(self.groupBox_5)
        self.rg_ratio.setObjectName(u"rg_ratio")
        self.rg_ratio.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.rg_ratio.setDecimals(3)

        self.horizontalLayout_16.addWidget(self.rg_ratio)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_17.addWidget(self.label_14)

        self.bg_ratio = QDoubleSpinBox(self.groupBox_5)
        self.bg_ratio.setObjectName(u"bg_ratio")
        self.bg_ratio.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bg_ratio.setDecimals(3)

        self.horizontalLayout_17.addWidget(self.bg_ratio)


        self.verticalLayout_12.addLayout(self.horizontalLayout_17)


        self.gridLayout_5.addLayout(self.verticalLayout_12, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_5, 1, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_7, 2, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMaximumSize(QSize(16777215, 153))
        self.gridLayout_4 = QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_18 = QLabel(self.groupBox_6)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_8.addWidget(self.label_18, 0, 0, 1, 1)

        self.section_y = QSpinBox(self.groupBox_6)
        self.section_y.setObjectName(u"section_y")
        self.section_y.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.section_y.setMaximum(10000)

        self.gridLayout_8.addWidget(self.section_y, 1, 1, 1, 1)

        self.section_x = QSpinBox(self.groupBox_6)
        self.section_x.setObjectName(u"section_x")
        self.section_x.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.section_x.setMaximum(10000)

        self.gridLayout_8.addWidget(self.section_x, 0, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_6)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_8.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_20 = QLabel(self.groupBox_6)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_8.addWidget(self.label_20, 0, 2, 1, 1)

        self.section_width = QSpinBox(self.groupBox_6)
        self.section_width.setObjectName(u"section_width")
        self.section_width.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.section_width.setMaximum(10000)

        self.gridLayout_8.addWidget(self.section_width, 0, 3, 1, 1)

        self.label_21 = QLabel(self.groupBox_6)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_8.addWidget(self.label_21, 1, 2, 1, 1)

        self.section_height = QSpinBox(self.groupBox_6)
        self.section_height.setObjectName(u"section_height")
        self.section_height.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.section_height.setMaximum(10000)

        self.gridLayout_8.addWidget(self.section_height, 1, 3, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_8, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_6, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.groupBox_7 = QGroupBox(HistgramView)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(437, 0))
        self.gridLayout_10 = QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.widget = QWidget(self.groupBox_7)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(352, 0))

        self.gridLayout_10.addWidget(self.widget, 1, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.r_enable = QCheckBox(self.groupBox_7)
        self.r_enable.setObjectName(u"r_enable")
        self.r_enable.setMinimumSize(QSize(31, 0))
        self.r_enable.setMaximumSize(QSize(60, 16777215))
        self.r_enable.setChecked(True)

        self.verticalLayout.addWidget(self.r_enable)

        self.g_enable = QCheckBox(self.groupBox_7)
        self.g_enable.setObjectName(u"g_enable")
        self.g_enable.setMinimumSize(QSize(31, 0))
        self.g_enable.setMaximumSize(QSize(60, 16777215))
        self.g_enable.setChecked(True)

        self.verticalLayout.addWidget(self.g_enable)

        self.b_enable = QCheckBox(self.groupBox_7)
        self.b_enable.setObjectName(u"b_enable")
        self.b_enable.setMinimumSize(QSize(31, 0))
        self.b_enable.setMaximumSize(QSize(60, 16777215))
        self.b_enable.setChecked(True)

        self.verticalLayout.addWidget(self.b_enable)

        self.y_enable = QCheckBox(self.groupBox_7)
        self.y_enable.setObjectName(u"y_enable")
        self.y_enable.setMinimumSize(QSize(31, 0))
        self.y_enable.setMaximumSize(QSize(60, 16777215))
        self.y_enable.setChecked(True)

        self.verticalLayout.addWidget(self.y_enable)


        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.gridLayout_10.addLayout(self.verticalLayout_7, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_7, 0, 0, 1, 1)


        self.retranslateUi(HistgramView)

        QMetaObject.connectSlotsByName(HistgramView)
    # setupUi

    def retranslateUi(self, HistgramView):
        HistgramView.setWindowTitle(QCoreApplication.translate("HistgramView", u"\u7edf\u8ba1\u4fe1\u606f", None))
        self.groupBox.setTitle(QCoreApplication.translate("HistgramView", u"\u8be6\u7ec6\u4fe1\u606f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("HistgramView", u"\u4fe1\u566a\u6bd4(db)", None))
        self.label_7.setText(QCoreApplication.translate("HistgramView", u"R:", None))
        self.label_8.setText(QCoreApplication.translate("HistgramView", u"G:", None))
        self.label_9.setText(QCoreApplication.translate("HistgramView", u"B:", None))
        self.label_10.setText(QCoreApplication.translate("HistgramView", u"Y:", None))
        self.label_11.setText(QCoreApplication.translate("HistgramView", u"cr:", None))
        self.label_12.setText(QCoreApplication.translate("HistgramView", u"Cb:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("HistgramView", u"\u5e73\u5747\u503c", None))
        self.label.setText(QCoreApplication.translate("HistgramView", u"R:", None))
        self.label_2.setText(QCoreApplication.translate("HistgramView", u"G:", None))
        self.label_3.setText(QCoreApplication.translate("HistgramView", u"B:", None))
        self.label_4.setText(QCoreApplication.translate("HistgramView", u"Y:", None))
        self.label_5.setText(QCoreApplication.translate("HistgramView", u"cr:", None))
        self.label_6.setText(QCoreApplication.translate("HistgramView", u"Cb:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("HistgramView", u"\u767d\u5e73\u8861\u589e\u76ca", None))
        self.label_15.setText(QCoreApplication.translate("HistgramView", u"R:", None))
        self.label_16.setText(QCoreApplication.translate("HistgramView", u"G:", None))
        self.label_17.setText(QCoreApplication.translate("HistgramView", u"B:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("HistgramView", u"\u6bd4\u503c", None))
        self.label_13.setText(QCoreApplication.translate("HistgramView", u"R/G", None))
        self.label_14.setText(QCoreApplication.translate("HistgramView", u"B/G", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("HistgramView", u"\u9009\u533a\u5927\u5c0f", None))
        self.label_18.setText(QCoreApplication.translate("HistgramView", u"X:", None))
        self.label_19.setText(QCoreApplication.translate("HistgramView", u"Y:", None))
        self.label_20.setText(QCoreApplication.translate("HistgramView", u"\u5bbd", None))
        self.label_21.setText(QCoreApplication.translate("HistgramView", u"\u9ad8", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("HistgramView", u"\u76f4\u65b9\u56fe", None))
        self.r_enable.setText(QCoreApplication.translate("HistgramView", u"R", None))
        self.g_enable.setText(QCoreApplication.translate("HistgramView", u"G", None))
        self.b_enable.setText(QCoreApplication.translate("HistgramView", u"B", None))
        self.y_enable.setText(QCoreApplication.translate("HistgramView", u"Y", None))
    # retranslateUi

