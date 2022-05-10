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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
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

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"YUV\u914d\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5927\u5c0f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"4K", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"1080P", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"720P", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u683c\u5f0f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"NV21", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"NV12", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog", u"YCrCb", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Dialog", u"YUV420", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Dialog", u"YUV422", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("Dialog", u"UYVY", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("Dialog", u"YUYV", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("Dialog", u"YVYU", None))

        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u65cb\u8f6c\u65f6\u4fdd\u5b58\u56fe\u7247", None))
    # retranslateUi

