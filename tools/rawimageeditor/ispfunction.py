import tools.rawimageeditor.isp as isp
import tools.rawimageeditor.debayer as debayer

pipeline_dict = {
    "raw":          isp.get_src_raw_data,
    "original raw": isp.get_src_raw_data,
    "black level":  isp.black_level_correction,
    "BLC":          isp.black_level_correction,
    "rolloff":      None,
    "ABF":          None,
    "demosaic":     debayer.demosaic,
    "awb":          isp.channel_gain_white_balance,
    "AWB":          isp.channel_gain_white_balance,
    "ccm":          isp.color_correction,
    "CCM":          None,
    "gamma":        isp.gamma_correction,
    "LTM":          isp.ltm_correction,
    "advanced chroma enhancement":  None,
    "ACE":                          None,
    "CSC":                          isp.color_space_conversion,
    "csc":                          isp.color_space_conversion,
    "wavelet denoise":              None,
    "WNR":                          None,
    "adaptive spatial filter":      None,
    "ASF":                          None,
    "bad pixel correction":         isp.bad_pixel_correction
}