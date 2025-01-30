import cv2
from PySide6.QtWidgets import QLabel
from Core.CameraCapture import CameraRuntimeThread
from Core.Common import ImageConvertor
from Core.ImageSaver.ImageSaver import ImageSaver
from loguru import logger


class DisplayHandler:
    def __init__(self, index: int, label: QLabel):
        self.__display_label = None
        self.__display_label = label
        self.video_info: list[int] = [0, 0]
        if self.__display_label is None:
            raise ValueError("Haven't yet set label to display!")
        self.__thread_handle = CameraRuntimeThread(index, label)
        self.__thread_handle.tell_current_image.connect(self.__handle_display_res)
        self.__thread_handle.tell_points.connect(self.__handle_roi_rect)
        self.__thread_handle.tell_target_image.connect(self.__handle_core_res)
        self.__current_ready_save_point = [0, 0, 0, 0]
        self.__current_handle_mat = None
    """
        display the emit image from capturing thread
    """
    def __handle_display_res(self, mat):
        self.__display_label.setPixmap(ImageConvertor.cvImage_to_QPixmap(mat))

    def __handle_core_res(self, mat):
        self.__current_handle_mat = mat

    def __handle_roi_rect(self, points: list[int]):
        self.__current_ready_save_point = points.copy()

    def set_stop(self):
        self.__thread_handle.shell_stop = True
        self.__thread_handle.quit()
        self.__thread_handle.wait()
        logger.info("stop the thread")

    def export_current_fetch(self):
        if self.__current_handle_mat is None or self.__current_ready_save_point == [0, 0, 0, 0]:
            return None
        else:
            return ImageSaver.gain_suit_corp_image(self.__current_handle_mat, self.__current_ready_save_point)

    def start_display(self):
        try:
            self.__thread_handle.start()
        except Exception as e:
            logger.error(str(e))
            return

    def __del__(self):
        if self.__thread_handle.isRunning():
            self.__thread_handle.quit()
            self.__thread_handle.wait()
            logger.info("stop the thread")