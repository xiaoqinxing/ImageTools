# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rawimageeditor_window.ui'
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
        ImageEditor.resize(811, 621)
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
        self.medianblur = QAction(ImageEditor)
        self.medianblur.setObjectName(u"medianblur")
        self.medianblur.setShortcutContext(Qt.WindowShortcut)
        self.bilateralblur = QAction(ImageEditor)
        self.bilateralblur.setObjectName(u"bilateralblur")
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

        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)

        self.height = QSpinBox(self.groupBox)
        self.height.setObjectName(u"height")
        self.height.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.height.setMaximum(10000)

        self.gridLayout_4.addWidget(self.height, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 3, 0, 1, 1)

        self.width = QSpinBox(self.groupBox)
        self.width.setObjectName(u"width")
        self.width.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.width.setMaximum(10000)

        self.gridLayout_4.addWidget(self.width, 0, 1, 1, 1)

        self.bit = QSpinBox(self.groupBox)
        self.bit.setObjectName(u"bit")
        self.bit.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_4.addWidget(self.bit, 2, 1, 1, 1)

        self.raw_format = QComboBox(self.groupBox)
        self.raw_format.addItem("")
        self.raw_format.addItem("")
        self.raw_format.addItem("")
        self.raw_format.setObjectName(u"raw_format")

        self.gridLayout_4.addWidget(self.raw_format, 3, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 4, 0, 1, 1)

        self.pattern = QComboBox(self.groupBox)
        self.pattern.addItem("")
        self.pattern.addItem("")
        self.pattern.addItem("")
        self.pattern.addItem("")
        self.pattern.setObjectName(u"pattern")

        self.gridLayout_4.addWidget(self.pattern, 4, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rolloff = QCheckBox(self.groupBox_2)
        self.rolloff.setObjectName(u"rolloff")

        self.gridLayout_2.addWidget(self.rolloff, 1, 0, 1, 1)

        self.demosaic = QCheckBox(self.groupBox_2)
        self.demosaic.setObjectName(u"demosaic")

        self.gridLayout_2.addWidget(self.demosaic, 3, 0, 1, 1)

        self.LTM = QCheckBox(self.groupBox_2)
        self.LTM.setObjectName(u"LTM")

        self.gridLayout_2.addWidget(self.LTM, 7, 0, 1, 1)

        self.blacklevel = QCheckBox(self.groupBox_2)
        self.blacklevel.setObjectName(u"blacklevel")

        self.gridLayout_2.addWidget(self.blacklevel, 0, 0, 1, 1)

        self.awb = QCheckBox(self.groupBox_2)
        self.awb.setObjectName(u"awb")

        self.gridLayout_2.addWidget(self.awb, 4, 0, 1, 1)

        self.ABF = QCheckBox(self.groupBox_2)
        self.ABF.setObjectName(u"ABF")

        self.gridLayout_2.addWidget(self.ABF, 2, 0, 1, 1)

        self.denoise = QCheckBox(self.groupBox_2)
        self.denoise.setObjectName(u"denoise")

        self.gridLayout_2.addWidget(self.denoise, 9, 0, 1, 1)

        self.asf = QCheckBox(self.groupBox_2)
        self.asf.setObjectName(u"asf")

        self.gridLayout_2.addWidget(self.asf, 10, 0, 1, 1)

        self.ccm = QCheckBox(self.groupBox_2)
        self.ccm.setObjectName(u"ccm")

        self.gridLayout_2.addWidget(self.ccm, 5, 0, 1, 1)

        self.gamma = QCheckBox(self.groupBox_2)
        self.gamma.setObjectName(u"gamma")

        self.gridLayout_2.addWidget(self.gamma, 6, 0, 1, 1)

        self.chroma_enhance = QCheckBox(self.groupBox_2)
        self.chroma_enhance.setObjectName(u"chroma_enhance")

        self.gridLayout_2.addWidget(self.chroma_enhance, 8, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        ImageEditor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ImageEditor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 811, 23))
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.blur = QMenu(self.menu_2)
        self.blur.setObjectName(u"blur")
        ImageEditor.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(ImageEditor)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMouseTracking(True)
        ImageEditor.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menu_2.menuAction())
        self.menu_2.addAction(self.blur.menuAction())
        self.blur.addAction(self.boxblur)
        self.blur.addAction(self.guassian)
        self.blur.addAction(self.medianblur)
        self.blur.addAction(self.bilateralblur)

        self.retranslateUi(ImageEditor)

        QMetaObject.connectSlotsByName(ImageEditor)
    # setupUi

    def retranslateUi(self, ImageEditor):
        ImageEditor.setWindowTitle(QCoreApplication.translate("ImageEditor", u"RAW\u56fe\u5904\u7406\u5de5\u5177", None))
