# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'field_depth_window.ui'
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


class Ui_FieldDepthWindow(object):
    def setupUi(self, FieldDepthWindow):
        if not FieldDepthWindow.objectName():
            FieldDepthWindow.setObjectName(u"FieldDepthWindow")
        FieldDepthWindow.resize(875, 602)
        FieldDepthWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(FieldDepthWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(298, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.output_image_distance = QRadioButton(self.groupBox)
        self.buttonGroup = QButtonGroup(FieldDepthWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.output_image_distance)
        self.output_image_distance.setObjectName(u"output_image_distance")
        self.output_image_distance.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_4.addWidget(self.output_image_distance, 0, 2, 1, 1)

        self.output_params = QRadioButton(self.groupBox)
        self.buttonGroup.addButton(self.output_params)
        self.output_params.setObjectName(u"output_params")
        self.output_params.setMaximumSize(QSize(68, 16777215))
        self.output_params.setChecked(False)

        self.gridLayout_4.addWidget(self.output_params, 0, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.output_field_depth = QRadioButton(self.groupBox)
        self.buttonGroup.addButton(self.output_field_depth)
        self.output_field_depth.setObjectName(u"output_field_depth")
        self.output_field_depth.setMaximumSize(QSize(300, 16777215))
        self.output_field_depth.setChecked(True)

        self.gridLayout_4.addWidget(self.output_field_depth, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.input_distance = QRadioButton(self.groupBox)
        self.buttonGroup_2 = QButtonGroup(FieldDepthWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.input_distance)
        self.input_distance.setObjectName(u"input_distance")
        self.input_distance.setMaximumSize(QSize(68, 16777215))
        self.input_distance.setChecked(True)

        self.gridLayout_5.addWidget(self.input_distance, 0, 3, 1, 1)

        self.input_apeture = QRadioButton(self.groupBox)
        self.buttonGroup_2.addButton(self.input_apeture)
        self.input_apeture.setObjectName(u"input_apeture")
        self.input_apeture.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.input_apeture, 0, 2, 1, 1)

        self.input_focus_length = QRadioButton(self.groupBox)
        self.buttonGroup_2.addButton(self.input_focus_length)
        self.input_focus_length.setObjectName(u"input_focus_length")
        self.input_focus_length.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.input_focus_length, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 1, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(298, 16777215))
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.focus_length = QDoubleSpinBox(self.groupBox_2)
        self.focus_length.setObjectName(u"focus_length")
        self.focus_length.setMaximumSize(QSize(300, 16777215))
        self.focus_length.setMaximum(200.000000000000000)
        self.focus_length.setValue(50.000000000000000)

        self.gridLayout_6.addWidget(self.focus_length, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_6.addWidget(self.label, 1, 0, 1, 1)

        self.aperture = QDoubleSpinBox(self.groupBox_2)
        self.aperture.setObjectName(u"aperture")
        self.aperture.setMaximumSize(QSize(300, 16777215))
        self.aperture.setSingleStep(0.100000000000000)
        self.aperture.setValue(1.400000000000000)

        self.gridLayout_6.addWidget(self.aperture, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_6.addWidget(self.label_2, 2, 0, 1, 1)

        self.focus_distance = QDoubleSpinBox(self.groupBox_2)
        self.focus_distance.setObjectName(u"focus_distance")
        self.focus_distance.setMaximumSize(QSize(300, 16777215))
        self.focus_distance.setBaseSize(QSize(2, 2))
        self.focus_distance.setValue(2.000000000000000)

        self.gridLayout_6.addWidget(self.focus_distance, 2, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_6.addWidget(self.label_8, 3, 0, 1, 1)

        self.sensor_size_list = QComboBox(self.groupBox_2)
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.addItem("")
        self.sensor_size_list.setObjectName(u"sensor_size_list")
        self.sensor_size_list.setMaximumSize(QSize(188, 16777215))

        self.gridLayout_6.addWidget(self.sensor_size_list, 3, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.groupBox_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetMaximumSize)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(294, 16777215))
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout.addWidget(self.label_3)

        self.sensor_size = QDoubleSpinBox(self.groupBox_3)
        self.sensor_size.setObjectName(u"sensor_size")
        self.sensor_size.setMaximumSize(QSize(300, 16777215))
        self.sensor_size.setMaximum(100.000000000000000)
        self.sensor_size.setSingleStep(0.005000000000000)
        self.sensor_size.setValue(43.270000000000003)

        self.horizontalLayout.addWidget(self.sensor_size)


        self.gridLayout_7.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_2.addWidget(self.label_7)

        self.confusion_circle_diam_slide = QSlider(self.groupBox_3)
        self.confusion_circle_diam_slide.setObjectName(u"confusion_circle_diam_slide")
        self.confusion_circle_diam_slide.setMaximumSize(QSize(300, 16777215))
        self.confusion_circle_diam_slide.setValue(50)
        self.confusion_circle_diam_slide.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.confusion_circle_diam_slide)

        self.confusion_circle_diam = QDoubleSpinBox(self.groupBox_3)
        self.confusion_circle_diam.setObjectName(u"confusion_circle_diam")
        self.confusion_circle_diam.setMaximumSize(QSize(300, 16777215))
        self.confusion_circle_diam.setDecimals(3)
        self.confusion_circle_diam.setMaximum(1.000000000000000)
        self.confusion_circle_diam.setSingleStep(0.005000000000000)
        self.confusion_circle_diam.setValue(0.040000000000000)

        self.horizontalLayout_2.addWidget(self.confusion_circle_diam)


        self.gridLayout_7.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_4.addWidget(self.label_12)

        self.focus_min_range = QDoubleSpinBox(self.groupBox_3)
        self.focus_min_range.setObjectName(u"focus_min_range")
        self.focus_min_range.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_4.addWidget(self.focus_min_range)

        self.focus_max_range = QDoubleSpinBox(self.groupBox_3)
        self.focus_max_range.setObjectName(u"focus_max_range")
        self.focus_max_range.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_4.addWidget(self.focus_max_range)


        self.gridLayout_7.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_5.addWidget(self.label_13)

        self.apeture_min_range = QDoubleSpinBox(self.groupBox_3)
        self.apeture_min_range.setObjectName(u"apeture_min_range")
        self.apeture_min_range.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_5.addWidget(self.apeture_min_range)

        self.apeture_max_range = QDoubleSpinBox(self.groupBox_3)
        self.apeture_max_range.setObjectName(u"apeture_max_range")
        self.apeture_max_range.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_5.addWidget(self.apeture_max_range)


        self.gridLayout_7.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_6.addWidget(self.label_14)

        self.distance_min_range = QDoubleSpinBox(self.groupBox_3)
        self.distance_min_range.setObjectName(u"distance_min_range")
        self.distance_min_range.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_6.addWidget(self.distance_min_range)

        self.distance_max_range = QDoubleSpinBox(self.groupBox_3)
        self.distance_max_range.setObjectName(u"distance_max_range")
        self.distance_max_range.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_6.addWidget(self.distance_max_range)


        self.gridLayout_7.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.groupBox_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(294, 16777215))

        self.verticalLayout_8.addWidget(self.pushButton)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)


        self.gridLayout.addLayout(self.verticalLayout_10, 0, 1, 1, 1)

        self.plotview = QGridLayout()
        self.plotview.setObjectName(u"plotview")

        self.gridLayout.addLayout(self.plotview, 0, 0, 1, 1)

        FieldDepthWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FieldDepthWindow)
        self.statusbar.setObjectName(u"statusbar")
        FieldDepthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FieldDepthWindow)

        QMetaObject.connectSlotsByName(FieldDepthWindow)
    # setupUi

    def retranslateUi(self, FieldDepthWindow):
        FieldDepthWindow.setWindowTitle(QCoreApplication.translate("FieldDepthWindow", u"\u666f\u6df1\u8ba1\u7b97\u5668", None))
        self.groupBox.setTitle(QCoreApplication.translate("FieldDepthWindow", u"\u53d8\u91cf\u8bbe\u7f6e", None))
        self.output_image_distance.setText(QCoreApplication.translate("FieldDepthWindow", u"\u50cf\u8ddd", None))
        self.output_params.setText(QCoreApplication.translate("FieldDepthWindow", u"\u53c2\u6570", None))
        self.label_5.setText(QCoreApplication.translate("FieldDepthWindow", u"\u56fe\u50cf\u8f93\u51fa", None))
        self.output_field_depth.setText(QCoreApplication.translate("FieldDepthWindow", u"\u666f\u6df1", None))
        self.input_distance.setText(QCoreApplication.translate("FieldDepthWindow", u"\u7269\u8ddd", None))
        self.input_apeture.setText(QCoreApplication.translate("FieldDepthWindow", u"\u5149\u5708", None))
        self.input_focus_length.setText(QCoreApplication.translate("FieldDepthWindow", u"\u7126\u8ddd", None))
        self.label_6.setText(QCoreApplication.translate("FieldDepthWindow", u"\u53d8\u91cf", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("FieldDepthWindow", u"\u57fa\u7840\u8bbe\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("FieldDepthWindow", u"\u7126\u8ddd(mm)", None))
        self.label.setText(QCoreApplication.translate("FieldDepthWindow", u"\u5149\u5708(F)", None))
        self.label_2.setText(QCoreApplication.translate("FieldDepthWindow", u"\u7269\u4f53\u8ddd\u79bb(m)", None))
        self.label_8.setText(QCoreApplication.translate("FieldDepthWindow", u"sensor\u5c3a\u5bf8(\u82f1\u5bf8)", None))
        self.sensor_size_list.setItemText(0, QCoreApplication.translate("FieldDepthWindow", u"1/6", None))
        self.sensor_size_list.setItemText(1, QCoreApplication.translate("FieldDepthWindow", u"1/4", None))
        self.sensor_size_list.setItemText(2, QCoreApplication.translate("FieldDepthWindow", u"1/3.6", None))
        self.sensor_size_list.setItemText(3, QCoreApplication.translate("FieldDepthWindow", u"1/3.2", None))
        self.sensor_size_list.setItemText(4, QCoreApplication.translate("FieldDepthWindow", u"1/3", None))
        self.sensor_size_list.setItemText(5, QCoreApplication.translate("FieldDepthWindow", u"1/2.8", None))
        self.sensor_size_list.setItemText(6, QCoreApplication.translate("FieldDepthWindow", u"1/2.7", None))
        self.sensor_size_list.setItemText(7, QCoreApplication.translate("FieldDepthWindow", u"1/2.5", None))
        self.sensor_size_list.setItemText(8, QCoreApplication.translate("FieldDepthWindow", u"1/2", None))
        self.sensor_size_list.setItemText(9, QCoreApplication.translate("FieldDepthWindow", u"1/1.8", None))
        self.sensor_size_list.setItemText(10, QCoreApplication.translate("FieldDepthWindow", u"1/1.7", None))
        self.sensor_size_list.setItemText(11, QCoreApplication.translate("FieldDepthWindow", u"1/1.6", None))
        self.sensor_size_list.setItemText(12, QCoreApplication.translate("FieldDepthWindow", u"2/3", None))
        self.sensor_size_list.setItemText(13, QCoreApplication.translate("FieldDepthWindow", u"1", None))
        self.sensor_size_list.setItemText(14, QCoreApplication.translate("FieldDepthWindow", u"4/3", None))
        self.sensor_size_list.setItemText(15, QCoreApplication.translate("FieldDepthWindow", u"1.8", None))
        self.sensor_size_list.setItemText(16, QCoreApplication.translate("FieldDepthWindow", u"35mm film", None))

        self.sensor_size_list.setCurrentText(QCoreApplication.translate("FieldDepthWindow", u"1/6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("FieldDepthWindow", u"\u9ad8\u7ea7\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("FieldDepthWindow", u"sensor\u5c3a\u5bf8(mm)", None))
        self.label_7.setText(QCoreApplication.translate("FieldDepthWindow", u"\u5f25\u6563\u5708\u76f4\u5f84(mm)", None))
        self.label_12.setText(QCoreApplication.translate("FieldDepthWindow", u"\u7126\u8ddd\u8303\u56f4(mm)", None))
        self.label_13.setText(QCoreApplication.translate("FieldDepthWindow", u"\u5149\u5708\u8303\u56f4(F)", None))
        self.label_14.setText(QCoreApplication.translate("FieldDepthWindow", u"\u5bf9\u7126\u8303\u56f4(m)", None))
        self.pushButton.setText(QCoreApplication.translate("FieldDepthWindow", u"\u786e\u8ba4", None))
    # retranslateUi

