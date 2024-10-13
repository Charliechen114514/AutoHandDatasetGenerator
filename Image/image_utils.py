import cv2
from PyQt6.QtGui import QImage, QPixmap


class ImageUtils:
    @staticmethod
    def cvImage_to_QPixmap(image: cv2.Mat):
        return QPixmap.fromImage(QImage(image.data,
                                        image.shape[1], image.shape[0], image.strides[0], QImage.Format.Format_RGB888))

    @staticmethod
    def gain_suit_corp_image(image: cv2.Mat, points: list[int]):
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


