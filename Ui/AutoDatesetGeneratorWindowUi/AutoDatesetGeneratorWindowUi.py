# System level dependencies
from loguru import logger
import sys

# Core Dependencies
from Core.CameraCapture import CameraCollector, CameraDeviceUtils
from Core.Common import PathUtils
from Core.CameraCapture.CameraRuntimeThread import DeviceNotFound, NoneFrame
from Core.MessageInformer import MessageInformer
from Core.ImageSaver import ImageSaver

# Ui Dependencies
from .ui_AutoDatesetGeneratorWindowUi import Ui_AutoDatesetGeneratorWindow
from Ui.Common.ui_path_utils import UiUtils
from Ui.DisplayHandler.DisplayHandler import DisplayHandler

# Pyside dependencies
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QTimer

class AutoDatesetGeneratorWindow(QMainWindow):
    def __init__(self, parent = None):
        self.__setup_logger()
        logger.trace("entering initialize...")
        super().__init__(parent)
        # Memory issue
        self.__devices_info = []
        self.__saved_root_dirent: str = ""
        self.__current_label:str = ""
        self.__handle_btn_open_close_camera_switch = False
        self.__handle_auto_mode_start_stop = False
        self.__internal_timer = QTimer()
        self.__image_saver = ImageSaver()
        # ui setup
        self.__Ui = Ui_AutoDatesetGeneratorWindow()
        self.__Ui.setupUi(self)
        self.refresh_camera_list()
        self.__check_if_accessible_to_open_camera()
        self.__init_connections()
        self.setWindowTitle("手部数据集生成器")

    def refresh_camera_list(self):
        camera_collector = CameraCollector()
        self.__devices_info = camera_collector.devices
        self.__Ui.comboBox_cameralist.addItems(camera_collector.devicesName)

    def finalize(self):
        logger.info("start finalize issue")

