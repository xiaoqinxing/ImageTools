# =============================================================
# Import the libraries
# =============================================================
import numpy as np  # array operations
from PySide2.QtGui import QImage
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QFileDialog
from tools.rawimageeditor.ui.rawimageeditor_window import Ui_ImageEditor
from components.customwidget import critical
import cv2
    

class CscParams():
    """
    CSC转换的相关参数
    """
    luma = 50
    contrast = 50
    hue = 50
    satu = 50
    limitrange = Qt.Unchecked
    colorspace = 'BT709'
    need_flush = False
    name = 'CSC'
    
    def set(self, ui:Ui_ImageEditor):
        """
        设置参数界面的显示
        """
        ui.luma.setValue(self.luma)
        ui.contrast.setValue(self.contrast)
        ui.hue.setValue(self.hue)
        ui.saturation.setValue(self.satu)
        index = ui.color_space.findText(self.colorspace)
        ui.color_space.setCurrentIndex(index)
        ui.limitrange.setCheckState(self.limitrange)
    
    def get(self, ui:Ui_ImageEditor):
        """
        func: 获取界面参数
        """
        self.set_contrast(ui.contrast.value())
        self.set_hue(ui.hue.value())
        self.set_satu(ui.saturation.value())
        self.set_luma(ui.luma.value())
        self.set_colorspace(ui.color_space.currentText())
        self.set_limitrange(ui.limitrange.checkState())
        return self.need_flush
    
    def set_luma(self, value):
        if(value != self.luma):
            self.luma = value
            self.need_flush = True
    
    def set_contrast(self, value):
        if(value != self.contrast):
            self.contrast = value
            self.need_flush = True

    def set_hue(self, value):
        if(value != self.hue):
            self.hue = value
            self.need_flush = True

    def set_satu(self, value):
        if(value != self.satu):
            self.satu = value
            self.need_flush = True
    
    def set_colorspace(self, value):
        if(value != self.colorspace):
            self.colorspace = value
            self.need_flush = True
    
    def set_limitrange(self, value):
        """
        设置是否限制YUV的输出范围，TV标准是16-235，PC标准是0-255。0为关，2为开
        """
        if(value != self.limitrange):
            self.limitrange = value
            self.need_flush = True

class FormatParams():
    """
    图片输入格式相关参数
    """
    height = 0
    width = 0
    bit_depth = 0
    raw_format = "MIPI"
    pattern = "rggb"
    name = 'original raw'
    need_flush = False
    filename = ''

    def set(self, ui:Ui_ImageEditor):
        ui.width.setValue(self.width)
        ui.height.setValue(self.height)
        ui.bit.setValue(self.bit_depth)
        index = ui.pattern.findText(self.pattern.upper())
        ui.pattern.setCurrentIndex(index)
        index = ui.raw_format.findText(self.raw_format)
        ui.raw_format.setCurrentIndex(index)
        ui.filename.setText(self.filename)
    
    def get(self, ui:Ui_ImageEditor):
        self.set_width(ui.width.value())
        self.set_height(ui.height.value())
        self.set_bit_depth(ui.bit.value())
        self.set_raw_format(ui.raw_format.currentText())
        self.set_pattern(ui.pattern.currentText().lower())
        self.set_filename(ui.filename.text())
        return self.need_flush
    
    def set_width(self, value):
        if(self.width != value):
            self.width = value
            self.need_flush = True
    
    def set_height(self, value):
        if(self.height != value):
            self.height = value
            self.need_flush = True
    
    def set_bit_depth(self, value):
        if(self.bit_depth != value):
            self.bit_depth = value
            self.need_flush = True
    
    def set_raw_format(self, value):
        if(self.raw_format != value):
            self.raw_format = value
            self.need_flush = True
    
    def set_pattern(self, value):
        if(self.pattern != value):
            self.pattern = value
            self.need_flush = True
    
    def set_filename(self, value):
        if(self.filename != value):
            self.filename = value
            self.need_flush = True

