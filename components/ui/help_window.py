# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        if not HelpWindow.objectName():
            HelpWindow.setObjectName(u"HelpWindow")
        HelpWindow.resize(800, 600)
        self.centralwidget = QWidget(HelpWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(15)
        self.textBrowser.setFont(font)
        self.textBrowser.setAcceptRichText(False)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        HelpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HelpWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        HelpWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HelpWindow)
        self.statusbar.setObjectName(u"statusbar")
        HelpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HelpWindow)

        QMetaObject.connectSlotsByName(HelpWindow)
    # setupUi

    def retranslateUi(self, HelpWindow):
        HelpWindow.setWindowTitle(QCoreApplication.translate("HelpWindow", u"\u5e2e\u52a9\u624b\u518c", None))
    # retranslateUi

