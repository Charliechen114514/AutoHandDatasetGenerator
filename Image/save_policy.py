from abc import ABC, abstractmethod


class ImageSaveInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def gain_next_image_name(self):
        pass

    @abstractmethod
    def update_policy(self):
        pass

    @abstractmethod
    def reset_policy(self):
        pass


class ImageSavePolicy(ImageSaveInterface):
    def __init__(self):
        super().__init__()
        self.__cnt = 0

    def gain_next_image_name(self):
        self.update_policy()
        return str(self.__cnt)

    def update_policy(self):
        self.__cnt += 1

    def reset_policy(self):
        self.__cnt = 0
