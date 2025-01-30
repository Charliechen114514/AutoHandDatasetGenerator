import cv2
from loguru import logger
import os
from Core.Common import PathUtils
from abc import ABC, abstractmethod


class ImageSaveInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def gain_next_image_name(self):
        pass

    @abstractmethod
    def update_policy(self):
        pass

    @abstractmethod
    def reset_policy(self):
        pass


class ImageSavePolicy(ImageSaveInterface):
    def __init__(self):
        super().__init__()
        self.__cnt = 0

    def gain_next_image_name(self):
        self.update_policy()
        return str(self.__cnt)

    def update_policy(self):
        self.__cnt += 1

    def reset_policy(self):
        self.__cnt = 0


class ImageSaverUtils:
    @staticmethod
    def check_dir_exist(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def join_path(_dir: str, file_name: str):
        return os.path.join(_dir, file_name)



class ImageSaver:
    def __init__(self):
        self.save_dir = ""
        self.save_policy = ImageSavePolicy()
        self.__label = ""

    def register_policy(self, policy: ImageSaveInterface):
        self.save_policy = policy

    def set_image_save_dir(self, path_dir: str):
        self.save_dir = path_dir

    def set_label_name(self, label: str):
        self.__label = label

    def save_image(self, image: cv2) -> str:
        file_name = ImageSaverUtils.join_path(self.save_dir, self.__label)
        PathUtils.create_dirent_if_not_exsited(file_name)
        file_name = ImageSaverUtils.join_path(file_name, self.save_policy.gain_next_image_name() + ".jpg")
        logger.info(file_name)
        cv2.imwrite(filename=file_name, img=image)
        return file_name

    @staticmethod
    def gain_suit_corp_image(image: cv2.Mat, points: list[int]) -> cv2.Mat:
        # top_left x, y
        # top right x, y
        bound_width = image.shape[1]
        bound_height = image.shape[0]

        if points[0] < 0:
            points[0] = 0
        if points[1] < 0:
            points[1] = 0
        if points[2] >= bound_width:
            points[2] = bound_width - 1
        if points[3] >= bound_height:
            points[3] = bound_height - 1
        return image[points[1]: points[3], points[0]:points[2]]