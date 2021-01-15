from scipy.ndimage.filters import convolve, convolve1d
import numpy as np
import math
import time
import tools.rawimageeditor.utility
from scipy import signal
from tools.rawimageeditor.rawImage import RawImageInfo, RawImageParams


def demosaic(raw: RawImageInfo, params: RawImageParams):
    """
    function: demosaic
    input: raw:RawImageInfo() params:RawImageParams()
    demosaic有两种算法，设置demosaic的算法
    0: Malvar-He-Cutler algorithm
    1: directionally weighted gradient based interpolation algorithm
    """
    ret_img = RawImageInfo()
    ret_img.create_image('after demosaic', (raw.get_height(), raw.get_width(), 3))
    if (params.get_demosaic_funct_type() == 0):
        demosaicing_CFA_Bayer_bilinear(raw, ret_img.data)
    elif (params.get_demosaic_funct_type() == 1):
        demosaicing_CFA_Bayer_Malvar2004(raw, ret_img.data)
    elif (params.get_demosaic_funct_type() == 2):
        demosaicing_CFA_Bayer_Menon2007(raw, ret_img.data)
    else:
        return None

    ret_img.clip_range()
    ret_img.set_color_space("RGB")
    return ret_img


def demosaicing_CFA_Bayer_bilinear(raw: RawImageInfo, output):
    """
    Bilinear Bayer CFA Demosaicing
    ==============================
    *Bayer* CFA (Colour Filter Array) bilinear demosaicing.
    References
    ----------
    -   :cite:`Losson2010c` : Losson, O., Macaire, L., & Yang, Y. (2010).
        Comparison of Color Demosaicing Methods. In Advances in Imaging and
        Electron Physics (Vol. 162, pp. 173-265). doi:10.1016/S1076-5670(10)62005-8
    """

    R_m, G_m, B_m = raw.masks_CFA_Bayer()
    CFA = raw.get_raw_data()

    H_G = np.float32(
        [[0, 1, 0],
         [1, 4, 1],
         [0, 1, 0]]) * 0.25

    H_RB = np.float32(
        [[1, 2, 1],
         [2, 4, 2],
         [1, 2, 1]]) * 0.25

    output[:, :, 2] = convolve(CFA * R_m, H_RB)
    output[:, :, 1] = convolve(CFA * G_m, H_G)
    output[:, :, 0] = convolve(CFA * B_m, H_RB)

    del R_m, G_m, B_m, H_RB, H_G
    return


def demosaicing_CFA_Bayer_Malvar2004(raw: RawImageInfo, output):
    """
    *Bayer* CFA (Colour Filter Array) *Malvar (2004)* demosaicing.
    References
    ----------
    -   :cite:`Malvar2004a` : Malvar, H. S., He, L.-W., Cutler, R., & Way, O. M.
        (2004). High-Quality Linear Interpolation for Demosaicing of
        Bayer-Patterned Color Images. International Conference of Acoustic, Speech
        and Signal Processing, 5-8.
        http://research.microsoft.com/apps/pubs/default.aspx?id=102068
    """

    R_m, G_m, B_m = raw.masks_CFA_Bayer()
    CFA = raw.get_raw_data()

    GR_GB = np.float32(
         [[0, 0, -1, 0, 0],
         [0, 0, 2, 0, 0],
         [-1, 2, 4, 2, -1],
         [0, 0, 2, 0, 0],
         [0, 0, -1, 0, 0]]) * 0.125

    Rg_RB_Bg_BR = np.float32(
        [[0, 0, 0.5, 0, 0],
         [0, -1, 0, -1, 0],
         [-1, 4, 5, 4, - 1],
         [0, -1, 0, -1, 0],
         [0, 0, 0.5, 0, 0]]) * 0.125

    Rg_BR_Bg_RB = np.transpose(Rg_RB_Bg_BR)

    Rb_BB_Br_RR = np.float32(
        [[0, 0, -1.5, 0, 0],
         [0, 2, 0, 2, 0],
         [-1.5, 0, 6, 0, -1.5],
         [0, 2, 0, 2, 0],
         [0, 0, -1.5, 0, 0]]) * 0.125

    R = CFA * R_m
    G = CFA * G_m
    B = CFA * B_m

    del G_m

    G = np.where(np.logical_or(R_m == 1, B_m == 1), convolve(CFA, GR_GB), G)

    RBg_RBBR = convolve(CFA, Rg_RB_Bg_BR)
    RBg_BRRB = convolve(CFA, Rg_BR_Bg_RB)
    RBgr_BBRR = convolve(CFA, Rb_BB_Br_RR)

    del GR_GB, Rg_RB_Bg_BR, Rg_BR_Bg_RB, Rb_BB_Br_RR

    # Red rows.
    R_r = np.transpose(np.any(R_m == 1, axis=1)[np.newaxis]) * np.ones(R.shape, dtype=np.float32)
    # Red columns.
    R_c = np.any(R_m == 1, axis=0)[np.newaxis] * np.ones(R.shape, dtype=np.float32)
    # Blue rows.
    B_r = np.transpose(np.any(B_m == 1, axis=1)[np.newaxis]) * np.ones(B.shape, dtype=np.float32)
    # Blue columns
    B_c = np.any(B_m == 1, axis=0)[np.newaxis] * np.ones(B.shape, dtype=np.float32)

    del R_m, B_m

    R = np.where(np.logical_and(R_r == 1, B_c == 1), RBg_RBBR, R)
    R = np.where(np.logical_and(B_r == 1, R_c == 1), RBg_BRRB, R)

    B = np.where(np.logical_and(B_r == 1, R_c == 1), RBg_RBBR, B)
    B = np.where(np.logical_and(R_r == 1, B_c == 1), RBg_BRRB, B)

    R = np.where(np.logical_and(B_r == 1, B_c == 1), RBgr_BBRR, R)
    B = np.where(np.logical_and(R_r == 1, R_c == 1), RBgr_BBRR, B)

    del RBg_RBBR, RBg_BRRB, RBgr_BBRR, R_r, R_c, B_r, B_c

    output[:, :, 2] = R
    output[:, :, 1] = G
    output[:, :, 0] = B
    del R,G,B
    return