class DemosaicParams():
    """
    demosaic相关参数
    """
    __neighborhood_size_for_bad_pixel_correction = 3
    __demosaic_func_type = 0
    __demosaic_need_proc_color = 0
    __demosaic_need_media_filter = 0
    need_flush = False
    name = 'demosaic'

    def set(self, ui:Ui_ImageEditor):
        index = ui.demosaic_type.findText(self.get_demosaic_func_string())
        ui.demosaic_type.setCurrentIndex(index)
    
    def get(self, ui:Ui_ImageEditor):
        self.set_demosaic_func_type(ui.demosaic_type.currentText())
        return self.need_flush        
    
    def set_demosaic_func_type(self, demosaic_type):
        """
        demosaic有两种算法，设置demosaic的算法
        0: 双线性插值
        1: Malvar-He-Cutler algorithm
        2: directionally weighted gradient based interpolation algorithm
        """
        if(demosaic_type == '双线性插值'):
            index = 0
        elif(demosaic_type == 'Malvar2004'):
            index = 1
        else:
            index = 2
        if(index != self.__demosaic_func_type):
            self.__demosaic_func_type = index
            self.need_flush = True

    def get_demosaic_func_string(self):
        if(self.__demosaic_func_type == 0):
            ret = '双线性插值'
        elif(self.__demosaic_func_type == 1):
            ret = 'Malvar2004'
        else:
            ret = 'Menon2007'
        return ret
    
    def get_demosaic_funct_type(self):
        return self.__demosaic_func_type

    def set_demosaic_need_proc_color(self, value):
        """
        是否在demosaic之后启用色度抑制
        """
        self.__demosaic_need_proc_color = value

    def get_demosaic_need_proc_color(self):
        return self.__demosaic_need_proc_color

    def set_demosaic_need_media_filter(self, value):
        """
        是否在demosaic之后启用中值滤波
        """
        self.__demosaic_need_media_filter = value

    def get_demosaic_need_media_filter(self):
        return self.__demosaic_need_media_filter


class LTMParams():
    """
    设置动态范围调整参数
    """
    __dark_boost = 100
    __bright_suppress = 100
    need_flush = False
    name = 'LTM'

    def set(self, ui:Ui_ImageEditor):
        ui.dark_boost.setValue(self.get_dark_boost())
        ui.bright_suppress.setValue(self.get_bright_suppress())
    
    def get(self, ui:Ui_ImageEditor):
        self.set_dark_boost(ui.dark_boost.value())
        self.set_bright_suppress(ui.bright_suppress.value())
        return self.need_flush
    
    def set_dark_boost(self, value):
        """
        设置暗处提亮程度
        """
        if(value != self.__dark_boost):
            self.need_flush = True
            self.__dark_boost = value
    
    def get_dark_boost(self):
        return self.__dark_boost

    def set_bright_suppress(self, value):
        if(value != self.__bright_suppress):
            self.need_flush = True
            self.__bright_suppress = value
    
    def get_bright_suppress(self):
        return self.__bright_suppress


class AWBParams():
    need_flush = False
    name = 'AWB'
    awb_gain = [1., 1., 1.]

    def set(self, ui:Ui_ImageEditor):
        awb_gain = self.get_awb_gain()
        ui.awb_r.setValue(awb_gain[0])
        ui.awb_g.setValue(awb_gain[1])
        ui.awb_b.setValue(awb_gain[2])
    
    def get(self, ui:Ui_ImageEditor):
        self.set_awb_gain(
            [ui.awb_r.value(), ui.awb_g.value(), ui.awb_b.value()])
        return self.need_flush
    
    def set_awb_gain(self, awb_gain):
        """
        设置AWB的增益 1x3
        """
        if(awb_gain != self.awb_gain):
            self.awb_gain = awb_gain
            self.need_flush = True

    def get_awb_gain(self):
        return self.awb_gain
    
    def set_awb_ratio(self, awb_ratio):
        """
        设置r/g和b/g的值
        """
        awb_gain = [1, 1, 1]
        awb_gain[0] = awb_ratio[0]
        awb_gain[1] = 1
        awb_gain[2] = awb_ratio[1]
        if (awb_gain != self.awb_gain):
            self.awb_gain = awb_gain
            self.need_flush = True
    
