# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'af_calc_ui.ui'
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


class Ui_AFCalcToolView(object):
    def setupUi(self, AFCalcToolView):
        if not AFCalcToolView.objectName():
            AFCalcToolView.setObjectName(u"AFCalcToolView")
        AFCalcToolView.resize(800, 600)
        self.centralwidget = QWidget(AFCalcToolView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(461, 0))
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.plotview = QGridLayout()
        self.plotview.setObjectName(u"plotview")

        self.gridLayout_5.addLayout(self.plotview, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(275, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)

        self.zoom_ratio = QLineEdit(self.groupBox)
        self.zoom_ratio.setObjectName(u"zoom_ratio")

        self.gridLayout.addWidget(self.zoom_ratio, 5, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 12, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)

        self.focus_num = QSpinBox(self.groupBox)
        self.focus_num.setObjectName(u"focus_num")
        self.focus_num.setMaximum(10000)
        self.focus_num.setSingleStep(1)
        self.focus_num.setValue(5)

        self.gridLayout.addWidget(self.focus_num, 3, 1, 1, 1)

        self.focus_nums = QLineEdit(self.groupBox)
        self.focus_nums.setObjectName(u"focus_nums")

        self.gridLayout.addWidget(self.focus_nums, 8, 1, 1, 1)

        self.tele_pianyi = QSpinBox(self.groupBox)
        self.tele_pianyi.setObjectName(u"tele_pianyi")
        self.tele_pianyi.setMaximum(10000)
        self.tele_pianyi.setSingleStep(1)
        self.tele_pianyi.setValue(97)

        self.gridLayout.addWidget(self.tele_pianyi, 6, 1, 1, 1)

        self.end_num = QSpinBox(self.groupBox)
        self.end_num.setObjectName(u"end_num")
        self.end_num.setMaximum(100000)
        self.end_num.setValue(982)

        self.gridLayout.addWidget(self.end_num, 10, 1, 1, 1)

        self.zoom_num = QSpinBox(self.groupBox)
        self.zoom_num.setObjectName(u"zoom_num")
        self.zoom_num.setMaximum(10000)
        self.zoom_num.setSingleStep(1)
        self.zoom_num.setValue(3)

        self.gridLayout.addWidget(self.zoom_num, 2, 1, 1, 1)

        self.num_inter = QSpinBox(self.groupBox)
        self.num_inter.setObjectName(u"num_inter")
        self.num_inter.setMaximum(10000)
        self.num_inter.setValue(4)

        self.gridLayout.addWidget(self.num_inter, 11, 1, 1, 1)

        self.zoom_range = QSpinBox(self.groupBox)
        self.zoom_range.setObjectName(u"zoom_range")
        self.zoom_range.setMaximum(10000)
        self.zoom_range.setSingleStep(1)
        self.zoom_range.setValue(971)

        self.gridLayout.addWidget(self.zoom_range, 4, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.open_in_path = QPushButton(self.groupBox)
        self.open_in_path.setObjectName(u"open_in_path")

        self.gridLayout.addWidget(self.open_in_path, 0, 1, 1, 1)

        self.sheetname = QLineEdit(self.groupBox)
        self.sheetname.setObjectName(u"sheetname")

        self.gridLayout.addWidget(self.sheetname, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.open_out_path = QPushButton(self.groupBox)
        self.open_out_path.setObjectName(u"open_out_path")

        self.gridLayout.addWidget(self.open_out_path, 12, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.start_num = QSpinBox(self.groupBox)
        self.start_num.setObjectName(u"start_num")
        self.start_num.setMaximum(10000)
        self.start_num.setValue(11)

        self.gridLayout.addWidget(self.start_num, 9, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)

        self.focus_ratio = QLineEdit(self.groupBox)
        self.focus_ratio.setObjectName(u"focus_ratio")

        self.gridLayout.addWidget(self.focus_ratio, 7, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.okbutton = QPushButton(self.centralwidget)
        self.okbutton.setObjectName(u"okbutton")
        self.okbutton.setMaximumSize(QSize(275, 16777215))

        self.verticalLayout.addWidget(self.okbutton)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)

        AFCalcToolView.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AFCalcToolView)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        AFCalcToolView.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AFCalcToolView)
        self.statusbar.setObjectName(u"statusbar")
        AFCalcToolView.setStatusBar(self.statusbar)

        self.retranslateUi(AFCalcToolView)

        QMetaObject.connectSlotsByName(AFCalcToolView)
    # setupUi

    def retranslateUi(self, AFCalcToolView):
        AFCalcToolView.setWindowTitle(QCoreApplication.translate("AFCalcToolView", u"AF\u955c\u5934\u66f2\u7ebf\u8ba1\u7b97", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AFCalcToolView", u"\u56fe\u8868", None))
        self.groupBox.setTitle(QCoreApplication.translate("AFCalcToolView", u"\u8bbe\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("AFCalcToolView", u"Zoom\u6bd4\u4f8b\u7cfb\u6570", None))
        self.label_7.setText(QCoreApplication.translate("AFCalcToolView", u"\u6570\u636e\u8d77\u59cb\u884c\u53f7", None))
        self.label_4.setText(QCoreApplication.translate("AFCalcToolView", u"Zoom\u8303\u56f4", None))
        self.label_3.setText(QCoreApplication.translate("AFCalcToolView", u"\u65e0\u7a77\u8fdc\u5904focus\u5217\u53f7", None))
        self.label_9.setText(QCoreApplication.translate("AFCalcToolView", u"\u6570\u636e\u95f4\u9694", None))
        self.label_12.setText(QCoreApplication.translate("AFCalcToolView", u"tele\u7aefFocus\u504f\u79fb", None))
        self.zoom_ratio.setText(QCoreApplication.translate("AFCalcToolView", u"4", None))
        self.label_10.setText(QCoreApplication.translate("AFCalcToolView", u"\u8f93\u51fa\u6587\u4ef6\u8def\u5f84", None))
        self.label_6.setText(QCoreApplication.translate("AFCalcToolView", u"\u6240\u6709\u5f85\u8ba1\u7b97Focus\u5217\u53f7", None))
        self.focus_nums.setText(QCoreApplication.translate("AFCalcToolView", u"5,9,11,13,14,15", None))
        self.label_8.setText(QCoreApplication.translate("AFCalcToolView", u"\u6570\u636e\u7ed3\u675f\u884c\u53f7", None))
        self.label.setText(QCoreApplication.translate("AFCalcToolView", u"sheet\u540d\u79f0", None))
        self.open_in_path.setText(QCoreApplication.translate("AFCalcToolView", u"\u6253\u5f00\u6587\u4ef6", None))
        self.sheetname.setText(QCoreApplication.translate("AFCalcToolView", u"VIS", None))
        self.label_2.setText(QCoreApplication.translate("AFCalcToolView", u"Zoom\u5217\u53f7", None))
        self.open_out_path.setText(QCoreApplication.translate("AFCalcToolView", u"\u6253\u5f00\u8f93\u51fa\u8def\u5f84", None))
        self.label_11.setText(QCoreApplication.translate("AFCalcToolView", u"\u6587\u4ef6\u8def\u5f84", None))
        self.label_13.setText(QCoreApplication.translate("AFCalcToolView", u"focus\u6bd4\u4f8b\u7cfb\u6570", None))
        self.focus_ratio.setText(QCoreApplication.translate("AFCalcToolView", u"2", None))
        self.okbutton.setText(QCoreApplication.translate("AFCalcToolView", u"\u786e\u8ba4", None))
    # retranslateUi

