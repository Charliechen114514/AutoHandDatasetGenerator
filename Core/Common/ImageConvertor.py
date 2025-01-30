from mediapipe.python import Image, ImageFormat
from PySide6.QtGui import QPixmap, QImage
import cv2

"""
    this imports make the transfer from Mat to Image
"""
class ImageConvertor:
    @staticmethod
    def convert_from_cv_color_image(cv_image: cv2.Mat) -> Image:
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        return Image(image_format=ImageFormat.SRGB, data=cv_image)

    @staticmethod
    def convert_from_file_path(image_path) -> Image:
        return Image.create_from_file(image_path)

    @staticmethod
    def cvImage_to_QPixmap(image: cv2.Mat):
        return QPixmap.fromImage(QImage(image.data,
                                        image.shape[1], image.shape[0], image.strides[0], QImage.Format.Format_RGB888))
