import os.path

import cv2
import os
from Image.save_policy import ImageSavePolicy, ImageSaveInterface
from PyQt6.QtWidgets import QFileDialog, QWidget
from PyQt6.QtCore import QDir

class ImageSaverUtils:
    @staticmethod
    def check_dir_exist(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def join_path(_dir: str, file_name: str):
        return os.path.join(_dir, file_name)

    @staticmethod
    def gain_dir_save_path(widget: QWidget) -> str:
        return QFileDialog.getExistingDirectory(widget, "选择需要保存的路径总名称")

    @staticmethod
    def try_make_dir(path: str):
        d = QDir(path)
        if not os.path.exists(path):
            d.mkdir(path)



class ImageSaver:
    def __init__(self):
        self.save_dir = ""
        self.save_policy = ImageSavePolicy()

    def register_policy(self, policy: ImageSaveInterface):
        self.save_policy = policy

    def set_image_save_dir(self, path_dir: str):
        self.save_dir = path_dir

    def save_image(self, image: cv2) -> str:
        if not ImageSaverUtils.check_dir_exist(self.save_dir):
            raise FileNotFoundError("无法保存文件到" + self.save_dir + "文件夹下！检查路径！")
        file_name = ImageSaverUtils.join_path(self.save_dir, self.save_policy.gain_next_image_name() + ".jpg")
        print(file_name)
        cv2.imwrite(filename=file_name, img=image)
        return file_name