#if QT_CONFIG(tooltip)
        ImageEditor.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.historgram.setText(QCoreApplication.translate("ImageEditor", u"\u76f4\u65b9\u56fe", None))
        self.statics.setText(QCoreApplication.translate("ImageEditor", u"\u7edf\u8ba1\u4fe1\u606f", None))
        self.boxblur.setText(QCoreApplication.translate("ImageEditor", u"\u65b9\u6846\u6ee4\u6ce2", None))
        self.guassian.setText(QCoreApplication.translate("ImageEditor", u"\u9ad8\u65af\u6ee4\u6ce2", None))
        self.medianblur.setText(QCoreApplication.translate("ImageEditor", u"\u4e2d\u503c\u6ee4\u6ce2", None))
        self.bilateralblur.setText(QCoreApplication.translate("ImageEditor", u"\u53cc\u8fb9\u6ee4\u6ce2", None))
        self.groupBox.setTitle(QCoreApplication.translate("ImageEditor", u"raw\u56fe\u8bbe\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("ImageEditor", u"\u9ad8", None))
        self.label_7.setText(QCoreApplication.translate("ImageEditor", u"\u5bbd", None))
        self.label_8.setText(QCoreApplication.translate("ImageEditor", u"\u50cf\u7d20\u70b9\u4f4d\u6570", None))
        self.label_9.setText(QCoreApplication.translate("ImageEditor", u"RAW\u683c\u5f0f", None))
        self.raw_format.setItemText(0, QCoreApplication.translate("ImageEditor", u"MIPI", None))
        self.raw_format.setItemText(1, QCoreApplication.translate("ImageEditor", u"PACKED", None))
        self.raw_format.setItemText(2, QCoreApplication.translate("ImageEditor", u"UNPACKED", None))

        self.label_10.setText(QCoreApplication.translate("ImageEditor", u"pattern", None))
        self.pattern.setItemText(0, QCoreApplication.translate("ImageEditor", u"RGGB", None))
        self.pattern.setItemText(1, QCoreApplication.translate("ImageEditor", u"GRBG", None))
        self.pattern.setItemText(2, QCoreApplication.translate("ImageEditor", u"BGGR", None))
        self.pattern.setItemText(3, QCoreApplication.translate("ImageEditor", u"GBRG", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("ImageEditor", u"ISP\u5904\u7406\u6d41\u7a0b", None))
        self.rolloff.setText(QCoreApplication.translate("ImageEditor", u"rolloff", None))
        self.demosaic.setText(QCoreApplication.translate("ImageEditor", u"demosaic", None))
        self.LTM.setText(QCoreApplication.translate("ImageEditor", u"LTM", None))
        self.blacklevel.setText(QCoreApplication.translate("ImageEditor", u"black level", None))
        self.awb.setText(QCoreApplication.translate("ImageEditor", u"awb", None))
        self.ABF.setText(QCoreApplication.translate("ImageEditor", u"ABF", None))
        self.denoise.setText(QCoreApplication.translate("ImageEditor", u"wavelet denoise", None))
        self.asf.setText(QCoreApplication.translate("ImageEditor", u"adaptive spatial filter", None))
        self.ccm.setText(QCoreApplication.translate("ImageEditor", u"ccm", None))
        self.gamma.setText(QCoreApplication.translate("ImageEditor", u"gamma", None))
        self.chroma_enhance.setText(QCoreApplication.translate("ImageEditor", u"advanced chroma enhancement", None))
        self.menu_2.setTitle(QCoreApplication.translate("ImageEditor", u"\u56fe\u50cf\u5904\u7406", None))
        self.blur.setTitle(QCoreApplication.translate("ImageEditor", u"\u6ee4\u6ce2", None))
    # retranslateUi

