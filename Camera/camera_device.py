from pygrabber.dshow_graph import FilterGraph


class CameraDeviceInfo:
    def __init__(self):
        self.name = ""
        self.index = -1

    def set_index_and_name(self, index: int, name: str):
        self.index = index
        self.name = name


class CameraDeviceFetcher:
    INVALID_CAMERA_INDEX = -1

    def __init__(self):
        graph = FilterGraph()
        self.__device_name_list = graph.get_input_devices()
        self.device_usable_list: list[CameraDeviceInfo] = []
        self.__gen_according_device_list()


    def __gen_according_device_list(self):
        index = 0
        for each_device_name in self.__device_name_list:
            each_device = CameraDeviceInfo()
            each_device.set_index_and_name(index, each_device_name)
            self.device_usable_list.append(each_device)
            index += 1

    def get_devices_name(self):
        return self.__device_name_list

    def get_devices(self) -> list[CameraDeviceInfo]:
        return self.device_usable_list


class CameraDeviceUtils:
    @staticmethod
    def search_from_list(lists_of_cameras_info: list[CameraDeviceInfo], name: str) -> int:
        for each_device in lists_of_cameras_info:
            if each_device.name == name:
                return each_device.index
        return CameraDeviceFetcher.INVALID_CAMERA_INDEX
