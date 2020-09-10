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
        ShakeTestWindow.resize(805, 743)
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
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.corner_num = QSlider(self.groupBox_2)
        self.corner_num.setObjectName(u"corner_num")
        self.corner_num.setSliderPosition(50)
        self.corner_num.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.corner_num, 3, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 4, 0, 1, 1)

        self.set_roi_up = QSpinBox(self.groupBox_2)
        self.set_roi_up.setObjectName(u"set_roi_up")
        self.set_roi_up.setMaximum(1000)
        self.set_roi_up.setSingleStep(50)

        self.gridLayout_6.addWidget(self.set_roi_up, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 1, 0, 1, 1)

        self.set_roi_down = QSpinBox(self.groupBox_2)
        self.set_roi_down.setObjectName(u"set_roi_down")
        self.set_roi_down.setMaximum(1000)
        self.set_roi_down.setSingleStep(50)

        self.gridLayout_6.addWidget(self.set_roi_down, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 2, 0, 1, 1)

        self.corner_size = QSlider(self.groupBox_2)
        self.corner_size.setObjectName(u"corner_size")
        self.corner_size.setSliderPosition(40)
        self.corner_size.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.corner_size, 4, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)

        self.skipframes = QSpinBox(self.groupBox_2)
        self.skipframes.setObjectName(u"skipframes")
        self.skipframes.setMaximum(10000)
        self.skipframes.setSingleStep(10)

        self.gridLayout_6.addWidget(self.skipframes, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_6.addWidget(self.label_19, 5, 0, 1, 1)

        self.calc_inter_frams = QSpinBox(self.groupBox_2)
        self.calc_inter_frams.setObjectName(u"calc_inter_frams")
        self.calc_inter_frams.setMaximum(1000)
        self.calc_inter_frams.setValue(50)

        self.gridLayout_6.addWidget(self.calc_inter_frams, 5, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_6, 1, 0, 1, 1)

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

        self.remove_move_point_enable = QCheckBox(self.groupBox_2)
        self.remove_move_point_enable.setObjectName(u"remove_move_point_enable")
        self.remove_move_point_enable.setChecked(True)

        self.gridLayout_3.addWidget(self.remove_move_point_enable, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(270, 16777215))
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)

        self.center_x_distance = QDoubleSpinBox(self.groupBox_3)
        self.center_x_distance.setObjectName(u"center_x_distance")
        self.center_x_distance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.center_x_distance.setDecimals(4)
        self.center_x_distance.setMaximum(1000.000000000000000)

        self.gridLayout_7.addWidget(self.center_x_distance, 1, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 5, 0, 1, 1)

        self.any_average_x_distance = QDoubleSpinBox(self.groupBox_3)
        self.any_average_x_distance.setObjectName(u"any_average_x_distance")
        self.any_average_x_distance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.any_average_x_distance.setDecimals(4)
        self.any_average_x_distance.setMaximum(1000.000000000000000)

        self.gridLayout_7.addWidget(self.any_average_x_distance, 4, 1, 1, 1)

        self.any_varia_x_distance = QDoubleSpinBox(self.groupBox_3)
        self.any_varia_x_distance.setObjectName(u"any_varia_x_distance")
        self.any_varia_x_distance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.any_varia_x_distance.setDecimals(4)
        self.any_varia_x_distance.setMaximum(1000.000000000000000)

        self.gridLayout_7.addWidget(self.any_varia_x_distance, 5, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 2, 0, 1, 1)

        self.any_max_x_distance = QDoubleSpinBox(self.groupBox_3)
        self.any_max_x_distance.setObjectName(u"any_max_x_distance")
        self.any_max_x_distance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.any_max_x_distance.setDecimals(4)
        self.any_max_x_distance.setMaximum(1000.000000000000000)

        self.gridLayout_7.addWidget(self.any_max_x_distance, 2, 1, 1, 1)

        self.center_max_x_distance = QDoubleSpinBox(self.groupBox_3)
        self.center_max_x_distance.setObjectName(u"center_max_x_distance")
        self.center_max_x_distance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.center_max_x_distance.setDecimals(4)
        self.center_max_x_distance.setMaximum(1000.000000000000000)

        self.gridLayout_7.addWidget(self.center_max_x_distance, 0, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 4, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_7.addWidget(self.label_17, 6, 0, 1, 1)

        self.photo_warp_ratio_x = QDoubleSpinBox(self.groupBox_3)
        self.photo_warp_ratio_x.setObjectName(u"photo_warp_ratio_x")
        self.photo_warp_ratio_x.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.photo_warp_ratio_x.setDecimals(4)
        self.photo_warp_ratio_x.setMaximum(1000.000000000000000)

        self.gridLayout_7.addWidget(self.photo_warp_ratio_x, 6, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(270, 16777215))
        self.gridLayout_8 = QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.center_max_y_distance = QDoubleSpinBox(self.groupBox_5)
        self.center_max_y_distance.setObjectName(u"center_max_y_distance")
        self.center_max_y_distance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.center_max_y_distance.setDecimals(4)
        self.center_max_y_distance.setMaximum(1000.000000000000000)

        self.gridLayout_9.addWidget(self.center_max_y_distance, 0, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_9.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_9.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_9.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_9.addWidget(self.label_16, 5, 0, 1, 1)

        self.any_varia_y_distance = QDoubleSpinBox(self.groupBox_5)
        self.any_varia_y_distance.setObjectName(u"any_varia_y_distance")
        self.any_varia_y_distance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.any_varia_y_distance.setDecimals(4)
        self.any_varia_y_distance.setMaximum(1000.000000000000000)

        self.gridLayout_9.addWidget(self.any_varia_y_distance, 5, 1, 1, 1)

        self.any_average_y_distance = QDoubleSpinBox(self.groupBox_5)
        self.any_average_y_distance.setObjectName(u"any_average_y_distance")
        self.any_average_y_distance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.any_average_y_distance.setDecimals(4)
        self.any_average_y_distance.setMaximum(1000.000000000000000)

        self.gridLayout_9.addWidget(self.any_average_y_distance, 4, 1, 1, 1)

        self.any_max_y_distance = QDoubleSpinBox(self.groupBox_5)
        self.any_max_y_distance.setObjectName(u"any_max_y_distance")
        self.any_max_y_distance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.any_max_y_distance.setDecimals(4)
        self.any_max_y_distance.setMaximum(1000.000000000000000)

        self.gridLayout_9.addWidget(self.any_max_y_distance, 2, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_9.addWidget(self.label_15, 0, 0, 1, 1)

        self.center_y_distance = QDoubleSpinBox(self.groupBox_5)
        self.center_y_distance.setObjectName(u"center_y_distance")
        self.center_y_distance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.center_y_distance.setDecimals(4)
        self.center_y_distance.setMaximum(1000.000000000000000)

        self.gridLayout_9.addWidget(self.center_y_distance, 1, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_9.addWidget(self.label_18, 6, 0, 1, 1)

        self.photo_warp_ratio_y = QDoubleSpinBox(self.groupBox_5)
        self.photo_warp_ratio_y.setObjectName(u"photo_warp_ratio_y")
        self.photo_warp_ratio_y.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.photo_warp_ratio_y.setDecimals(4)
        self.photo_warp_ratio_y.setMaximum(1000.000000000000000)

        self.gridLayout_9.addWidget(self.photo_warp_ratio_y, 6, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_5)

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
        self.groupBox.setMinimumSize(QSize(500, 0))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        ShakeTestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ShakeTestWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 805, 22))
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
        self.label_7.setText(QCoreApplication.translate("ShakeTestWindow", u"\u8fd0\u52a8\u5e45\u5ea6", None))
        self.label_9.setText(QCoreApplication.translate("ShakeTestWindow", u"ROI\u4e0b\u8fb9\u754c", None))
        self.label_5.setText(QCoreApplication.translate("ShakeTestWindow", u"\u8df3\u8fc7\u5e27\u6570", None))
        self.label_8.setText(QCoreApplication.translate("ShakeTestWindow", u"ROI\u4e0a\u8fb9\u754c", None))
        self.label_6.setText(QCoreApplication.translate("ShakeTestWindow", u"\u7279\u5f81\u70b9\u6570\u91cf", None))
        self.label_19.setText(QCoreApplication.translate("ShakeTestWindow", u"\u8ba1\u7b97\u95f4\u9694\uff08\u5e27\uff09", None))
        self.label.setText(QCoreApplication.translate("ShakeTestWindow", u"\u89c6\u9891\u6587\u4ef6", None))
        self.openvideo.setText(QCoreApplication.translate("ShakeTestWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.remove_move_point_enable.setText(QCoreApplication.translate("ShakeTestWindow", u"\u53bb\u9664\u9759\u6b62\u7684\u7279\u5f81\u70b9", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ShakeTestWindow", u"\u6c34\u5e73\u65b9\u5411\u7ed3\u679c", None))
        self.label_2.setText(QCoreApplication.translate("ShakeTestWindow", u"\u4e2d\u5fc3\u70b9\u6a2a\u5411\u4f4d\u79fb", None))
        self.label_11.setText(QCoreApplication.translate("ShakeTestWindow", u"\u5404\u70b9\u6a2a\u5411\u4f4d\u79fb\u65b9\u5dee", None))
        self.label_3.setText(QCoreApplication.translate("ShakeTestWindow", u"\u4e2d\u5fc3\u70b9\u5e73\u5747\u6a2a\u5411\u4f4d\u79fb", None))
        self.label_4.setText(QCoreApplication.translate("ShakeTestWindow", u"\u5404\u70b9\u6700\u5927\u6a2a\u5411\u4f4d\u79fb", None))
        self.label_10.setText(QCoreApplication.translate("ShakeTestWindow", u"\u5404\u70b9\u5e73\u5747\u6a2a\u5411\u4f4d\u79fb", None))
        self.label_17.setText(QCoreApplication.translate("ShakeTestWindow", u"\u56fe\u7247\u626d\u66f2\u7a0b\u5ea6", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ShakeTestWindow", u"\u5782\u76f4\u65b9\u5411\u7ed3\u679c", None))
        self.label_12.setText(QCoreApplication.translate("ShakeTestWindow", u"\u5404\u70b9\u5e73\u5747\u7eb5\u5411\u4f4d\u79fb", None))
        self.label_13.setText(QCoreApplication.translate("ShakeTestWindow", u"\u5404\u70b9\u6700\u5927\u7eb5\u5411\u4f4d\u79fb", None))
        self.label_14.setText(QCoreApplication.translate("ShakeTestWindow", u"\u4e2d\u5fc3\u70b9\u5e73\u5747\u7eb5\u5411\u4f4d\u79fb", None))
        self.label_16.setText(QCoreApplication.translate("ShakeTestWindow", u"\u5404\u70b9\u7eb5\u5411\u4f4d\u79fb\u65b9\u5dee", None))
        self.label_15.setText(QCoreApplication.translate("ShakeTestWindow", u"\u4e2d\u5fc3\u70b9\u7eb5\u5411\u4f4d\u79fb", None))
        self.label_18.setText(QCoreApplication.translate("ShakeTestWindow", u"\u56fe\u7247\u626d\u66f2\u7a0b\u5ea6", None))
        self.groupBox_4.setTitle("")
        self.isok.setText(QCoreApplication.translate("ShakeTestWindow", u"\u5f00\u59cb", None))
        self.cancel_button.setText(QCoreApplication.translate("ShakeTestWindow", u"\u505c\u6b62", None))
        self.groupBox.setTitle(QCoreApplication.translate("ShakeTestWindow", u"\u89c6\u9891\u9884\u89c8", None))
    # retranslateUi