class BLCParams():
    need_flush = False
    name = 'black level'
    black_level = [0, 0, 0, 0]

    def set(self, ui:Ui_ImageEditor):
        blc_level = self.get_black_level()
        ui.blc_r.setValue(blc_level[0])
        ui.blc_gr.setValue(blc_level[1])
        ui.blc_gb.setValue(blc_level[2])
        ui.blc_b.setValue(blc_level[3])
    
    def get(self, ui:Ui_ImageEditor):
        self.set_black_level([ui.blc_r.value(
            ), ui.blc_gr.value(), ui.blc_gb.value(), ui.blc_b.value()])
        return self.need_flush
    
    def set_black_level(self, black_level):
        if(black_level != self.black_level):
            self.black_level = black_level
            self.need_flush = True

    def get_black_level(self):
        return np.array(self.black_level)

class GammaParams():
    need_flush = False
    name = 'gamma'
    __gamma_ratio = 2.2
    # gamma 查找表的长度
    gamma_table_size = 512

    def set(self, ui:Ui_ImageEditor):
        ui.gamma_ratio.setValue(self.get_gamma_ratio())
    
    def get(self, ui:Ui_ImageEditor):
        self.set_gamma(ui.gamma_ratio.value())
        return self.need_flush

    def set_gamma(self, gamma_ratio):
        """
        设置gamma的值
        """
        if(gamma_ratio != self.__gamma_ratio):
            self.__gamma_ratio = gamma_ratio
            self.need_flush = True

    def get_gamma_ratio(self):
        return self.__gamma_ratio

class CCMParams():
    need_flush = False
    name = 'CCM'
    color_matrix = [[1., .0, .0],
                    [.0, 1., .0],
                    [.0, .0, 1.]]
    
    def set(self, ui:Ui_ImageEditor):
        ccm = self.get_color_matrix()
        ui.ccm_rr.setValue(ccm[0][0])
        ui.ccm_rg.setValue(ccm[0][1])
        ui.ccm_rb.setValue(ccm[0][2])
        ui.ccm_gr.setValue(ccm[1][0])
        ui.ccm_gg.setValue(ccm[1][1])
        ui.ccm_gb.setValue(ccm[1][2])
        ui.ccm_br.setValue(ccm[2][0])
        ui.ccm_bg.setValue(ccm[2][1])
        ui.ccm_bb.setValue(ccm[2][2])
    
    def get(self, ui:Ui_ImageEditor):
        self.set_color_matrix([[ui.ccm_rr.value(), ui.ccm_rg.value(), ui.ccm_rb.value()],
                            [ui.ccm_gr.value(), ui.ccm_gg.value(), ui.ccm_gb.value()],
                            [ui.ccm_br.value(), ui.ccm_bg.value(), ui.ccm_bb.value()]]) 
        return self.need_flush
    
    def set_color_matrix(self, color_matrix):
        """
        设置CCM 3x3
        """
        if(color_matrix != self.color_matrix):
            self.color_matrix = color_matrix
            self.need_flush = True

    def get_color_matrix(self):
        return self.color_matrix

class BPCParams():
    need_flush = False
    name = 'bad pixel correction'
    __neighborhood_size_for_bad_pixel_correction = 0

    def set_size_for_bad_pixel_correction(self, value):
        """
        设置bad pixel correction的检测核大小
        默认值为3，代表在3x3的范围内检测，这个范围内如果超过两个坏点则不生效
        """
        if(value != self.__neighborhood_size_for_bad_pixel_correction):
            self.__neighborhood_size_for_bad_pixel_correction = value
            self.need_flush = True

    def get_size_for_bad_pixel_correction(self):
        return self.__neighborhood_size_for_bad_pixel_correction * 2 + 3
    
    def set(self, ui:Ui_ImageEditor):
        ui.badpixelcorrection.setValue(self.__neighborhood_size_for_bad_pixel_correction)
    
    def get(self, ui:Ui_ImageEditor):
        self.set_size_for_bad_pixel_correction(ui.badpixelcorrection.value())
        return self.need_flush

