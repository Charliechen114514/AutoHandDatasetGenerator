from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QTimer

from WindowHelper import WindowClassHelper
from Camera.runtime_display_thread import DeviceNotFound, NoneFrame
from CaptureMode.capture_mode import AutoCaptureMode
from Image.image_saver import ImageSaver, ImageSaverUtils
from MessageInformer.message_informer import MessageInformer
from AutoDatesetGeneratorWindowUi import Ui_MainWindow
from Camera.camera_device import CameraDeviceFetcher, CameraDeviceInfo, CameraDeviceUtils
from Camera.runtime_display import RuntimeDisplay


class AutoDatesetGeneratorWindow(QMainWindow):
    """
        MainWindow Handle Main
    """
    WINDOW_TITLE = "手部数据集生成器"

    def __init__(self):
        super().__init__()  # 用于访问父类的方法和属性
        self.__UI = Ui_MainWindow()
        self.__UI.setupUi(self)
        self.__base_save_dir = ""
        self.__camera_devices: list[CameraDeviceInfo] = []
        # generate devices_list
        self.__capture_mode = AutoCaptureMode()
        self.__do_according_mode()
        self.__get_usable_cameras()
        self.__display_handle = None
        self.__image_saver = ImageSaver()
        self.__handle_btn_open_close_camera_switch = False
        self.__handle_auto_mode_start_stop = False
        self.__internal_timer = QTimer()
        self.__handle_the_capturing_widget(True)
        # self.__load_qss()
        self.setWindowTitle(AutoDatesetGeneratorWindow.WINDOW_TITLE)
        self.__init_connections()

    """
        using in init or the utils
        get the device's cameras
    """

    def __get_usable_cameras(self):
        fetcher = CameraDeviceFetcher()
        self.__camera_devices = fetcher.get_devices()
        self.__UI.comboBox_cameralist.addItems(fetcher.get_devices_name())

    """
        init MainWindow's slots and signals 
        call only in initializations
    """

    def __init_connections(self):
        self.__UI.btn_open_this.clicked.connect(self.__do_open_close_btn_slot)
        self.__internal_timer.timeout.connect(self.__shell_gain_image)
        self.__UI.btn_select_mode.clicked.connect(self.__switch_mode)
        self.__UI.btn_set_saving_path.clicked.connect(self.__set_base_dir)
        self.__UI.btn_manual.clicked.connect(self.__shell_gain_image)
        self.__UI.btn_auto_manual.clicked.connect(self.__shell_gain_image)
        self.__UI.btn_auto_start.clicked.connect(self.__handle_timer)

    """
        handling the timer behaviour
    """
    def __handle_timer(self):
        self.__handle_auto_mode_start_stop = not self.__handle_auto_mode_start_stop
        if not self.__handle_auto_mode_start_stop:
            self.__internal_timer.stop()
            self.__UI.btn_auto_start.setText("开启自动采集")
        else:
            self.__set_save_interval()
            self.__internal_timer.start()
            self.__UI.btn_auto_start.setText("关闭自动采集")

    def __load_qss(self):
        res, is_good = WindowClassHelper.gain_qss_file_string("./QSS/light/lightstyle.qss")
        if is_good:
            self.setStyleSheet(res)
        else:
            self.__set_message_below("加载失败: " + res)

    """
        handling the modes switch between the manually label 
        and auto label
    """
    def __switch_mode(self):
        if self.__capture_mode.is_auto_now():
            self.__capture_mode.set_to_manual()
        else:
            self.__capture_mode.set_to_auto()
        self.__do_according_mode()

    def __do_according_mode(self):
        if self.__capture_mode.is_auto_now():
            self.__UI.btn_select_mode.setText("自动模式")
        else:
            self.__UI.btn_select_mode.setText("手动模式")

    def __open_camera_by_current_selections(self):
        self.__set_message_below("摄像头正在开启...")
        if not self.__check_all_params():
            return
        camera_name = self.__UI.comboBox_cameralist.currentText()
        camera_index = CameraDeviceUtils.search_from_list(self.__camera_devices, camera_name)
        self.__handle_the_capturing_widget(False)
        self.__UI.btn_open_this.setText("结束采集数据")
        try:
            self.__display_handle = RuntimeDisplay(camera_index, self.__UI.label_displayRuntimeCapture)
            self.__display_handle.start_display()
            self.__set_message_below("摄像头开启成功!现在正在显示展示图象...")
        except DeviceNotFound as e:
            MessageInformer.invalid_camera_name(self)
            return
        except NoneFrame as e:
            MessageInformer.tell_dry_frame_error(self)
        except Exception as e:
            MessageInformer.tell_internal_error(self, str(e))

    def __close_camera(self):
        if self.__capture_mode.is_auto_now():
            self.__internal_timer.stop()
        self.__handle_the_capturing_widget(True)
        self.__UI.btn_open_this.setText("开始采集数据集")
        del self.__display_handle
        self.__display_handle = None

    def __do_open_close_btn_slot(self):
        self.__handle_btn_open_close_camera_switch = not self.__handle_btn_open_close_camera_switch
        if self.__handle_btn_open_close_camera_switch:
            return self.__open_camera_by_current_selections()
        else:
            return self.__close_camera()

    def __set_base_dir(self):
        path = ImageSaverUtils.gain_dir_save_path(self)
        if path == "":
            return False
        self.__base_save_dir = path
        self.__UI.label_tell_save_path.setText("根路径: " + self.__base_save_dir)

    def __check_path_before_run(self) -> bool:
        label = self.__UI.lineEdit_label_name.text()
        if label == "":
            MessageInformer.label_empty(self)
            return False
        if not ImageSaverUtils.check_dir_exist(self.__base_save_dir):
            MessageInformer.file_un_found(self, self.__base_save_dir)
            return False
        path = ImageSaverUtils.join_path(self.__base_save_dir, label)
        ImageSaverUtils.try_make_dir(path)
        self.__image_saver.set_image_save_dir(path_dir=path)
        return True

    def __handle_the_capturing_widget(self, state: bool):
        self.__handle_mode_related_widget(state)
        self.__UI.btn_set_saving_path.setEnabled(state)
        self.__UI.comboBox_cameralist.setEnabled(state)
        self.__UI.time_set_spinBox.setEnabled(state)
        self.__UI.lineEdit_label_name.setEnabled(state)
        self.__UI.btn_select_mode.setEnabled(state)

    """
        this function is used in manually/auto label 
        switch-behaviours! help prevent invalid operations
    """
    def __handle_mode_related_widget(self, state: bool):
        if self.__capture_mode.is_auto_now():
            self.__UI.btn_auto_start.setEnabled(not state)
            self.__UI.btn_auto_manual.setEnabled(not state)
            self.__UI.time_set_spinBox.setEnabled(state)
            self.__UI.btn_manual.setEnabled(False)
        else:
            self.__UI.btn_auto_start.setEnabled(False)
            self.__UI.btn_auto_manual.setEnabled(False)
            self.__UI.time_set_spinBox.setEnabled(False)
            self.__UI.btn_manual.setEnabled(not state)

    """
        gain image real impl
    """
    def __shell_gain_image(self):
        mat = self.__display_handle.export_current_fetch()
        if mat is None:
            return
        try:
            file_path = self.__image_saver.save_image(mat)
            self.__set_message_below("已经保存图像在" + file_path + "上了")
        except FileNotFoundError as e:
            MessageInformer.file_un_found(self, str(e))

    """
        interval setter
    """
    def __set_save_interval(self):
        self.__internal_timer.setInterval(self.__UI.time_set_spinBox.value() * 1000)
        self.__set_message_below("已经将定时器设置为” + self.__UI.time_set_spinBox.value() + “s一次捕获！")

    def __set_message_below(self, text: str):
        self.statusBar().showMessage(text)

    def __check_all_params(self) -> bool:
        if not self.__check_path_before_run():
            return False
        return True
