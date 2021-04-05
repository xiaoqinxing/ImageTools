# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rawimageeditor_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_ImageEditor(object):
    def setupUi(self, ImageEditor):
        if not ImageEditor.objectName():
            ImageEditor.setObjectName(u"ImageEditor")
        ImageEditor.resize(495, 577)
        ImageEditor.setFocusPolicy(Qt.ClickFocus)
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
        self.groupBox.setMaximumSize(QSize(164, 16777215))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 6, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 5, 0, 1, 1)

        self.pattern = QComboBox(self.groupBox)
        self.pattern.addItem("")
        self.pattern.addItem("")
        self.pattern.addItem("")
        self.pattern.addItem("")
        self.pattern.setObjectName(u"pattern")

        self.gridLayout_4.addWidget(self.pattern, 6, 1, 1, 1)

        self.raw_format = QComboBox(self.groupBox)
        self.raw_format.addItem("")
        self.raw_format.addItem("")
        self.raw_format.addItem("")
        self.raw_format.setObjectName(u"raw_format")

        self.gridLayout_4.addWidget(self.raw_format, 5, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 4, 0, 1, 1)

        self.width = QSpinBox(self.groupBox)
        self.width.setObjectName(u"width")
        self.width.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.width.setMaximum(8096)

        self.gridLayout_4.addWidget(self.width, 2, 1, 1, 1)

        self.height = QSpinBox(self.groupBox)
        self.height.setObjectName(u"height")
        self.height.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.height.setMaximum(8096)

        self.gridLayout_4.addWidget(self.height, 3, 1, 1, 1)

        self.bit = QSpinBox(self.groupBox)
        self.bit.setObjectName(u"bit")
        self.bit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bit.setMaximum(16)

        self.gridLayout_4.addWidget(self.bit, 4, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.filename = QLineEdit(self.groupBox)
        self.filename.setObjectName(u"filename")

        self.verticalLayout_2.addWidget(self.filename)

        self.open_image = QPushButton(self.groupBox)
        self.open_image.setObjectName(u"open_image")

        self.verticalLayout_2.addWidget(self.open_image)

        self.save_image = QPushButton(self.groupBox)
        self.save_image.setObjectName(u"save_image")

        self.verticalLayout_2.addWidget(self.save_image)

        self.analysis_img = QPushButton(self.groupBox)
        self.analysis_img.setObjectName(u"analysis_img")

        self.verticalLayout_2.addWidget(self.analysis_img)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(227, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pipeline_ok = QPushButton(self.groupBox_2)
        self.pipeline_ok.setObjectName(u"pipeline_ok")

        self.gridLayout_2.addWidget(self.pipeline_ok, 3, 1, 1, 1)

        self.pipeline = QListWidget(self.groupBox_2)
        __qlistwidgetitem = QListWidgetItem(self.pipeline)
        __qlistwidgetitem.setCheckState(Qt.Checked);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        brush = QBrush(QColor(85, 255, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        __qlistwidgetitem1 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem1.setCheckState(Qt.Unchecked);
        __qlistwidgetitem1.setBackground(brush);
        __qlistwidgetitem2 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem2.setCheckState(Qt.Unchecked);
        __qlistwidgetitem2.setBackground(brush);
        __qlistwidgetitem3 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem3.setCheckState(Qt.Unchecked);
        __qlistwidgetitem3.setBackground(brush);
        __qlistwidgetitem4 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem4.setCheckState(Qt.Unchecked);
        __qlistwidgetitem4.setBackground(brush);
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qlistwidgetitem5 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem5.setCheckState(Qt.Unchecked);
        __qlistwidgetitem5.setBackground(brush1);
        brush2 = QBrush(QColor(255, 255, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        __qlistwidgetitem6 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem6.setCheckState(Qt.Unchecked);
        __qlistwidgetitem6.setBackground(brush2);
        __qlistwidgetitem7 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem7.setCheckState(Qt.Unchecked);
        __qlistwidgetitem7.setBackground(brush2);
        __qlistwidgetitem8 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem8.setCheckState(Qt.Unchecked);
        __qlistwidgetitem8.setBackground(brush2);
        __qlistwidgetitem9 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem9.setCheckState(Qt.Unchecked);
        __qlistwidgetitem9.setBackground(brush2);
        __qlistwidgetitem10 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem10.setCheckState(Qt.Unchecked);
        __qlistwidgetitem10.setBackground(brush1);
        brush3 = QBrush(QColor(170, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        __qlistwidgetitem11 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem11.setCheckState(Qt.Unchecked);
        __qlistwidgetitem11.setBackground(brush3);
        __qlistwidgetitem12 = QListWidgetItem(self.pipeline)
        __qlistwidgetitem12.setCheckState(Qt.Unchecked);
        __qlistwidgetitem12.setBackground(brush3);
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

        self.reload = QPushButton(self.groupBox_2)
        self.reload.setObjectName(u"reload")

        self.gridLayout_2.addWidget(self.reload, 2, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(399, 16777215))
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea = QScrollArea(self.groupBox_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 364, 743))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_14 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_14.setObjectName(u"groupBox_14")

        self.gridLayout_7.addWidget(self.groupBox_14, 10, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_11 = QGridLayout(self.groupBox_12)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.dark_boost = QSlider(self.groupBox_12)
        self.dark_boost.setObjectName(u"dark_boost")
        self.dark_boost.setMaximum(300)
        self.dark_boost.setSingleStep(10)
        self.dark_boost.setPageStep(50)
        self.dark_boost.setValue(100)
        self.dark_boost.setOrientation(Qt.Horizontal)

        self.gridLayout_11.addWidget(self.dark_boost, 0, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_12)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_11.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_12)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_11.addWidget(self.label_15, 1, 0, 1, 1)

        self.bright_suppress = QSlider(self.groupBox_12)
        self.bright_suppress.setObjectName(u"bright_suppress")
        self.bright_suppress.setMaximum(300)
        self.bright_suppress.setSingleStep(10)
        self.bright_suppress.setPageStep(50)
        self.bright_suppress.setValue(100)
        self.bright_suppress.setOrientation(Qt.Horizontal)

        self.gridLayout_11.addWidget(self.bright_suppress, 1, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_12, 8, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 5, 1, 1)

        self.blc_b = QSpinBox(self.groupBox_4)
        self.blc_b.setObjectName(u"blc_b")
        self.blc_b.setMaximum(10000)

        self.gridLayout_3.addWidget(self.blc_b, 0, 8, 1, 1)

        self.blc_gb = QSpinBox(self.groupBox_4)
        self.blc_gb.setObjectName(u"blc_gb")
        self.blc_gb.setMaximum(1000)

        self.gridLayout_3.addWidget(self.blc_gb, 0, 6, 1, 1)

        self.blc_gr = QSpinBox(self.groupBox_4)
        self.blc_gr.setObjectName(u"blc_gr")
        self.blc_gr.setMaximum(10000)

        self.gridLayout_3.addWidget(self.blc_gr, 0, 4, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 7, 1, 1)

        self.blc_r = QSpinBox(self.groupBox_4)
        self.blc_r.setObjectName(u"blc_r")
        self.blc_r.setMaximum(10000)

        self.gridLayout_3.addWidget(self.blc_r, 0, 2, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_7.setObjectName(u"groupBox_7")

        self.gridLayout_7.addWidget(self.groupBox_7, 3, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_13 = QGridLayout(self.groupBox_13)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.saturation = QSlider(self.groupBox_13)
        self.saturation.setObjectName(u"saturation")
        self.saturation.setMaximum(100)
        self.saturation.setValue(50)
        self.saturation.setOrientation(Qt.Horizontal)

        self.gridLayout_13.addWidget(self.saturation, 5, 1, 1, 1)

        self.hue = QSlider(self.groupBox_13)
        self.hue.setObjectName(u"hue")
        self.hue.setMaximum(100)
        self.hue.setValue(50)
        self.hue.setOrientation(Qt.Horizontal)

        self.gridLayout_13.addWidget(self.hue, 4, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_13)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_13.addWidget(self.label_16, 2, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_13)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_13.addWidget(self.label_18, 4, 0, 1, 1)

        self.limitrange = QCheckBox(self.groupBox_13)
        self.limitrange.setObjectName(u"limitrange")

        self.gridLayout_13.addWidget(self.limitrange, 0, 0, 1, 2)

        self.luma = QSlider(self.groupBox_13)
        self.luma.setObjectName(u"luma")
        self.luma.setMaximum(100)
        self.luma.setValue(50)
        self.luma.setOrientation(Qt.Horizontal)

        self.gridLayout_13.addWidget(self.luma, 2, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_13)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_13.addWidget(self.label_17, 3, 0, 1, 1)

        self.contrast = QSlider(self.groupBox_13)
        self.contrast.setObjectName(u"contrast")
        self.contrast.setMaximum(100)
        self.contrast.setValue(50)
        self.contrast.setOrientation(Qt.Horizontal)

        self.gridLayout_13.addWidget(self.contrast, 3, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_13)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_13.addWidget(self.label_19, 5, 0, 1, 1)

        self.color_space = QComboBox(self.groupBox_13)
        self.color_space.addItem("")
        self.color_space.addItem("")
        self.color_space.addItem("")
        self.color_space.setObjectName(u"color_space")
        self.color_space.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_13.addWidget(self.color_space, 1, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_13)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_13.addWidget(self.label_20, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_13, 9, 0, 1, 1)

        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_9 = QGridLayout(self.groupBox_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_13 = QLabel(self.groupBox_11)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_9.addWidget(self.label_13, 0, 0, 1, 1)

        self.gamma_ratio = QDoubleSpinBox(self.groupBox_11)
        self.gamma_ratio.setObjectName(u"gamma_ratio")
        self.gamma_ratio.setValue(2.200000000000000)

        self.gridLayout_9.addWidget(self.gamma_ratio, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_11, 7, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_12 = QGridLayout(self.groupBox_10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_22 = QLabel(self.groupBox_10)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_2.addWidget(self.label_22)

        self.ccm_rr = QDoubleSpinBox(self.groupBox_10)
        self.ccm_rr.setObjectName(u"ccm_rr")
        self.ccm_rr.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ccm_rr.setDecimals(3)
        self.ccm_rr.setMinimum(-8.000000000000000)
        self.ccm_rr.setMaximum(8.000000000000000)
        self.ccm_rr.setValue(1.000000000000000)

        self.horizontalLayout_2.addWidget(self.ccm_rr)

        self.label_23 = QLabel(self.groupBox_10)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_2.addWidget(self.label_23)

        self.ccm_rg = QDoubleSpinBox(self.groupBox_10)
        self.ccm_rg.setObjectName(u"ccm_rg")
        self.ccm_rg.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ccm_rg.setDecimals(3)
        self.ccm_rg.setMinimum(-8.000000000000000)
        self.ccm_rg.setMaximum(8.000000000000000)

        self.horizontalLayout_2.addWidget(self.ccm_rg)

        self.label_24 = QLabel(self.groupBox_10)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_2.addWidget(self.label_24)

        self.ccm_rb = QDoubleSpinBox(self.groupBox_10)
        self.ccm_rb.setObjectName(u"ccm_rb")
        self.ccm_rb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ccm_rb.setDecimals(3)
        self.ccm_rb.setMinimum(-8.000000000000000)
        self.ccm_rb.setMaximum(8.000000000000000)

        self.horizontalLayout_2.addWidget(self.ccm_rb)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_25 = QLabel(self.groupBox_10)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_4.addWidget(self.label_25)

        self.ccm_gr = QDoubleSpinBox(self.groupBox_10)
        self.ccm_gr.setObjectName(u"ccm_gr")
        self.ccm_gr.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ccm_gr.setDecimals(3)
        self.ccm_gr.setMinimum(-8.000000000000000)
        self.ccm_gr.setMaximum(8.000000000000000)

        self.horizontalLayout_4.addWidget(self.ccm_gr)

        self.label_26 = QLabel(self.groupBox_10)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_4.addWidget(self.label_26)

        self.ccm_gg = QDoubleSpinBox(self.groupBox_10)
        self.ccm_gg.setObjectName(u"ccm_gg")
        self.ccm_gg.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ccm_gg.setDecimals(3)
        self.ccm_gg.setMinimum(-8.000000000000000)
        self.ccm_gg.setMaximum(8.000000000000000)
        self.ccm_gg.setValue(1.000000000000000)

        self.horizontalLayout_4.addWidget(self.ccm_gg)

        self.label_27 = QLabel(self.groupBox_10)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_4.addWidget(self.label_27)

        self.ccm_gb = QDoubleSpinBox(self.groupBox_10)
        self.ccm_gb.setObjectName(u"ccm_gb")
        self.ccm_gb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ccm_gb.setDecimals(3)
        self.ccm_gb.setMinimum(-8.000000000000000)
        self.ccm_gb.setMaximum(8.000000000000000)

        self.horizontalLayout_4.addWidget(self.ccm_gb)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_28 = QLabel(self.groupBox_10)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_5.addWidget(self.label_28)

        self.ccm_br = QDoubleSpinBox(self.groupBox_10)
        self.ccm_br.setObjectName(u"ccm_br")
        self.ccm_br.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ccm_br.setDecimals(3)
        self.ccm_br.setMinimum(-8.000000000000000)
        self.ccm_br.setMaximum(8.000000000000000)

        self.horizontalLayout_5.addWidget(self.ccm_br)

        self.label_29 = QLabel(self.groupBox_10)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_5.addWidget(self.label_29)

        self.ccm_bg = QDoubleSpinBox(self.groupBox_10)
        self.ccm_bg.setObjectName(u"ccm_bg")
        self.ccm_bg.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ccm_bg.setDecimals(3)
        self.ccm_bg.setMinimum(-8.000000000000000)
        self.ccm_bg.setMaximum(8.000000000000000)

        self.horizontalLayout_5.addWidget(self.ccm_bg)

        self.label_30 = QLabel(self.groupBox_10)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_5.addWidget(self.label_30)

        self.ccm_bb = QDoubleSpinBox(self.groupBox_10)
        self.ccm_bb.setObjectName(u"ccm_bb")
        self.ccm_bb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ccm_bb.setDecimals(3)
        self.ccm_bb.setMinimum(-8.000000000000000)
        self.ccm_bb.setMaximum(8.000000000000000)
        self.ccm_bb.setValue(1.000000000000000)

        self.horizontalLayout_5.addWidget(self.ccm_bb)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.gridLayout_12.addLayout(self.verticalLayout_3, 1, 4, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_10, 6, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_14 = QGridLayout(self.groupBox_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.inputflatphoto = QPushButton(self.groupBox_5)
        self.inputflatphoto.setObjectName(u"inputflatphoto")

        self.gridLayout_14.addWidget(self.inputflatphoto, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_5, 2, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_8 = QGridLayout(self.groupBox_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.awb_r = QDoubleSpinBox(self.groupBox_9)
        self.awb_r.setObjectName(u"awb_r")
        self.awb_r.setDecimals(3)
        self.awb_r.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.awb_r, 0, 2, 1, 1)

        self.awb_g = QDoubleSpinBox(self.groupBox_9)
        self.awb_g.setObjectName(u"awb_g")
        self.awb_g.setDecimals(3)
        self.awb_g.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.awb_g, 0, 4, 1, 1)

        self.label_12 = QLabel(self.groupBox_9)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_8.addWidget(self.label_12, 0, 5, 1, 1)

        self.label_5 = QLabel(self.groupBox_9)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_8.addWidget(self.label_5, 0, 1, 1, 1)

        self.awb_b = QDoubleSpinBox(self.groupBox_9)
        self.awb_b.setObjectName(u"awb_b")
        self.awb_b.setDecimals(3)
        self.awb_b.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.awb_b, 0, 6, 1, 1)

        self.label_11 = QLabel(self.groupBox_9)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_8.addWidget(self.label_11, 0, 3, 1, 1)

        self.select_from_raw = QPushButton(self.groupBox_9)
        self.select_from_raw.setObjectName(u"select_from_raw")

        self.gridLayout_8.addWidget(self.select_from_raw, 0, 7, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_9, 5, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_10 = QGridLayout(self.groupBox_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.demosaic_type = QComboBox(self.groupBox_8)
        self.demosaic_type.addItem("")
        self.demosaic_type.addItem("")
        self.demosaic_type.addItem("")
        self.demosaic_type.setObjectName(u"demosaic_type")

        self.gridLayout_10.addWidget(self.demosaic_type, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_8, 4, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_15.setObjectName(u"groupBox_15")

        self.gridLayout_7.addWidget(self.groupBox_15, 11, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_15 = QGridLayout(self.groupBox_6)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_21 = QLabel(self.groupBox_6)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_15.addWidget(self.label_21, 0, 0, 1, 1)

        self.badpixelcorrection = QSlider(self.groupBox_6)
        self.badpixelcorrection.setObjectName(u"badpixelcorrection")
        self.badpixelcorrection.setMaximum(2)
        self.badpixelcorrection.setOrientation(Qt.Horizontal)

        self.gridLayout_15.addWidget(self.badpixelcorrection, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_6, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.photo_title = QGroupBox(self.centralwidget)
        self.photo_title.setObjectName(u"photo_title")
        self.gridLayout_5 = QGridLayout(self.photo_title)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGridLayout()
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addLayout(self.graphicsView, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.photo_title, 1, 0, 1, 1)

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
        self.label_10.setText(QCoreApplication.translate("ImageEditor", u"pattern", None))
        self.label_6.setText(QCoreApplication.translate("ImageEditor", u"\u9ad8", None))
        self.label_9.setText(QCoreApplication.translate("ImageEditor", u"RAW\u683c\u5f0f", None))
        self.pattern.setItemText(0, QCoreApplication.translate("ImageEditor", u"RGGB", None))
        self.pattern.setItemText(1, QCoreApplication.translate("ImageEditor", u"GRBG", None))
        self.pattern.setItemText(2, QCoreApplication.translate("ImageEditor", u"BGGR", None))
        self.pattern.setItemText(3, QCoreApplication.translate("ImageEditor", u"GBRG", None))

        self.raw_format.setItemText(0, QCoreApplication.translate("ImageEditor", u"MIPI", None))
        self.raw_format.setItemText(1, QCoreApplication.translate("ImageEditor", u"PACKED", None))
        self.raw_format.setItemText(2, QCoreApplication.translate("ImageEditor", u"UNPACKED", None))

        self.label_7.setText(QCoreApplication.translate("ImageEditor", u"\u5bbd", None))
        self.label_8.setText(QCoreApplication.translate("ImageEditor", u"\u50cf\u7d20\u70b9\u4f4d\u6570", None))
        self.open_image.setText(QCoreApplication.translate("ImageEditor", u"\u6253\u5f00\u56fe\u7247", None))
        self.save_image.setText(QCoreApplication.translate("ImageEditor", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.analysis_img.setText(QCoreApplication.translate("ImageEditor", u"\u56fe\u7247\u5206\u6790", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ImageEditor", u"ISP\u5904\u7406\u6d41\u7a0b", None))
        self.pipeline_ok.setText(QCoreApplication.translate("ImageEditor", u"\u786e\u5b9a", None))

        __sortingEnabled = self.pipeline.isSortingEnabled()
        self.pipeline.setSortingEnabled(False)
        ___qlistwidgetitem = self.pipeline.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ImageEditor", u"original raw", None));
        ___qlistwidgetitem1 = self.pipeline.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("ImageEditor", u"black level", None));
        ___qlistwidgetitem2 = self.pipeline.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("ImageEditor", u"bad pixel correction", None));
        ___qlistwidgetitem3 = self.pipeline.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("ImageEditor", u"rolloff", None));
        ___qlistwidgetitem4 = self.pipeline.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("ImageEditor", u"ABF", None));
        ___qlistwidgetitem5 = self.pipeline.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("ImageEditor", u"demosaic", None));
        ___qlistwidgetitem6 = self.pipeline.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("ImageEditor", u"awb", None));
        ___qlistwidgetitem7 = self.pipeline.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("ImageEditor", u"ccm", None));
        ___qlistwidgetitem8 = self.pipeline.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("ImageEditor", u"gamma", None));
        ___qlistwidgetitem9 = self.pipeline.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("ImageEditor", u"LTM", None));
        ___qlistwidgetitem10 = self.pipeline.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("ImageEditor", u"CSC", None));
        ___qlistwidgetitem11 = self.pipeline.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("ImageEditor", u"wavelet denoise", None));
        ___qlistwidgetitem12 = self.pipeline.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("ImageEditor", u"adaptive spatial filter", None));
        self.pipeline.setSortingEnabled(__sortingEnabled)

        self.reload.setText(QCoreApplication.translate("ImageEditor", u"\u7b97\u6cd5\u70ed\u66f4\u65b0", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ImageEditor", u"ISP\u53c2\u6570", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("ImageEditor", u"wavelet denoise", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("ImageEditor", u"LTM", None))
        self.label_14.setText(QCoreApplication.translate("ImageEditor", u"\u6697\u533a\u63d0\u5347    ", None))
        self.label_15.setText(QCoreApplication.translate("ImageEditor", u"\u4eae\u533a\u6291\u5236", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ImageEditor", u"black level", None))
        self.label_2.setText(QCoreApplication.translate("ImageEditor", u"GR", None))
        self.label_3.setText(QCoreApplication.translate("ImageEditor", u"GB", None))
        self.label.setText(QCoreApplication.translate("ImageEditor", u"R", None))
        self.label_4.setText(QCoreApplication.translate("ImageEditor", u"B", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("ImageEditor", u"ABF", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("ImageEditor", u"CSC", None))
        self.label_16.setText(QCoreApplication.translate("ImageEditor", u"\u4eae\u5ea6        ", None))
        self.label_18.setText(QCoreApplication.translate("ImageEditor", u"\u8272\u8c03      ", None))
        self.limitrange.setText(QCoreApplication.translate("ImageEditor", u"\u662f\u5426\u9650\u5236YUV\u7684\u8f93\u51fa\u8303\u56f4\uff0cTV\u6807\u51c6\u9700:16-235,PC\u6807\u51c6:0-255", None))
        self.label_17.setText(QCoreApplication.translate("ImageEditor", u"\u5bf9\u6bd4\u5ea6     ", None))
        self.label_19.setText(QCoreApplication.translate("ImageEditor", u"\u9971\u548c\u5ea6    ", None))
        self.color_space.setItemText(0, QCoreApplication.translate("ImageEditor", u"BT709", None))
        self.color_space.setItemText(1, QCoreApplication.translate("ImageEditor", u"BT2020", None))
        self.color_space.setItemText(2, QCoreApplication.translate("ImageEditor", u"BT601", None))

        self.label_20.setText(QCoreApplication.translate("ImageEditor", u"\u8272\u57df\u6807\u51c6", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("ImageEditor", u"gamma", None))
        self.label_13.setText(QCoreApplication.translate("ImageEditor", u"ratio", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("ImageEditor", u"ccm", None))
        self.label_22.setText(QCoreApplication.translate("ImageEditor", u"RR", None))
        self.label_23.setText(QCoreApplication.translate("ImageEditor", u"RG", None))
        self.label_24.setText(QCoreApplication.translate("ImageEditor", u"RB", None))
        self.label_25.setText(QCoreApplication.translate("ImageEditor", u"GR", None))
        self.label_26.setText(QCoreApplication.translate("ImageEditor", u"GG", None))
        self.label_27.setText(QCoreApplication.translate("ImageEditor", u"GB", None))
        self.label_28.setText(QCoreApplication.translate("ImageEditor", u"BR", None))
        self.label_29.setText(QCoreApplication.translate("ImageEditor", u"BG", None))
        self.label_30.setText(QCoreApplication.translate("ImageEditor", u"BB", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ImageEditor", u"rolloff", None))
        self.inputflatphoto.setText(QCoreApplication.translate("ImageEditor", u"\u5bfc\u5165\u5e73\u573a\u56fe\uff08\u5747\u5300\u5149\u7167\u7684\u56fe\u7247\uff09", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("ImageEditor", u"awb", None))
        self.label_12.setText(QCoreApplication.translate("ImageEditor", u"B", None))
        self.label_5.setText(QCoreApplication.translate("ImageEditor", u"R", None))
        self.label_11.setText(QCoreApplication.translate("ImageEditor", u"G", None))
        self.select_from_raw.setText(QCoreApplication.translate("ImageEditor", u"\u4eceraw\u56fe\u9009\u53d6", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("ImageEditor", u"demosaic", None))
        self.demosaic_type.setItemText(0, QCoreApplication.translate("ImageEditor", u"\u53cc\u7ebf\u6027\u63d2\u503c", None))
        self.demosaic_type.setItemText(1, QCoreApplication.translate("ImageEditor", u"Malvar2004", None))
        self.demosaic_type.setItemText(2, QCoreApplication.translate("ImageEditor", u"Menon2007", None))

        self.groupBox_15.setTitle(QCoreApplication.translate("ImageEditor", u"adaptive spatial filter", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("ImageEditor", u"bad pixel correction", None))
        self.label_21.setText(QCoreApplication.translate("ImageEditor", u"\u68c0\u6d4b\u533a\u57df     ", None))
        self.photo_title.setTitle(QCoreApplication.translate("ImageEditor", u"\u56fe\u7247\u9884\u89c8", None))
    # retranslateUi