class RolloffParams():
    need_flush = False
    name = 'rolloff'
    flatphoto = 1
    rgb_pattern_dict = {
        'r':2,
        'g':1,
        'b':0
    }
    def __init__(self, rawformat, blc):
        self.rawformat = rawformat # 应该只是引用
        self.blc = blc

    def set_flatphoto(self):
        self.flatphoto = np.zeros((self.rawformat.height, self.rawformat.width), dtype=np.float32)
        imagepath = QFileDialog.getOpenFileName(
            None, '打开平场图(RAW)', './', "raw (*.raw)")
        if imagepath[0] != '':
            try:
                flatphoto_ratio = np.fromfile(imagepath[0], dtype="uint16", sep="").reshape(
                    (self.rawformat.height, self.rawformat.width))
            except Exception:
                critical('打开图片错误')
            for blc, (y, x) in zip(self.blc.black_level, [(0, 0), (0, 1), (1, 0), (1, 1)]):
                tmp = cv2.medianBlur(flatphoto_ratio[y::2, x::2] - blc, 5)
                max_value = tmp.max()
                self.flatphoto[y::2, x::2] = max_value / tmp
            self.need_flush = True
    
    def set(self, ui:Ui_ImageEditor):
        pass
    
    def get(self, ui:Ui_ImageEditor):
        return self.need_flush

class SharpenParams():
    need_flush = False
    name = 'yuv sharpen'
    medianblur_strength = 0
    sharpen_strength = 5
    denoise_threshold = 50
    clip_range = 64
    # TODO 滑动条右侧增加数值label显示

    def set_medianblur_strength(self, value):
        """
        设置yuv 3x3中值滤波的强度
        """
        if(value != self.medianblur_strength):
            self.medianblur_strength = value
            self.need_flush = True
    
    def set_sharpen_strength(self, value):
        """
        设置yuv 锐化强度
        """
        if(value != self.sharpen_strength):
            self.sharpen_strength = value
            self.need_flush = True
    
    def set_denoise_threshold(self, value):
        """
        设置yuv 锐化权重
        """
        if(value != self.denoise_threshold):
            self.denoise_threshold = value
            self.need_flush = True
    
    def set_clip_range(self, value):
        """
        设置yuv 钳位阈值
        """
        if(value != self.clip_range):
            self.clip_range = value
            self.need_flush = True
    
    def set(self, ui:Ui_ImageEditor):
        ui.medianblur_strength.setValue(self.medianblur_strength)
        ui.sharpen_strength.setValue(self.sharpen_strength)
        ui.denoise_threshold.setValue(self.denoise_threshold)
        ui.clip_range.setValue(self.clip_range)
    
    def get(self, ui:Ui_ImageEditor):
        self.set_medianblur_strength(ui.medianblur_strength.value())
        self.set_sharpen_strength(ui.sharpen_strength.value())
        self.set_denoise_threshold(ui.denoise_threshold.value())
        self.set_clip_range(ui.clip_range.value())
        return self.need_flush
    
# =============================================================
# class RawImageParams:

#   Helps set up necessary information/metadata of the image
# =============================================================
class RawImageParams():
    def __init__(self):
        """
        zh
        """
        self.error_str = ""
        # 自动刷新pipeline的参数，防止设置参数没有生效
        self.need_flush = False
        self.need_flush_isp = []
        # params需要一一对应
        self.params = [
            FormatParams(),
            DemosaicParams(),
            LTMParams(),
            AWBParams(),
            BLCParams(),
            GammaParams(),
            CCMParams(),
            CscParams(),
            BPCParams(),
            SharpenParams()
        ]
        [
            self.rawformat,
            self.demosaic,
            self.ltm,
            self.awb, 
            self.blc,
            self.gamma,
            self.ccm,
            self.csc,
            self.bpc, 
            self.sharpen
        ] = self.params

        self.rolloff = RolloffParams(self.rawformat, self.blc)

    def set_img_params_ui(self, ui:Ui_ImageEditor):
        """
        设置参数界面的显示
        """
        for param in self.params:
            param.set(ui)

    def get_img_params(self, ui:Ui_ImageEditor):
        """
        func: 获取界面参数
        """
        self.need_flush_isp = []
        for param in self.params:
            self.get_params(param, ui)
        if(len(self.need_flush_isp) > 0):
            self.need_flush = True

    def set_error_str(self, string):
        self.error_str = string

    def get_error_str(self):
        return self.error_str
    
    def get_params(self, params, ui):
        if params.get(ui) == True:
            self.need_flush_isp.append(params.name)
            params.need_flush = False