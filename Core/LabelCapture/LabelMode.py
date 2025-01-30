class LabelCollectMode:
    MODE_AUTO       = 0
    MODE_MANUAL     = 1
    def __init__(self):
        self.__mode = LabelCollectMode.MODE_AUTO

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: int):
        if mode != LabelCollectMode.MODE_AUTO \
            and mode != LabelCollectMode.MODE_MANUAL:
            raise ValueError("Invalid Mode Settings")
        self.__mode = mode