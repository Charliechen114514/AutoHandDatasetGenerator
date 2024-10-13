import math
from Image.ROI_Hand_Impl.gesture_recognitions import GestureRecognition
from Image.ROI_Hand_Impl.result_handler import GestureRecognizerResultAnalyzer
import cv2


class RoiHandImpl:
    def __init__(self):
        self.gesture_recognizer = GestureRecognition()
        self.rect_color = (0, 255, 0)
        self.external_bound: list[int] = [30, 30]

        self.roi_rect_point = [0, 0, 0, 0]

    def gain_hand_roi(self, frame: cv2.Mat) -> cv2.Mat:
        # fetch the result from the frame
        frame = frame.copy()
        result = self.gesture_recognizer.get_from_cv_image(frame)
        if GestureRecognizerResultAnalyzer.check_result_available(result):
            paw_x_list = []
            paw_y_list = []
            for i in result.hand_landmarks:
                for each_point in i:
                    paw_x_list.append(each_point.x)
                    paw_y_list.append(each_point.y)
            ratio_x_to_pixel = lambda x: math.ceil(x * frame.shape[1])
            ratio_y_to_pixel = lambda y: math.ceil(y * frame.shape[0])
            paw_left_top_x, paw_right_bottom_x = map(ratio_x_to_pixel,
                                                     [min(paw_x_list), max(paw_x_list)])
            paw_left_top_y, paw_right_bottom_y = map(ratio_y_to_pixel,
                                                     [min(paw_y_list), max(paw_y_list)])

            self.roi_rect_point[0] = paw_left_top_x - self.external_bound[0]
            self.roi_rect_point[1] = paw_left_top_y - self.external_bound[1]
            self.roi_rect_point[2] = paw_right_bottom_x + self.external_bound[0]
            self.roi_rect_point[3] = paw_right_bottom_y + self.external_bound[1]
            return cv2.rectangle(frame,
                                 (paw_left_top_x - self.external_bound[0],
                                  paw_left_top_y - self.external_bound[1]),
                                 (paw_right_bottom_x + self.external_bound[0],
                                  paw_right_bottom_y + self.external_bound[1]),
                                 self.rect_color, 2).copy()
        for i in range(4):
            self.roi_rect_point[i] = 0
        return frame.copy()
