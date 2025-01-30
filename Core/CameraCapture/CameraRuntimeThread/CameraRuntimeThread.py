from PySide6.QtCore import QThread, Signal
from Core.HandMatching import HandROI_impl
from loguru import logger
import numpy
import cv2

class DeviceNotFound(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class NoneFrame(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class AutoHandCapture:
    KEY_MAT = "Mat"
    KEY_RECT_INFO = "Rect_info"

    def __init__(self):
        self.__roi_gainer = HandROI_impl()

    def gain_roi_infos(self, mat):
        return {
            AutoHandCapture.KEY_MAT: self.__roi_gainer.gain_hand_roi(mat),
            AutoHandCapture.KEY_RECT_INFO: self.__roi_gainer.roi_rect_point
        }


class CameraRuntimeThread(QThread):
    tell_current_image = Signal(numpy.ndarray)
    tell_target_image = Signal(numpy.ndarray)
    tell_points = Signal(list)
    def __init__(self, passing_camera_index: int, parent = None):
        super().__init__(parent)
        logger.info("thread inited")
        self.__videoHandle = cv2.VideoCapture(passing_camera_index)
        self.__hand_capture = AutoHandCapture()
        self.shell_stop = False
        self.finished.connect(self.deleteLater)
        if not self.__videoHandle.isOpened():
            raise DeviceNotFound("error")


    def run(self):
        while True:
            _, frame = self.__videoHandle.read()
            if frame is None or self.shell_stop:
                return
            # 将图象转发出来
            res = self.__hand_capture.gain_roi_infos(frame.copy())
            # 处理展示
            frame_display = res[AutoHandCapture.KEY_MAT]
            frame_display = cv2.cvtColor(frame_display, cv2.COLOR_BGR2RGB)
            self.tell_current_image.emit(frame_display)
            # 通知分割点
            self.tell_points.emit(res[AutoHandCapture.KEY_RECT_INFO])
            self.tell_target_image.emit(frame)   

    def __del__(self):
        logger.info("release the video handle")
        self.__videoHandle.release()     




    
