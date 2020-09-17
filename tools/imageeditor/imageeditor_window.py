# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imageeditor_window.ui'
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

import resource_rc

class Ui_ImageEditor(object):
    def setupUi(self, ImageEditor):
        if not ImageEditor.objectName():
            ImageEditor.setObjectName(u"ImageEditor")
        ImageEditor.resize(800, 600)
        ImageEditor.setToolTipDuration(-1)
        ImageEditor.setAnimated(True)
        ImageEditor.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks|QMainWindow.GroupedDragging|QMainWindow.VerticalTabs)
        self.historgram = QAction(ImageEditor)
        self.historgram.setObjectName(u"historgram")
        self.statics = QAction(ImageEditor)
        self.statics.setObjectName(u"statics")
        self.statics.setCheckable(True)
        self.boxblur = QAction(ImageEditor)
        self.boxblur.setObjectName(u"boxblur")
        self.guassian = QAction(ImageEditor)
        self.guassian.setObjectName(u"guassian")
        self.saveimage = QAction(ImageEditor)
        self.saveimage.setObjectName(u"saveimage")
        icon = QIcon()
        icon.addFile(u":/tool_icon/resource/save_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveimage.setIcon(icon)
        self.medianblur = QAction(ImageEditor)
        self.medianblur.setObjectName(u"medianblur")
        self.medianblur.setShortcutContext(Qt.WindowShortcut)
        self.bilateralblur = QAction(ImageEditor)
        self.bilateralblur.setObjectName(u"bilateralblur")
        self.compareimage = QAction(ImageEditor)
        self.compareimage.setObjectName(u"compareimage")
        icon1 = QIcon()
        icon1.addFile(u":/tool_icon/resource/compare.png", QSize(), QIcon.Normal, QIcon.Off)
        self.compareimage.setIcon(icon1)
        self.openimage = QAction(ImageEditor)
        self.openimage.setObjectName(u"openimage")
        icon2 = QIcon()
        icon2.addFile(u":/tool_icon/resource/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openimage.setIcon(icon2)
        self.actionstats = QAction(ImageEditor)
        self.actionstats.setObjectName(u"actionstats")
        icon3 = QIcon()
        icon3.addFile(u":/tool_icon/resource/stats.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionstats.setIcon(icon3)
        self.centralwidget = QWidget(ImageEditor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setAcceptDrops(True)
        self.graphicsView.setToolTipDuration(-1)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.graphicsView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.graphicsView.setTransformationAnchor(QGraphicsView.AnchorViewCenter)
        self.graphicsView.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        self.gridLayout.addWidget(self.graphicsView, 0, 1, 3, 1)

        ImageEditor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ImageEditor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.blur = QMenu(self.menu_2)
        self.blur.setObjectName(u"blur")
        ImageEditor.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(ImageEditor)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMouseTracking(True)
        ImageEditor.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(ImageEditor)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setAllowedAreas(Qt.AllToolBarAreas)
        self.toolBar.setOrientation(Qt.Vertical)
        ImageEditor.addToolBar(Qt.RightToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_2.menuAction())
        self.menu_2.addAction(self.blur.menuAction())
        self.blur.addAction(self.boxblur)
        self.blur.addAction(self.guassian)
        self.blur.addAction(self.medianblur)
        self.blur.addAction(self.bilateralblur)
        self.toolBar.addAction(self.openimage)
        self.toolBar.addAction(self.saveimage)
        self.toolBar.addAction(self.compareimage)
        self.toolBar.addAction(self.actionstats)

        self.retranslateUi(ImageEditor)

        QMetaObject.connectSlotsByName(ImageEditor)
    # setupUi

    def retranslateUi(self, ImageEditor):
        ImageEditor.setWindowTitle(QCoreApplication.translate("ImageEditor", u"\u56fe\u7247\u5904\u7406\u5de5\u5177", None))
#if QT_CONFIG(tooltip)
        ImageEditor.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.historgram.setText(QCoreApplication.translate("ImageEditor", u"\u76f4\u65b9\u56fe", None))
        self.statics.setText(QCoreApplication.translate("ImageEditor", u"\u7edf\u8ba1\u4fe1\u606f", None))
        self.boxblur.setText(QCoreApplication.translate("ImageEditor", u"\u65b9\u6846\u6ee4\u6ce2", None))
        self.guassian.setText(QCoreApplication.translate("ImageEditor", u"\u9ad8\u65af\u6ee4\u6ce2", None))
        self.saveimage.setText(QCoreApplication.translate("ImageEditor", u"save", None))
#if QT_CONFIG(shortcut)
        self.saveimage.setShortcut(QCoreApplication.translate("ImageEditor", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.medianblur.setText(QCoreApplication.translate("ImageEditor", u"\u4e2d\u503c\u6ee4\u6ce2", None))
        self.bilateralblur.setText(QCoreApplication.translate("ImageEditor", u"\u53cc\u8fb9\u6ee4\u6ce2", None))
        self.compareimage.setText(QCoreApplication.translate("ImageEditor", u"compare", None))
#if QT_CONFIG(tooltip)
        self.compareimage.setToolTip(QCoreApplication.translate("ImageEditor", u"compare", None))
#endif // QT_CONFIG(tooltip)
        self.openimage.setText(QCoreApplication.translate("ImageEditor", u"open", None))
#if QT_CONFIG(tooltip)
        self.openimage.setToolTip(QCoreApplication.translate("ImageEditor", u"open", None))
#endif // QT_CONFIG(tooltip)
        self.actionstats.setText(QCoreApplication.translate("ImageEditor", u"stats", None))
#if QT_CONFIG(tooltip)
        self.actionstats.setToolTip(QCoreApplication.translate("ImageEditor", u"\u7edf\u8ba1\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.menu_2.setTitle(QCoreApplication.translate("ImageEditor", u"\u56fe\u50cf\u5904\u7406", None))
        self.blur.setTitle(QCoreApplication.translate("ImageEditor", u"\u6ee4\u6ce2", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("ImageEditor", u"toolBar_2", None))
    # retranslateUi

