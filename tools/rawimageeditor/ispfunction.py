import tools.rawimageeditor.isp as isp
import tools.rawimageeditor.debayer as debayer

# pipeline名称全部小写
pipeline_dict = {
    "original raw":                 isp.get_src_raw_data,
    "black level":                  isp.black_level_correction,
    "blc":                          isp.black_level_correction,
    "rolloff":                      isp.rolloff_correction,
    "bad pixel correction":         isp.bad_pixel_correction,
    "bayer denoise":                None,
    "demosaic":                     debayer.demosaic,
    "awb":                          isp.channel_gain_white_balance,
    "ccm":                          isp.color_correction,
    "gamma":                        isp.gamma_correction,
    "ltm":                          isp.ltm_correction,
    "csc":                          isp.color_space_conversion,
    "yuv denoise":                  isp.wavelet_denoise,
    "yuv sharpen":                  isp.sharpen
}