import cv2
import math
import mediapipe as mp
from mediapipe.tasks.python.vision.gesture_recognizer import GestureRecognizerResult
from mediapipe.tasks.python import BaseOptions, vision
from Core.Common.ImageConvertor import ImageConvertor
from Core.Common.path_utils import PathUtils


class GestureRecognition:
    def __init__(self):
        self.__init_default_recognizer()

    """
        INIT the recognizer as default, usually use the default recognizers
    """
    def __init_default_recognizer(self):
        base_options = BaseOptions(model_asset_path=PathUtils.MODEL_PATH)
        options = vision.GestureRecognizerOptions(base_options=base_options)
        options.min_hand_detection_confidence = 0.8
        options.min_hand_presence_confidence = 0.8
        options.min_tracking_confidence = 0
        self.recognizer = vision.GestureRecognizer.create_from_options(options)

    """
        Core Implements of recognize gestures from general Image
    """
    def __recognize_gesture_impl(self, target_image: mp.Image):
        recognition_result = self.recognizer.recognize(target_image)
        return recognition_result

    """
        do recognize from available cv image
    """
    def get_from_cv_image(self, cv_image: cv2.Mat):
        return self.__recognize_gesture_impl(ImageConvertor.convert_from_cv_color_image(cv_image=cv_image))

    """
        do recognize from available file path
    """
    def get_from_file_name(self, file_path: str):
        return self.__recognize_gesture_impl(ImageConvertor.convert_from_file_path(image_path=file_path))



class GestureRecognizerResultAnalyzer:
    @staticmethod
    def check_result_available(result: GestureRecognizerResult) -> bool:
        return len(result.gestures) != 0

    @staticmethod
    def get_gesture_signals(result: GestureRecognizerResult) -> str:
        return result.gestures[0][0].category_name


class HandROI_impl:
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


""" Configure """
SHELL_FLIP = True

"""
    Hands Features Capture
"""
class HandsCapture:
    MIN_DETECTION_CONFIDENCE = 0.75
    MIN_TRACKING_CONFIDENCE = 0.75
    STATIC_IMAGE_MODE = False
    MAX_NUM_HANDS = 2

    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.75,
            min_tracking_confidence=0.75)
        self.shell_flip = SHELL_FLIP

    def get_marked_frame(self, original_frame: cv2.Mat) -> cv2.Mat:
        frame = cv2.cvtColor(original_frame, cv2.COLOR_BGR2RGB)
        if self.shell_flip:
            frame = cv2.flip(frame, 1)
        results = self.hands.process(frame)  # process()是手势识别最核心的方法，通过调用这个方法，将窗口对象作为参数，mediapipe就会将手势识别的信息存入到res对象中
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 关键点可视化
                self.mp_drawing.draw_landmarks(
                    frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return frame
