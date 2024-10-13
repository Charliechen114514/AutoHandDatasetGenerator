import cv2

from Image.ROI_Hand_Impl.roi_hand_impl import RoiHandImpl


class AutoHandCapture:
    KEY_MAT = "Mat"
    KEY_RECT_INFO = "Rect_info"

    def __init__(self):
        self.__roi_gainer = RoiHandImpl()

    def gain_roi_infos(self, mat):
        return {
            AutoHandCapture.KEY_MAT: self.__roi_gainer.gain_hand_roi(mat),
            AutoHandCapture.KEY_RECT_INFO: self.__roi_gainer.roi_rect_point
        }
