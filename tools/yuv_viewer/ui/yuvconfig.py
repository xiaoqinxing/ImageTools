# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yuvconfig.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_YUVConfig(object):
    def setupUi(self, YUVConfig):
        if not YUVConfig.objectName():
            YUVConfig.setObjectName(u"YUVConfig")
        YUVConfig.resize(400, 300)
        self.verticalLayout = QVBoxLayout(YUVConfig)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(YUVConfig)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_2)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.checkBox = QCheckBox(YUVConfig)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox)

        self.buttonBox = QDialogButtonBox(YUVConfig)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(YUVConfig)
        self.buttonBox.accepted.connect(YUVConfig.accept)
        self.buttonBox.rejected.connect(YUVConfig.reject)

        QMetaObject.connectSlotsByName(YUVConfig)
    # setupUi

    def retranslateUi(self, YUVConfig):
        YUVConfig.setWindowTitle(QCoreApplication.translate("YUVConfig", u"\u56fe\u7247\u67e5\u770b\u5de5\u5177\u914d\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("YUVConfig", u"YUV\u914d\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("YUVConfig", u"\u5927\u5c0f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("YUVConfig", u"4K", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("YUVConfig", u"1080P", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("YUVConfig", u"720P", None))

        self.label_3.setText(QCoreApplication.translate("YUVConfig", u"\u683c\u5f0f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("YUVConfig", u"NV21", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("YUVConfig", u"NV12", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("YUVConfig", u"YCrCb", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("YUVConfig", u"YUV420", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("YUVConfig", u"YUV422", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("YUVConfig", u"UYVY", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("YUVConfig", u"YUYV", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("YUVConfig", u"YVYU", None))

        self.checkBox.setText(QCoreApplication.translate("YUVConfig", u"\u65cb\u8f6c\u65f6\u4fdd\u5b58\u56fe\u7247", None))
    # retranslateUi

