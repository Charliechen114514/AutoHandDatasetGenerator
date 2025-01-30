from Core.CameraCapture import CameraInfo

class CameraDeviceUtils:
    INVALID_CAMERA_INDEX:int = -1
    @staticmethod
    def search_from_list(lists_of_cameras_info: list[CameraInfo], name: str) -> int:
        for each_device in lists_of_cameras_info:
            if each_device.name == name:
                return each_device.index
        return CameraDeviceUtils.INVALID_CAMERA_INDEX
