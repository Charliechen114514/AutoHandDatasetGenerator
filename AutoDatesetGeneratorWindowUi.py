# Form implementation generated from reading ui file 'AutoDatesetGeneratorWindowUi.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(979, 656)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_operation_bar = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_operation_bar.setObjectName("widget_operation_bar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_operation_bar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_settings = QtWidgets.QWidget(parent=self.widget_operation_bar)
        self.widget_settings.setObjectName("widget_settings")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_tell_this_is_settings_table = QtWidgets.QLabel(parent=self.widget_settings)
        self.label_tell_this_is_settings_table.setMaximumSize(QtCore.QSize(16777215, 70))
        self.label_tell_this_is_settings_table.setObjectName("label_tell_this_is_settings_table")
        self.verticalLayout_2.addWidget(self.label_tell_this_is_settings_table)
        self.widget_settings_core = QtWidgets.QWidget(parent=self.widget_settings)
        self.widget_settings_core.setObjectName("widget_settings_core")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_settings_core)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_path_settings = QtWidgets.QWidget(parent=self.widget_settings_core)
        self.widget_path_settings.setObjectName("widget_path_settings")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_path_settings)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_tell_save_path = QtWidgets.QLabel(parent=self.widget_path_settings)
        self.label_tell_save_path.setMinimumSize(QtCore.QSize(0, 35))
        self.label_tell_save_path.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_tell_save_path.setWordWrap(True)
        self.label_tell_save_path.setObjectName("label_tell_save_path")
        self.verticalLayout_5.addWidget(self.label_tell_save_path)
        self.btn_set_saving_path = QtWidgets.QPushButton(parent=self.widget_path_settings)
        self.btn_set_saving_path.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_set_saving_path.setObjectName("btn_set_saving_path")
        self.verticalLayout_5.addWidget(self.btn_set_saving_path)
        self.verticalLayout_7.addWidget(self.widget_path_settings)
        self.widget_cur_label_name = QtWidgets.QWidget(parent=self.widget_settings_core)
        self.widget_cur_label_name.setObjectName("widget_cur_label_name")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_cur_label_name)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_label_name = QtWidgets.QLineEdit(parent=self.widget_cur_label_name)
        self.lineEdit_label_name.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_label_name.setObjectName("lineEdit_label_name")
        self.verticalLayout_8.addWidget(self.lineEdit_label_name)
        self.verticalLayout_7.addWidget(self.widget_cur_label_name)
        self.widget_auto_setings = QtWidgets.QWidget(parent=self.widget_settings_core)
        self.widget_auto_setings.setObjectName("widget_auto_setings")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_auto_setings)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_timer_settings = QtWidgets.QWidget(parent=self.widget_auto_setings)
        self.widget_timer_settings.setObjectName("widget_timer_settings")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_timer_settings)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_display_freq = QtWidgets.QLabel(parent=self.widget_timer_settings)
        self.label_display_freq.setObjectName("label_display_freq")
        self.horizontalLayout_4.addWidget(self.label_display_freq)
        self.time_set_spinBox = QtWidgets.QSpinBox(parent=self.widget_timer_settings)
        self.time_set_spinBox.setMinimum(1)
        self.time_set_spinBox.setMaximum(10)
        self.time_set_spinBox.setObjectName("time_set_spinBox")
        self.horizontalLayout_4.addWidget(self.time_set_spinBox)
        self.label_s = QtWidgets.QLabel(parent=self.widget_timer_settings)
        self.label_s.setObjectName("label_s")
        self.horizontalLayout_4.addWidget(self.label_s)
        self.verticalLayout_9.addWidget(self.widget_timer_settings)
        self.btn_auto_manual = QtWidgets.QPushButton(parent=self.widget_auto_setings)
        self.btn_auto_manual.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_auto_manual.setObjectName("btn_auto_manual")
        self.verticalLayout_9.addWidget(self.btn_auto_manual)
        self.btn_auto_start = QtWidgets.QPushButton(parent=self.widget_auto_setings)
        self.btn_auto_start.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_auto_start.setObjectName("btn_auto_start")
        self.verticalLayout_9.addWidget(self.btn_auto_start)
        self.verticalLayout_7.addWidget(self.widget_auto_setings)
        self.widget_manual_fetch = QtWidgets.QWidget(parent=self.widget_settings_core)
        self.widget_manual_fetch.setObjectName("widget_manual_fetch")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_manual_fetch)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_manual = QtWidgets.QPushButton(parent=self.widget_manual_fetch)
        self.btn_manual.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_manual.setObjectName("btn_manual")
        self.verticalLayout_6.addWidget(self.btn_manual)
        self.verticalLayout_7.addWidget(self.widget_manual_fetch)
        self.widget_btn_settings = QtWidgets.QWidget(parent=self.widget_settings_core)
        self.widget_btn_settings.setObjectName("widget_btn_settings")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_btn_settings)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_select_mode = QtWidgets.QPushButton(parent=self.widget_btn_settings)
        self.btn_select_mode.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_select_mode.setObjectName("btn_select_mode")
        self.verticalLayout_4.addWidget(self.btn_select_mode)
        self.verticalLayout_7.addWidget(self.widget_btn_settings)
        self.verticalLayout_2.addWidget(self.widget_settings_core)
        self.verticalLayout_3.addWidget(self.widget_settings)
        self.horizontalLayout.addWidget(self.widget_operation_bar)
        self.widget_display_and_settings = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_display_and_settings.setMinimumSize(QtCore.QSize(700, 0))
        self.widget_display_and_settings.setObjectName("widget_display_and_settings")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_display_and_settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_displaying = QtWidgets.QWidget(parent=self.widget_display_and_settings)
        self.widget_displaying.setMinimumSize(QtCore.QSize(0, 400))
        self.widget_displaying.setObjectName("widget_displaying")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_displaying)
        self.gridLayout.setObjectName("gridLayout")
        self.label_displayRuntimeCapture = QtWidgets.QLabel(parent=self.widget_displaying)
        self.label_displayRuntimeCapture.setObjectName("label_displayRuntimeCapture")
        self.gridLayout.addWidget(self.label_displayRuntimeCapture, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_displaying)
        self.widget_settings_of_camera = QtWidgets.QWidget(parent=self.widget_display_and_settings)
        self.widget_settings_of_camera.setObjectName("widget_settings_of_camera")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_settings_of_camera)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_depatch_gain = QtWidgets.QWidget(parent=self.widget_settings_of_camera)
        self.widget_depatch_gain.setObjectName("widget_depatch_gain")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_depatch_gain)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_open_this = QtWidgets.QPushButton(parent=self.widget_depatch_gain)
        self.btn_open_this.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_open_this.setObjectName("btn_open_this")
        self.horizontalLayout_2.addWidget(self.btn_open_this)
        self.comboBox_cameralist = QtWidgets.QComboBox(parent=self.widget_depatch_gain)
        self.comboBox_cameralist.setMinimumSize(QtCore.QSize(0, 50))
        self.comboBox_cameralist.setObjectName("comboBox_cameralist")
        self.horizontalLayout_2.addWidget(self.comboBox_cameralist)
        self.horizontalLayout_3.addWidget(self.widget_depatch_gain)
        self.verticalLayout.addWidget(self.widget_settings_of_camera)
        self.horizontalLayout.addWidget(self.widget_display_and_settings)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_tell_this_is_settings_table.setText(_translate("MainWindow", "设置表"))
        self.label_tell_save_path.setText(_translate("MainWindow", "根路径: "))
        self.btn_set_saving_path.setText(_translate("MainWindow", "设置导出位置"))
        self.label_display_freq.setText(_translate("MainWindow", "采集频率"))
        self.label_s.setText(_translate("MainWindow", "s"))
        self.btn_auto_manual.setText(_translate("MainWindow", "手动采集"))
        self.btn_auto_start.setText(_translate("MainWindow", "点击开始自动采集"))
        self.btn_manual.setText(_translate("MainWindow", "点击开始手动采集"))
        self.btn_select_mode.setText(_translate("MainWindow", "自动采集"))
        self.label_displayRuntimeCapture.setText(_translate("MainWindow", "请选择可用的摄像头，然后打开 ;)"))
        self.btn_open_this.setText(_translate("MainWindow", "打开摄像头"))
