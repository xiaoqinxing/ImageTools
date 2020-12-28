from ui.customwidget import SubWindow
from tools.pqtools_to_code.pqtools2code_window import Ui_PQtoolsToCode


class PQtoolsParams:
    tab_space = 4
    max_line_char_counts = 120
    xmlfile = ''
    product_id = 'imx415'
    output_path = ''
    output_filename = 'isp_params'
    author = 'liqinxing'
    filter_struct = """hiISP_SHARPEN_ATTR_S
customNRX_PARAM_AUTO_V1_S
hiNRX_PARAM_MANUAL_V1_S
hiVPSS_GRP_SHARPEN_ATTR_S
hiISP_NR_ATTR_S
hiISP_ANTIFALSECOLOR_ATTR_S
hiISP_DEMOSAIC_ATTR_S
hiISP_CR_ATTR_S
hiISP_LDCI_ATTR_S
"""
    custom_define_dict = """typedef struct customNRX_PARAM_AUTO_V1_S {
    HI_U32 u32ParamNum;
    HI_U32 ATTRIBUTE au32ISO[16];
    VI_PIPE_NRX_PARAM_V1_S ATTRIBUTE pastNRXParamV1[16];
} CUSTOM_NRX_PARAM_AUTO_V1_S;
"""
    need_remove_item = 'rb'
    is_const = True
    include_headers = """# include "mpi_isp.h"
# include "mpi_vi.h"
# include "mpi_vpss.h"
# include "hi_comm_vi.h"
# include "hi_comm_vpss.h"
# include "hi_isp_defines.h"
"""
    add_custom_defines = """hiNRX_PARAM_AUTO_V1_S:customNRX_PARAM_AUTO_V1_S"""
    copyright = """/*
* Copyright (c) 2020
* All rights reserved.
*
* Description: image isp params head file
* Author: liqinxing
* Create: 2020-12-28
* Modefication History:
* Author: %AUTHOR%
* Date: %NOW_TINE%
*/
"""

    def get_params(self, ui):
        self.xmlfile = ui.xmlfile.text()
        self.tab_space = ui.tab_space.value()
        self.max_line_char_counts = ui.max_line_num.value()
        self.product_id = ui.product_id.text()
        self.output_path = ui.output_path.text()
        self.output_filename = ui.output_filename.text()
        self.author = ui.author.text()
        self.filter_struct = ui.filter_struct.toPlainText()
        self.need_remove_item = ui.need_remove_item.text()
        self.include_headers = ui.include_headers.toPlainText()
        self.custom_define_dict = ui.custom_define_dict.toPlainText()
        self.is_const = ui.is_const.isChecked()
        self.add_custom_defines = ui.add_custom_defines.toPlainText()
        self.copyright = ui.copyright.toPlainText()

    def set_params(self, ui):
        ui.xmlfile.setText(self.xmlfile)
        ui.tab_space.setValue(self.tab_space)
        ui.max_line_num.setValue(self.max_line_char_counts)
        ui.product_id.setText(self.product_id)
        ui.output_path.setText(self.output_path)
        ui.output_filename.setText(self.output_filename)
        ui.author.setText(self.author)
        ui.filter_struct.setPlainText(self.filter_struct)
        ui.need_remove_item.setText(self.need_remove_item)
        ui.include_headers.setPlainText(self.include_headers)
        ui.is_const.setChecked(self.is_const)
        ui.add_custom_defines.setPlainText(self.add_custom_defines)
        ui.copyright.setPlainText(self.copyright)
        ui.custom_define_dict.setPlainText(self.custom_define_dict)


class PQtoolsToCode(SubWindow):
    def __init__(self, name, parent=None):
        super().__init__(name, parent, Ui_PQtoolsToCode())
        self.params = self.load_params(PQtoolsParams())
        self.params.set_params(self.ui)
        self.ui.generate.clicked.connect(self.generate_code)

    def generate_code(self):
        self.params.get_params(self.ui)