# ------------- Privates --------------
    def __setup_logger(self):
        logger.add(sys.stdout, level="TRACE")

    def __init_connections(self):
        self.__Ui.btn_set_saving_path.clicked.connect(
            self.__set_root_dirent
        )
        self.__Ui.lineEdit_label_name.textEdited.connect(
            self.__register_current_label
        )
        # Do the callback of camera open issue
        self.__Ui.btn_open_this.clicked.connect(
            self.__do_open_close_btn_slot
        )
        # Mode settings
        self.__Ui.btn_auto_manual.clicked.connect(self.__shell_gain_image)
        self.__Ui.btn_auto_start.clicked.connect(self.__handle_timer)
        # Period Fetch
        self.__internal_timer.timeout.connect(self.__shell_gain_image)
        # Help
        self.__Ui.btn_possible_help.clicked.connect(self.__handle_help)
    
    """
        handling the timer behaviour
    """
    def __handle_timer(self):
        self.__handle_auto_mode_start_stop = not self.__handle_auto_mode_start_stop
        if not self.__handle_auto_mode_start_stop:
            self.__internal_timer.stop()
            self.__Ui.btn_auto_start.setText("开启周期采集")
        else:
            self.__internal_timer.setInterval(self.__Ui.time_set_spinBox.value() * 1000)
            self.statusBar().showMessage("已经将定时器设置为” + self.__UI.time_set_spinBox.value() + “s一次捕获！")
            self.__internal_timer.start()
            self.__Ui.btn_auto_start.setText("关闭周期采集")

    def __set_root_dirent(self):
        path: str = UiUtils.fetch_selected_dirent(self, "选择数据集的保存文件夹")
        if path == "":
            logger.info(f"User cancelled selections")
            return
        self.__saved_root_dirent = path
        self.__Ui.label_tell_save_path.setText(f"根路径: {path}")
        logger.info(f"User select {path} as saved")
        self.__image_saver.set_image_save_dir(path_dir=path)
        self.__check_if_accessible_to_open_camera()

    def __register_current_label(self):
        label: str = self.__Ui.lineEdit_label_name.text()
        logger.info(f"User select {label} as current label")
        self.__current_label = label
        self.__image_saver.set_label_name(label)
        self.__Ui.setting_label.setText(f"当前标签为{label}")
        self.__check_if_accessible_to_open_camera()

    """
        following are the runtime check for 
        whether shell we avail some widgets
    """
    def __check_root_path_valid(self) -> bool:
        return PathUtils.check_paths_if_exsit(self.__saved_root_dirent)

    def __check_label_accessive(self) -> bool:
        return self.__current_label != ""

    def __config_ui_enable(self, enabled: bool):
        self.__Ui.btn_open_this.setEnabled(enabled)

    def __check_if_accessible_to_open_camera(self):
        enabled: bool = self.__check_root_path_valid()
        logger.info("pass the root path check?:" + str(enabled))
        enabled = enabled and self.__check_label_accessive()
        logger.info("pass the root label check?:" + str(enabled))
        self.__config_ui_enable(enabled)

    def __on_set_runtime_widgets_enable(self, enabled: bool):
        if enabled:
            self.__Ui.btn_open_this.setText("打开摄像头")
            self.__Ui.statusbar.showMessage("摄像头关闭")
        else:
            self.__Ui.btn_open_this.setText("关闭摄像头")
            self.__Ui.statusbar.showMessage("摄像头开启")
        self.__Ui.lineEdit_label_name.setEnabled(enabled)
        self.__Ui.btn_set_saving_path.setEnabled(enabled) 
        self.__Ui.comboBox_cameralist.setEnabled(enabled)
        self.__Ui.btn_auto_manual.setEnabled(not enabled)
        self.__Ui.btn_auto_start.setEnabled(not enabled)

    def __callback_of_open_camera(self):
        logger.info("User open the camera, do the job")
        self.__on_set_runtime_widgets_enable(False)
        # Fetch the index
        name = self.__Ui.comboBox_cameralist.currentText()
        index: int = CameraDeviceUtils.search_from_list(self.__devices_info, name)
        try:
            self.__display_handle = DisplayHandler(index, self.__Ui.label_displayRuntimeCapture)
            self.__display_handle.start_display()
            self.__Ui.statusbar.showMessage("摄像头开启成功!现在正在显示展示图象...")
        except DeviceNotFound as e:
            MessageInformer.invalid_camera_name(self)
            return
        except NoneFrame as e:
            MessageInformer.tell_dry_frame_error(self)
        except Exception as e:
            MessageInformer.tell_internal_error(self, str(e))        

    def __close_camera(self):
        if self.__handle_auto_mode_start_stop:
            self.__handle_timer()
        self.__on_set_runtime_widgets_enable(True)
        self.__Ui.btn_open_this.setText("开始采集数据集")
        self.__display_handle.set_stop()
        del self.__display_handle
        self.__display_handle = None    
    

    def __do_open_close_btn_slot(self):
        self.__handle_btn_open_close_camera_switch = not self.__handle_btn_open_close_camera_switch
        if self.__handle_btn_open_close_camera_switch:
            return self.__callback_of_open_camera()
        else:
            return self.__close_camera()

    def __shell_gain_image(self):
        mat = self.__display_handle.export_current_fetch()
        if mat is None:
            return
        try:
            file_path = self.__image_saver.save_image(mat)
            self.statusBar().showMessage("已经保存图像在" + file_path + "上了")
        except FileNotFoundError as e:
            MessageInformer.file_un_found(self, str(e))       

    def __handle_help(self):
        QMessageBox.information(self, "帮助", 
                                "自动计时器模式将会按照周期辅助截取ROI, 值得注意的是当没有手部的时候不会截取。"
                                "也可以直接按下立刻截取进行手动的截图!")

    def closeEvent(self, event):
        if self.__display_handle is not None:
            logger.info("Erase handle")
            self.__close_camera()
        return super().closeEvent(event)