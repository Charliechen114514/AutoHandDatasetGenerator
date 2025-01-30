from pygrabber.dshow_graph import FilterGraph
from Core.CameraCapture import CameraInfo


class CameraCollector:
    def __filled_devices(self):
        index = 0
        for name in self.__name_lists:
            self.__deviceslist.append(CameraInfo(index, name))
            index += 1

    def __init__(self):
        self.__deviceslist: list[CameraInfo] = []
        self.__name_lists:list[str] = FilterGraph().get_input_devices()
        self.__filled_devices()

    @property
    def devices(self) -> list[CameraInfo]:
        return self.__deviceslist
    
    @property
    def devicesName(self) -> list[str]:
        return self.__name_lists


    