class AutoCaptureMode:
    MANUAL = 0
    AUTO = 1

    def __init__(self):
        self.__mode = AutoCaptureMode.AUTO

    def is_auto_now(self):
        return self.__mode == AutoCaptureMode.AUTO

    def set_to_auto(self):
        self.__mode = AutoCaptureMode.AUTO

    def set_to_manual(self):
        self.__mode = AutoCaptureMode.MANUAL