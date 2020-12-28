# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pqtools2code_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PQtoolsToCode(object):
    def setupUi(self, PQtoolsToCode):
        if not PQtoolsToCode.objectName():
            PQtoolsToCode.setObjectName(u"PQtoolsToCode")
        PQtoolsToCode.resize(875, 650)
        PQtoolsToCode.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(PQtoolsToCode)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.det_file = QTextBrowser(self.centralwidget)
        self.det_file.setObjectName(u"det_file")

        self.gridLayout.addWidget(self.det_file, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(320, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)

        self.output_path = QLineEdit(self.groupBox)
        self.output_path.setObjectName(u"output_path")

        self.gridLayout_2.addWidget(self.output_path, 2, 1, 1, 1)

        self.open_output_path = QPushButton(self.groupBox)
        self.open_output_path.setObjectName(u"open_output_path")

        self.gridLayout_2.addWidget(self.open_output_path, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 8, 0, 1, 1)

        self.need_remove_item = QLineEdit(self.groupBox)
        self.need_remove_item.setObjectName(u"need_remove_item")

        self.gridLayout_2.addWidget(self.need_remove_item, 8, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 11, 0, 1, 1)

        self.openxmlfile = QPushButton(self.groupBox)
        self.openxmlfile.setObjectName(u"openxmlfile")

        self.gridLayout_2.addWidget(self.openxmlfile, 1, 0, 1, 1)

        self.author = QLineEdit(self.groupBox)
        self.author.setObjectName(u"author")

        self.gridLayout_2.addWidget(self.author, 7, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 9, 0, 1, 1)

        self.max_line_num = QSpinBox(self.groupBox)
        self.max_line_num.setObjectName(u"max_line_num")
        self.max_line_num.setMinimum(50)
        self.max_line_num.setMaximum(500)
        self.max_line_num.setValue(120)

        self.gridLayout_2.addWidget(self.max_line_num, 4, 1, 1, 1)

        self.product_id = QLineEdit(self.groupBox)
        self.product_id.setObjectName(u"product_id")

        self.gridLayout_2.addWidget(self.product_id, 5, 1, 1, 1)

        self.include_headers = QPlainTextEdit(self.groupBox)
        self.include_headers.setObjectName(u"include_headers")

        self.gridLayout_2.addWidget(self.include_headers, 10, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 10, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 13, 0, 1, 1)

        self.tab_space = QSpinBox(self.groupBox)
        self.tab_space.setObjectName(u"tab_space")
        self.tab_space.setMaximum(6)
        self.tab_space.setValue(4)

        self.gridLayout_2.addWidget(self.tab_space, 3, 1, 1, 1)

        self.output_filename = QLineEdit(self.groupBox)
        self.output_filename.setObjectName(u"output_filename")

        self.gridLayout_2.addWidget(self.output_filename, 6, 1, 1, 1)

        self.xmlfile = QLineEdit(self.groupBox)
        self.xmlfile.setObjectName(u"xmlfile")

        self.gridLayout_2.addWidget(self.xmlfile, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 7, 0, 1, 1)

        self.filter_struct = QPlainTextEdit(self.groupBox)
        self.filter_struct.setObjectName(u"filter_struct")

        self.gridLayout_2.addWidget(self.filter_struct, 9, 1, 1, 1)

        self.copyright = QPlainTextEdit(self.groupBox)
        self.copyright.setObjectName(u"copyright")

        self.gridLayout_2.addWidget(self.copyright, 13, 1, 1, 1)

        self.add_custom_defines = QPlainTextEdit(self.groupBox)
        self.add_custom_defines.setObjectName(u"add_custom_defines")

        self.gridLayout_2.addWidget(self.add_custom_defines, 11, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 12, 0, 1, 1)

        self.custom_define_dict = QPlainTextEdit(self.groupBox)
        self.custom_define_dict.setObjectName(u"custom_define_dict")

        self.gridLayout_2.addWidget(self.custom_define_dict, 12, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.is_const = QCheckBox(self.groupBox)
        self.is_const.setObjectName(u"is_const")
        self.is_const.setChecked(True)

        self.verticalLayout.addWidget(self.is_const)

        self.generate = QPushButton(self.groupBox)
        self.generate.setObjectName(u"generate")

        self.verticalLayout.addWidget(self.generate)


        self.gridLayout.addWidget(self.groupBox, 0, 3, 1, 1, Qt.AlignLeft)

        self.src_file = QTextBrowser(self.centralwidget)
        self.src_file.setObjectName(u"src_file")

        self.gridLayout.addWidget(self.src_file, 0, 0, 1, 1)

        PQtoolsToCode.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(PQtoolsToCode)
        self.statusbar.setObjectName(u"statusbar")
        PQtoolsToCode.setStatusBar(self.statusbar)

        self.retranslateUi(PQtoolsToCode)

        QMetaObject.connectSlotsByName(PQtoolsToCode)
    # setupUi

    def retranslateUi(self, PQtoolsToCode):
        PQtoolsToCode.setWindowTitle(QCoreApplication.translate("PQtoolsToCode", u"PQtools\u8f6c\u4ee3\u7801\u5de5\u5177", None))
        self.groupBox.setTitle(QCoreApplication.translate("PQtoolsToCode", u"\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("PQtoolsToCode", u"TAB\u7684\u7a7a\u683c\u6570", None))
        self.label_2.setText(QCoreApplication.translate("PQtoolsToCode", u"\u4e00\u884c\u6700\u5927\u5b57\u7b26\u6570", None))
        self.open_output_path.setText(QCoreApplication.translate("PQtoolsToCode", u"\u8f93\u51fa\u6587\u4ef6\u8def\u5f84", None))
        self.label_5.setText(QCoreApplication.translate("PQtoolsToCode", u"\u9700\u8981\u53bb\u9664\u7684\u5143\u7d20", None))
        self.need_remove_item.setText(QCoreApplication.translate("PQtoolsToCode", u"rb", None))
        self.label_3.setText(QCoreApplication.translate("PQtoolsToCode", u"\u4ea7\u54c1ID", None))
        self.label_7.setText(QCoreApplication.translate("PQtoolsToCode", u"\u81ea\u5b9a\u4e49\u7ed3\u6784\u4f53", None))
        self.openxmlfile.setText(QCoreApplication.translate("PQtoolsToCode", u"\u6253\u5f00xml\u6587\u4ef6", None))
        self.author.setText(QCoreApplication.translate("PQtoolsToCode", u"liqinxing", None))
        self.label_10.setText(QCoreApplication.translate("PQtoolsToCode", u"\u9700\u8981\u8f93\u51fa\u7684\u7ed3\u6784\u4f53", None))
        self.product_id.setText(QCoreApplication.translate("PQtoolsToCode", u"imx415", None))
        self.include_headers.setPlainText(QCoreApplication.translate("PQtoolsToCode", u"#include \"mpi_isp.h\"\n"
"#include \"mpi_vi.h\"\n"
"#include \"mpi_vpss.h\"\n"
"#include \"hi_comm_vi.h\"\n"
"#include \"hi_comm_vpss.h\"\n"
"#include \"hi_isp_defines.h\"", None))
        self.label_4.setText(QCoreApplication.translate("PQtoolsToCode", u"\u6587\u4ef6\u540d", None))
        self.label_6.setText(QCoreApplication.translate("PQtoolsToCode", u"\u9700\u8981\u5305\u542b\u7684\u5934\u6587\u4ef6", None))
        self.label_8.setText(QCoreApplication.translate("PQtoolsToCode", u"\u7248\u6743\u58f0\u660e", None))
        self.output_filename.setText(QCoreApplication.translate("PQtoolsToCode", u"isp_params", None))
        self.label_9.setText(QCoreApplication.translate("PQtoolsToCode", u"\u4f5c\u8005", None))
        self.filter_struct.setPlainText(QCoreApplication.translate("PQtoolsToCode", u"hiISP_SHARPEN_ATTR_S\n"
"customNRX_PARAM_AUTO_V1_S\n"
"hiNRX_PARAM_MANUAL_V1_S\n"
"hiVPSS_GRP_SHARPEN_ATTR_S\n"
"hiISP_NR_ATTR_S\n"
"hiISP_ANTIFALSECOLOR_ATTR_S\n"
"hiISP_DEMOSAIC_ATTR_S\n"
"hiISP_CR_ATTR_S\n"
"hiISP_LDCI_ATTR_S", None))
        self.copyright.setPlainText(QCoreApplication.translate("PQtoolsToCode", u"/*\n"
"* Copyright (c) 2020\n"
"* All rights reserved.\n"
"*\n"
"* Description: image isp params head file\n"
"* Author: liqinxing\n"
"* Create: 2020-12-28\n"
"* Modefication History:\n"
"* Author: %AUTHOR%\n"
"* Date: %NOW_TINE%\n"
"*/", None))
        self.add_custom_defines.setPlainText(QCoreApplication.translate("PQtoolsToCode", u"typedef struct customNRX_PARAM_AUTO_V1_S {\n"
"    HI_U32 u32ParamNum;\n"
"    HI_U32 ATTRIBUTE au32ISO[16];\n"
"    VI_PIPE_NRX_PARAM_V1_S ATTRIBUTE pastNRXParamV1[16];\n"
"} CUSTOM_NRX_PARAM_AUTO_V1_S;", None))
        self.label_11.setText(QCoreApplication.translate("PQtoolsToCode", u"\u9700\u8981\u66ff\u6362\u7684\u7ed3\u6784\u4f53", None))
        self.custom_define_dict.setPlainText(QCoreApplication.translate("PQtoolsToCode", u"hiNRX_PARAM_AUTO_V1_S:customNRX_PARAM_AUTO_V1_S", None))
        self.is_const.setText(QCoreApplication.translate("PQtoolsToCode", u"\u662f\u5426\u9700\u8981\u52a0const", None))
        self.generate.setText(QCoreApplication.translate("PQtoolsToCode", u"\u751f\u6210", None))
    # retranslateUi

