import cv2
import numpy
from PyQt6.QtCore import pyqtSignal, QThread
from PyQt6.QtWidgets import QLabel

from Image.hand_roi_fetcher import AutoHandCapture
from Image.image_utils import ImageUtils


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


class DisplayRuntimeFrameThread(QThread):
    tell_current_image = pyqtSignal(numpy.ndarray)
    tell_target_image = pyqtSignal(numpy.ndarray)
    tell_points = pyqtSignal(list)

    def __init__(self, _video_handle_index: int, label: QLabel):
        super(DisplayRuntimeFrameThread, self).__init__()
        self.video_capture_index = _video_handle_index
        self.__label = label
        self.video_capture = cv2.VideoCapture(self.video_capture_index)
        self.__hand_capture = AutoHandCapture()
        self.shell_stop = False
        if not self.video_capture.isOpened():
            raise DeviceNotFound("error")

    def run(self):
        while True:
            _, frame = self.video_capture.read()
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
        print("release the video handle")
        self.video_capture.release()