def demosaicing_CFA_Bayer_Menon2007(raw: RawImageInfo, output):
    """
    DDFAPD - Menon (2007) Bayer CFA Demosaicing
    ===========================================
    *Bayer* CFA (Colour Filter Array) DDFAPD - *Menon (2007)* demosaicing.
    References
    ----------
    -   :cite:`Menon2007c` : Menon, D., Andriani, S., & Calvagno, G. (2007).
        Demosaicing With Directional Filtering and a posteriori Decision. IEEE
        Transactions on Image Processing, 16(1), 132-141.
        doi:10.1109/TIP.2006.884928
    """
    R_m, G_m, B_m = raw.masks_CFA_Bayer()
    CFA = raw.get_raw_data()
    h_0 = np.array([0, 0.5, 0, 0.5, 0], dtype=np.float32)
    h_1 = np.array([-0.25, 0, 0.5, 0, -0.25], dtype=np.float32)

    R = CFA * R_m
    G = CFA * G_m
    B = CFA * B_m

    G_H = np.where(G_m == 0, _cnv_h(CFA, h_0) + _cnv_h(CFA, h_1), G)
    G_V = np.where(G_m == 0, _cnv_v(CFA, h_0) + _cnv_v(CFA, h_1), G)

    C_H = np.where(R_m == 1, R - G_H, 0)
    C_H = np.where(B_m == 1, B - G_H, C_H)

    C_V = np.where(R_m == 1, R - G_V, 0)
    C_V = np.where(B_m == 1, B - G_V, C_V)

    D_H = np.abs(C_H - np.pad(C_H, ((0, 0),
                                    (0, 2)), mode=str('reflect'))[:, 2:])
    D_V = np.abs(C_V - np.pad(C_V, ((0, 2),
                                    (0, 0)), mode=str('reflect'))[2:, :])

    del h_0, h_1, CFA, C_V, C_H

    k = np.array(
        [[0, 0, 1, 0, 1],
         [0, 0, 0, 1, 0],
         [0, 0, 3, 0, 3],
         [0, 0, 0, 1, 0],
         [0, 0, 1, 0, 1]], dtype=np.float32)

    d_H = convolve(D_H, k, mode='constant')
    d_V = convolve(D_V, np.transpose(k), mode='constant')

    del D_H, D_V

    mask = d_V >= d_H
    G = np.where(mask, G_H, G_V)
    M = np.where(mask, 1, 0)

    del d_H, d_V, G_H, G_V

    # Red rows.
    R_r = np.transpose(np.any(R_m == 1, axis=1)[np.newaxis]) * np.ones(R.shape, dtype=np.float32)
    # Blue rows.
    B_r = np.transpose(np.any(B_m == 1, axis=1)[np.newaxis]) * np.ones(B.shape, dtype=np.float32)

    k_b = np.array([0.5, 0, 0.5], dtype=np.float32)

    R = np.where(
        np.logical_and(G_m == 1, R_r == 1),
        G + _cnv_h(R, k_b) - _cnv_h(G, k_b),
        R,
    )

    R = np.where(
        np.logical_and(G_m == 1, B_r == 1) == 1,
        G + _cnv_v(R, k_b) - _cnv_v(G, k_b),
        R,
    )

    B = np.where(
        np.logical_and(G_m == 1, B_r == 1),
        G + _cnv_h(B, k_b) - _cnv_h(G, k_b),
        B,
    )

    B = np.where(
        np.logical_and(G_m == 1, R_r == 1) == 1,
        G + _cnv_v(B, k_b) - _cnv_v(G, k_b),
        B,
    )

    R = np.where(
        np.logical_and(B_r == 1, B_m == 1),
        np.where(
            M == 1,
            B + _cnv_h(R, k_b) - _cnv_h(B, k_b),
            B + _cnv_v(R, k_b) - _cnv_v(B, k_b),
        ),
        R,
    )

    B = np.where(
        np.logical_and(R_r == 1, R_m == 1),
        np.where(
            M == 1,
            R + _cnv_h(B, k_b) - _cnv_h(R, k_b),
            R + _cnv_v(B, k_b) - _cnv_v(R, k_b),
        ),
        B,
    )

    del k_b, R_r, B_r

    del M, R_m, G_m, B_m
    output[:, :, 2] = R
    output[:, :, 1] = G
    output[:, :, 0] = B
    del R,G,B
    return

def _cnv_h(x, y):
    """
    Helper function for horizontal convolution.
    """
    return convolve1d(x, y, mode='mirror')


def _cnv_v(x, y):
    """
    Helper function for vertical convolution.
    """
    return convolve1d(x, y, mode='mirror', axis=0)
