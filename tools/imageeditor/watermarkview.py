# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'watermarkview.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WaterMarkView(object):
    def setupUi(self, WaterMarkView):
        if not WaterMarkView.objectName():
            WaterMarkView.setObjectName(u"WaterMarkView")
        WaterMarkView.resize(252, 327)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WaterMarkView.sizePolicy().hasHeightForWidth())
        WaterMarkView.setSizePolicy(sizePolicy)
        WaterMarkView.setSizeGripEnabled(True)
        self.gridLayout = QGridLayout(WaterMarkView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(WaterMarkView)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.analysis = QPushButton(self.groupBox)
        self.analysis.setObjectName(u"analysis")

        self.gridLayout_9.addWidget(self.analysis, 2, 1, 1, 1)

        self.generate = QPushButton(self.groupBox)
        self.generate.setObjectName(u"generate")

        self.gridLayout_9.addWidget(self.generate, 1, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_8.addWidget(self.label, 1, 0, 1, 1)

        self.change_transparent = QSlider(self.groupBox)
        self.change_transparent.setObjectName(u"change_transparent")
        self.change_transparent.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.change_transparent, 4, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_8.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_8.addWidget(self.label_19, 3, 0, 1, 1)

        self.change_watermark_size = QSlider(self.groupBox)
        self.change_watermark_size.setObjectName(u"change_watermark_size")
        self.change_watermark_size.setValue(50)
        self.change_watermark_size.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.change_watermark_size, 3, 1, 1, 1)

        self.change_watermark_th = QSlider(self.groupBox)
        self.change_watermark_th.setObjectName(u"change_watermark_th")
        self.change_watermark_th.setMaximum(255)
        self.change_watermark_th.setValue(127)
        self.change_watermark_th.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.change_watermark_th, 2, 1, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_8.addWidget(self.comboBox, 1, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_8.addWidget(self.label_18, 2, 0, 1, 1)

        self.open_watermark = QPushButton(self.groupBox)
        self.open_watermark.setObjectName(u"open_watermark")

        self.gridLayout_8.addWidget(self.open_watermark, 0, 0, 1, 1)

        self.watermark_path = QLineEdit(self.groupBox)
        self.watermark_path.setObjectName(u"watermark_path")

        self.gridLayout_8.addWidget(self.watermark_path, 0, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)


        self.retranslateUi(WaterMarkView)

        QMetaObject.connectSlotsByName(WaterMarkView)
    # setupUi

    def retranslateUi(self, WaterMarkView):
        WaterMarkView.setWindowTitle(QCoreApplication.translate("WaterMarkView", u"\u6c34\u5370\u5236\u4f5c\u5de5\u5177", None))
        self.groupBox.setTitle(QCoreApplication.translate("WaterMarkView", u"\u5236\u4f5c\u6c34\u5370", None))
        self.analysis.setText(QCoreApplication.translate("WaterMarkView", u"\u89e3\u6790\u5e26\u6c34\u5370\u7684\u56fe\u7247", None))
        self.generate.setText(QCoreApplication.translate("WaterMarkView", u"\u5236\u4f5c\u5e26\u6c34\u5370\u7684\u56fe\u7247", None))
        self.label.setText(QCoreApplication.translate("WaterMarkView", u"\u6c34\u5370\u7c7b\u578b", None))
        self.label_2.setText(QCoreApplication.translate("WaterMarkView", u"\u900f\u660e\u7a0b\u5ea6", None))
        self.label_19.setText(QCoreApplication.translate("WaterMarkView", u"\u8c03\u6574\u6c34\u5370\u5927\u5c0f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("WaterMarkView", u"\u7a7a\u57df\u9690\u5f62\u6c34\u5370", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("WaterMarkView", u"\u65f6\u57df\u9690\u5f62\u6c34\u5370", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("WaterMarkView", u"\u534a\u900f\u660e\u6c34\u5370", None))

        self.label_18.setText(QCoreApplication.translate("WaterMarkView", u"\u4e8c\u503c\u5316", None))
        self.open_watermark.setText(QCoreApplication.translate("WaterMarkView", u"\u5bfc\u5165\u6c34\u5370", None))
    # retranslateUi

