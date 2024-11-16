from PyQt6.QtWidgets import QMessageBox, QWidget

class MessageInformer:
    @staticmethod
    def invalid_camera_name(widget: QWidget):
        QMessageBox.critical(widget, "发生错误","不可用的摄像头！请更换检查摄像头或者摄像头选项")

    @staticmethod
    def tell_internal_error(widget: QWidget, err: str):
        QMessageBox.critical(widget, "发生错误", "程序内部错误！,具体是: " + err)


    @staticmethod
    def tell_dry_frame_error(widget: QWidget):
        QMessageBox.critical(widget, "发生错误", "摄像头突发不存在可用的帧!")

    @staticmethod
    def file_un_found(widget: QWidget, file: str):
        QMessageBox.critical(widget, "发生错误", file + ",请检查路径！")

    @staticmethod
    def label_empty(w: QWidget):
        QMessageBox.critical(w, "发生错误", "标签名为空！请填写标签名！")