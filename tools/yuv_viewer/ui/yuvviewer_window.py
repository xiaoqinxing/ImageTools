# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yuvviewer_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_YUVEditor(object):
    def setupUi(self, YUVEditor):
        if not YUVEditor.objectName():
            YUVEditor.setObjectName(u"YUVEditor")
        YUVEditor.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/tool_icon/resource/main.png", QSize(), QIcon.Normal, QIcon.Off)
        YUVEditor.setWindowIcon(icon)
        YUVEditor.setToolTipDuration(-1)
        YUVEditor.setAnimated(True)
        YUVEditor.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks|QMainWindow.GroupedDragging|QMainWindow.VerticalTabs)
        self.saveimage = QAction(YUVEditor)
        self.saveimage.setObjectName(u"saveimage")
        icon1 = QIcon()
        icon1.addFile(u":/tool_icon/resource/save_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveimage.setIcon(icon1)
        self.openimage = QAction(YUVEditor)
        self.openimage.setObjectName(u"openimage")
        icon2 = QIcon()
        icon2.addFile(u":/tool_icon/resource/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openimage.setIcon(icon2)
        self.actionstats = QAction(YUVEditor)
        self.actionstats.setObjectName(u"actionstats")
        icon3 = QIcon()
        icon3.addFile(u":/tool_icon/resource/stats.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionstats.setIcon(icon3)
        self.nextphoto = QAction(YUVEditor)
        self.nextphoto.setObjectName(u"nextphoto")
        icon4 = QIcon()
        icon4.addFile(u":/tool_icon/resource/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextphoto.setIcon(icon4)
        self.prephoto = QAction(YUVEditor)
        self.prephoto.setObjectName(u"prephoto")
        icon5 = QIcon()
        icon5.addFile(u":/tool_icon/resource/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prephoto.setIcon(icon5)
        self.deletephoto = QAction(YUVEditor)
        self.deletephoto.setObjectName(u"deletephoto")
        icon6 = QIcon()
        icon6.addFile(u":/tool_icon/resource/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deletephoto.setIcon(icon6)
        self.add_compare = QAction(YUVEditor)
        self.add_compare.setObjectName(u"add_compare")
        icon7 = QIcon()
        icon7.addFile(u":/tool_icon/resource/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_compare.setIcon(icon7)
        self.rotateright = QAction(YUVEditor)
        self.rotateright.setObjectName(u"rotateright")
        icon8 = QIcon()
        icon8.addFile(u":/tool_icon/resource/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rotateright.setIcon(icon8)
        self.yuvconfig = QAction(YUVEditor)
        self.yuvconfig.setObjectName(u"yuvconfig")
        icon9 = QIcon()
        icon9.addFile(u":/tool_icon/resource/config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.yuvconfig.setIcon(icon9)
        self.centralwidget = QWidget(YUVEditor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.photo_title = QGroupBox(self.centralwidget)
        self.photo_title.setObjectName(u"photo_title")
        self.gridLayout_3 = QGridLayout(self.photo_title)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.photo_title, 0, 0, 1, 1)

        YUVEditor.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(YUVEditor)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMouseTracking(True)
        YUVEditor.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(YUVEditor)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setAllowedAreas(Qt.AllToolBarAreas)
        self.toolBar.setOrientation(Qt.Vertical)
        YUVEditor.addToolBar(Qt.RightToolBarArea, self.toolBar)

        self.toolBar.addAction(self.openimage)
        self.toolBar.addAction(self.saveimage)
        self.toolBar.addAction(self.yuvconfig)
        self.toolBar.addAction(self.deletephoto)
        self.toolBar.addAction(self.actionstats)
        self.toolBar.addAction(self.prephoto)
        self.toolBar.addAction(self.nextphoto)
        self.toolBar.addAction(self.rotateright)
        self.toolBar.addAction(self.add_compare)

        self.retranslateUi(YUVEditor)

        QMetaObject.connectSlotsByName(YUVEditor)
    # setupUi

    def retranslateUi(self, YUVEditor):
        YUVEditor.setWindowTitle(QCoreApplication.translate("YUVEditor", u"YUV\u56fe\u7247\u67e5\u770b\u5de5\u5177", None))
#if QT_CONFIG(tooltip)
        YUVEditor.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.saveimage.setText(QCoreApplication.translate("YUVEditor", u"save", None))
#if QT_CONFIG(shortcut)
        self.saveimage.setShortcut(QCoreApplication.translate("YUVEditor", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.openimage.setText(QCoreApplication.translate("YUVEditor", u"open", None))
#if QT_CONFIG(tooltip)
        self.openimage.setToolTip(QCoreApplication.translate("YUVEditor", u"open", None))
#endif // QT_CONFIG(tooltip)
        self.actionstats.setText(QCoreApplication.translate("YUVEditor", u"\u7edf\u8ba1\u4fe1\u606f", None))
#if QT_CONFIG(tooltip)
        self.actionstats.setToolTip(QCoreApplication.translate("YUVEditor", u"\u7edf\u8ba1\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.nextphoto.setText(QCoreApplication.translate("YUVEditor", u"\u4e0b\u4e00\u4e2a\u56fe\u7247", None))
#if QT_CONFIG(shortcut)
        self.nextphoto.setShortcut(QCoreApplication.translate("YUVEditor", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.prephoto.setText(QCoreApplication.translate("YUVEditor", u"\u4e0a\u4e00\u5f20\u56fe\u7247", None))
#if QT_CONFIG(shortcut)
        self.prephoto.setShortcut(QCoreApplication.translate("YUVEditor", u"Up", None))
#endif // QT_CONFIG(shortcut)
        self.deletephoto.setText(QCoreApplication.translate("YUVEditor", u"\u5220\u9664", None))
#if QT_CONFIG(tooltip)
        self.deletephoto.setToolTip(QCoreApplication.translate("YUVEditor", u"\u5220\u9664", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.deletephoto.setShortcut(QCoreApplication.translate("YUVEditor", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.add_compare.setText(QCoreApplication.translate("YUVEditor", u"\u6dfb\u52a0\u5bf9\u6bd4\u56fe\u7247", None))
        self.rotateright.setText(QCoreApplication.translate("YUVEditor", u"\u987a\u65f6\u9488\u65cb\u8f6c", None))
        self.yuvconfig.setText(QCoreApplication.translate("YUVEditor", u"YUV\u914d\u7f6e", None))
        self.photo_title.setTitle("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("YUVEditor", u"toolBar_2", None))
    # retranslateUi

