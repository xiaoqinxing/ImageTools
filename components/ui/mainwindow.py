# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1140, 857)
        icon = QIcon()
        icon.addFile(u":/tool_icon/resource/main.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.shake_tool = QAction(MainWindow)
        self.shake_tool.setObjectName(u"shake_tool")
        self.imageeditor = QAction(MainWindow)
        self.imageeditor.setObjectName(u"imageeditor")
        self.about = QAction(MainWindow)
        self.about.setObjectName(u"about")
        self.rawimageeditor = QAction(MainWindow)
        self.rawimageeditor.setObjectName(u"rawimageeditor")
        self.video_compare = QAction(MainWindow)
        self.video_compare.setObjectName(u"video_compare")
        self.pqtools2code = QAction(MainWindow)
        self.pqtools2code.setObjectName(u"pqtools2code")
        self.field_depth_tool = QAction(MainWindow)
        self.field_depth_tool.setObjectName(u"field_depth_tool")
        self.af_calc_tool = QAction(MainWindow)
        self.af_calc_tool.setObjectName(u"af_calc_tool")
        self.userguide = QAction(MainWindow)
        self.userguide.setObjectName(u"userguide")
        self.clearcache = QAction(MainWindow)
        self.clearcache.setObjectName(u"clearcache")
        self.checkupdate = QAction(MainWindow)
        self.checkupdate.setObjectName(u"checkupdate")
        self.yuv_viewer = QAction(MainWindow)
        self.yuv_viewer.setObjectName(u"yuv_viewer")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setAcceptDrops(True)
        self.mdiArea.setLineWidth(0)
        self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdiArea.setViewMode(QMdiArea.TabbedView)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setTabShape(QTabWidget.Rounded)

        self.gridLayout_2.addWidget(self.mdiArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1140, 22))
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menuISP = QMenu(self.menubar)
        self.menuISP.setObjectName(u"menuISP")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menuISP.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menu_2.addAction(self.shake_tool)
        self.menu_2.addAction(self.imageeditor)
        self.menu_2.addAction(self.rawimageeditor)
        self.menu_2.addAction(self.video_compare)
        self.menu_2.addAction(self.yuv_viewer)
        self.menuISP.addAction(self.pqtools2code)
        self.menuISP.addAction(self.field_depth_tool)
        self.menu.addAction(self.userguide)
        self.menu.addAction(self.clearcache)
        self.menu.addAction(self.checkupdate)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ImageTools", None))
        self.shake_tool.setText(QCoreApplication.translate("MainWindow", u"\u6296\u52a8\u6d4b\u8bd5\u5de5\u5177", None))
        self.imageeditor.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5206\u6790\u5de5\u5177", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.rawimageeditor.setText(QCoreApplication.translate("MainWindow", u"raw\u56fe\u5206\u6790\u5de5\u5177", None))
        self.video_compare.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u5bf9\u6bd4\u5de5\u5177", None))
        self.pqtools2code.setText(QCoreApplication.translate("MainWindow", u"PQtools\u8f6c\u4ee3\u7801", None))
        self.field_depth_tool.setText(QCoreApplication.translate("MainWindow", u"\u955c\u5934\u8ba1\u7b97\u5668", None))
        self.af_calc_tool.setText(QCoreApplication.translate("MainWindow", u"\u955c\u5934\u66f2\u7ebf\u8ba1\u7b97\u5de5\u5177", None))
        self.userguide.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u624b\u518c", None))
        self.clearcache.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7406\u7f13\u5b58", None))
        self.checkupdate.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.yuv_viewer.setText(QCoreApplication.translate("MainWindow", u"YUV\u67e5\u770b\u5de5\u5177", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u5177", None))
        self.menuISP.setTitle(QCoreApplication.translate("MainWindow", u"ISP", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

