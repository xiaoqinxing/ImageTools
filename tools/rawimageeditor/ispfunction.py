import tools.rawimageeditor.isp as isp
import tools.rawimageeditor.debayer as debayer

# pipeline名称全部小写
pipeline_dict = {
    "original raw": isp.get_src_raw_data,
    "black level":  isp.black_level_correction,
    "blc":          isp.black_level_correction,
    "rolloff":      isp.rolloff_correction,
    "abf":          None,
    "demosaic":     debayer.demosaic,
    "awb":          isp.channel_gain_white_balance,
    "ccm":          isp.color_correction,
    "gamma":        isp.gamma_correction,
    "ltm":          isp.ltm_correction,
    "advanced chroma enhancement":  None,
    "ace":                          None,
    "csc":                          isp.color_space_conversion,
    "wavelet denoise":              None,
    "wnr":                          None,
    "adaptive spatial filter":      None,
    "asf":                          None,
    "bad pixel correction":         isp.bad_pixel_correction
}