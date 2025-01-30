class CameraInfo:
    def __init__(self, index: int, name: str):
        self.__index = index
        self.__name = name

    @property
    def index(self):
        return self.__index

    @property
    def name(self):
        return self.__name
        
