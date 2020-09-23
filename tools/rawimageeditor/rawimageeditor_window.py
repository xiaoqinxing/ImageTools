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
        ImageEditor.resize(680, 577)
        ImageEditor.setContextMenuPolicy(Qt.DefaultContextMenu)
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
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(400, 16777215))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pattern = QComboBox(self.groupBox)
        self.pattern.addItem("")
        self.pattern.addItem("")
        self.pattern.addItem("")
        self.pattern.addItem("")
        self.pattern.setObjectName(u"pattern")

        self.gridLayout_4.addWidget(self.pattern, 4, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)

        self.raw_format = QComboBox(self.groupBox)
        self.raw_format.addItem("")
        self.raw_format.addItem("")
        self.raw_format.addItem("")
        self.raw_format.setObjectName(u"raw_format")

        self.gridLayout_4.addWidget(self.raw_format, 3, 1, 1, 1)

        self.height = QSpinBox(self.groupBox)
        self.height.setObjectName(u"height")
        self.height.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.height.setMaximum(10000)

        self.gridLayout_4.addWidget(self.height, 1, 1, 1, 1)

        self.width = QSpinBox(self.groupBox)
        self.width.setObjectName(u"width")
        self.width.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.width.setMaximum(10000)

        self.gridLayout_4.addWidget(self.width, 0, 1, 1, 1)

        self.bit = QSpinBox(self.groupBox)
        self.bit.setObjectName(u"bit")
        self.bit.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_4.addWidget(self.bit, 2, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 4, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_4)

        self.open_image = QPushButton(self.groupBox)
        self.open_image.setObjectName(u"open_image")

        self.verticalLayout_2.addWidget(self.open_image)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pipeline = QListWidget(self.groupBox_2)
        brush = QBrush(QColor(85, 255, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        __qlistwidgetitem = QListWidgetItem(self.pipeline)
        __qlistwidgetitem.setCheckState(Qt.Unchecked);
        __qlistwidgetitem.setBackground(brush);
        __qlistwidgetitem1 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem1.setCheckState(Qt.Unchecked);
        __qlistwidgetitem1.setBackground(brush);
        __qlistwidgetitem2 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem2.setCheckState(Qt.Unchecked);
        __qlistwidgetitem2.setBackground(brush);
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qlistwidgetitem3 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem3.setCheckState(Qt.Unchecked);
        __qlistwidgetitem3.setBackground(brush1);
        brush2 = QBrush(QColor(255, 255, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        __qlistwidgetitem4 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem4.setCheckState(Qt.Unchecked);
        __qlistwidgetitem4.setBackground(brush2);
        __qlistwidgetitem5 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem5.setCheckState(Qt.Unchecked);
        __qlistwidgetitem5.setBackground(brush2);
        __qlistwidgetitem6 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem6.setCheckState(Qt.Unchecked);
        __qlistwidgetitem6.setBackground(brush2);
        __qlistwidgetitem7 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem7.setCheckState(Qt.Unchecked);
        __qlistwidgetitem7.setBackground(brush2);
        __qlistwidgetitem8 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem8.setCheckState(Qt.Unchecked);
        __qlistwidgetitem8.setBackground(brush1);
        brush3 = QBrush(QColor(170, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        __qlistwidgetitem9 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem9.setCheckState(Qt.Unchecked);
        __qlistwidgetitem9.setBackground(brush3);
        __qlistwidgetitem10 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem10.setCheckState(Qt.Unchecked);
        __qlistwidgetitem10.setBackground(brush3);
        self.pipeline.setObjectName(u"pipeline")
        font = QFont()
        font.setPointSize(12)
        self.pipeline.setFont(font)
        self.pipeline.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.pipeline.setDragDropMode(QAbstractItemView.DragDrop)
        self.pipeline.setDefaultDropAction(Qt.MoveAction)
        self.pipeline.setAlternatingRowColors(False)
        self.pipeline.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pipeline.setMovement(QListView.Free)
        self.pipeline.setResizeMode(QListView.Adjust)
        self.pipeline.setLayoutMode(QListView.SinglePass)
        self.pipeline.setWordWrap(True)
        self.pipeline.setSelectionRectVisible(True)
        self.pipeline.setSortingEnabled(False)

        self.gridLayout_2.addWidget(self.pipeline, 1, 1, 1, 1)

        self.pipeline_ok = QPushButton(self.groupBox_2)
        self.pipeline_ok.setObjectName(u"pipeline_ok")

        self.gridLayout_2.addWidget(self.pipeline_ok, 2, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea = QScrollArea(self.groupBox_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 549, 249))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_13 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_13.setObjectName(u"groupBox_13")

        self.gridLayout_7.addWidget(self.groupBox_13, 8, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_14.setObjectName(u"groupBox_14")

        self.gridLayout_7.addWidget(self.groupBox_14, 9, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_10.setObjectName(u"groupBox_10")

        self.gridLayout_7.addWidget(self.groupBox_10, 5, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_9.setObjectName(u"groupBox_9")

        self.gridLayout_7.addWidget(self.groupBox_9, 4, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")

        self.gridLayout_7.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_12.setObjectName(u"groupBox_12")

        self.gridLayout_7.addWidget(self.groupBox_12, 7, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 6, 1, 1)

        self.spinBox_3 = QSpinBox(self.groupBox_4)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout_3.addWidget(self.spinBox_3, 0, 5, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox_4)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_3.addWidget(self.spinBox_2, 0, 3, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_4)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_3.addWidget(self.spinBox, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 4, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox_4)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout_3.addWidget(self.spinBox_4, 0, 7, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_8.setObjectName(u"groupBox_8")

        self.gridLayout_7.addWidget(self.groupBox_8, 3, 0, 1, 1)

        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_11.setObjectName(u"groupBox_11")

        self.gridLayout_7.addWidget(self.groupBox_11, 6, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_7.setObjectName(u"groupBox_7")

        self.gridLayout_7.addWidget(self.groupBox_7, 2, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_15.setObjectName(u"groupBox_15")

        self.gridLayout_7.addWidget(self.groupBox_15, 10, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_5 = QGridLayout(self.groupBox_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGridLayout()
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addLayout(self.graphicsView, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_6, 1, 0, 1, 1)

        ImageEditor.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(ImageEditor)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMouseTracking(True)
        ImageEditor.setStatusBar(self.statusBar)

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
        self.pattern.setItemText(0, QCoreApplication.translate("ImageEditor", u"RGGB", None))
        self.pattern.setItemText(1, QCoreApplication.translate("ImageEditor", u"GRBG", None))
        self.pattern.setItemText(2, QCoreApplication.translate("ImageEditor", u"BGGR", None))
        self.pattern.setItemText(3, QCoreApplication.translate("ImageEditor", u"GBRG", None))

        self.label_6.setText(QCoreApplication.translate("ImageEditor", u"\u9ad8", None))
        self.raw_format.setItemText(0, QCoreApplication.translate("ImageEditor", u"MIPI", None))
        self.raw_format.setItemText(1, QCoreApplication.translate("ImageEditor", u"PACKED", None))
        self.raw_format.setItemText(2, QCoreApplication.translate("ImageEditor", u"UNPACKED", None))

        self.label_9.setText(QCoreApplication.translate("ImageEditor", u"RAW\u683c\u5f0f", None))
        self.label_10.setText(QCoreApplication.translate("ImageEditor", u"pattern", None))
        self.label_7.setText(QCoreApplication.translate("ImageEditor", u"\u5bbd", None))
        self.label_8.setText(QCoreApplication.translate("ImageEditor", u"\u50cf\u7d20\u70b9\u4f4d\u6570", None))
        self.open_image.setText(QCoreApplication.translate("ImageEditor", u"\u6253\u5f00\u56fe\u7247", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ImageEditor", u"ISP\u5904\u7406\u6d41\u7a0b", None))

        __sortingEnabled = self.pipeline.isSortingEnabled()
        self.pipeline.setSortingEnabled(False)
        ___qlistwidgetitem = self.pipeline.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ImageEditor", u"black level", None));
        ___qlistwidgetitem1 = self.pipeline.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("ImageEditor", u"rolloff", None));
        ___qlistwidgetitem2 = self.pipeline.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("ImageEditor", u"ABF", None));
        ___qlistwidgetitem3 = self.pipeline.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("ImageEditor", u"demosaic", None));
        ___qlistwidgetitem4 = self.pipeline.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("ImageEditor", u"awb", None));
        ___qlistwidgetitem5 = self.pipeline.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("ImageEditor", u"ccm", None));
        ___qlistwidgetitem6 = self.pipeline.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("ImageEditor", u"gamma", None));
        ___qlistwidgetitem7 = self.pipeline.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("ImageEditor", u"LTM", None));
        ___qlistwidgetitem8 = self.pipeline.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("ImageEditor", u"advanced chroma enhancement", None));
        ___qlistwidgetitem9 = self.pipeline.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("ImageEditor", u"wavelet denoise", None));
        ___qlistwidgetitem10 = self.pipeline.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("ImageEditor", u"adaptive spatial filter", None));
        self.pipeline.setSortingEnabled(__sortingEnabled)

        self.pipeline_ok.setText(QCoreApplication.translate("ImageEditor", u"\u786e\u5b9a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ImageEditor", u"ISP\u53c2\u6570", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("ImageEditor", u"advanced chroma enhancement", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("ImageEditor", u"wavelet denoise", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("ImageEditor", u"ccm", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("ImageEditor", u"awb", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ImageEditor", u"rolloff", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("ImageEditor", u"LTM", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ImageEditor", u"black level", None))
        self.label_2.setText(QCoreApplication.translate("ImageEditor", u"GR", None))
        self.label_4.setText(QCoreApplication.translate("ImageEditor", u"B", None))
        self.label.setText(QCoreApplication.translate("ImageEditor", u"R", None))
        self.label_3.setText(QCoreApplication.translate("ImageEditor", u"GB", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("ImageEditor", u"demosaic", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("ImageEditor", u"gamma", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("ImageEditor", u"ABF", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("ImageEditor", u"adaptive spatial filter", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("ImageEditor", u"\u56fe\u7247\u9884\u89c8", None))
    # retranslateUi

