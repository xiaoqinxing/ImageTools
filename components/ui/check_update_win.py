# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check_update_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CheckUpdate(object):
    def setupUi(self, CheckUpdate):
        if not CheckUpdate.objectName():
            CheckUpdate.setObjectName(u"CheckUpdate")
        CheckUpdate.resize(395, 294)
        self.gridLayout = QGridLayout(CheckUpdate)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.version_num = QLabel(CheckUpdate)
        self.version_num.setObjectName(u"version_num")

        self.verticalLayout.addWidget(self.version_num)

        self.textBrowser = QTextBrowser(CheckUpdate)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.textBrowser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.autoupdate = QCheckBox(CheckUpdate)
        self.autoupdate.setObjectName(u"autoupdate")

        self.horizontalLayout.addWidget(self.autoupdate)

        self.progress = QProgressBar(CheckUpdate)
        self.progress.setObjectName(u"progress")
        self.progress.setValue(0)

        self.horizontalLayout.addWidget(self.progress)

        self.ok = QPushButton(CheckUpdate)
        self.ok.setObjectName(u"ok")
        self.ok.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout.addWidget(self.ok)

        self.cancel = QPushButton(CheckUpdate)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout.addWidget(self.cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(CheckUpdate)

        QMetaObject.connectSlotsByName(CheckUpdate)
    # setupUi

    def retranslateUi(self, CheckUpdate):
        CheckUpdate.setWindowTitle(QCoreApplication.translate("CheckUpdate", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.version_num.setText("")
        self.autoupdate.setText(QCoreApplication.translate("CheckUpdate", u"\u81ea\u52a8\u66f4\u65b0", None))
        self.ok.setText(QCoreApplication.translate("CheckUpdate", u"\u7acb\u523b\u66f4\u65b0", None))
        self.cancel.setText(QCoreApplication.translate("CheckUpdate", u"\u4ee5\u540e\u518d\u8bf4", None))
    # retranslateUi

