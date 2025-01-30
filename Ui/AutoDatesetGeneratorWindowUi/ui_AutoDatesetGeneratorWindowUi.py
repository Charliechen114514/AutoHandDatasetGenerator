# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoDatesetGeneratorWindowUi.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_AutoDatesetGeneratorWindow(object):
    def setupUi(self, AutoDatesetGeneratorWindow):
        if not AutoDatesetGeneratorWindow.objectName():
            AutoDatesetGeneratorWindow.setObjectName(u"AutoDatesetGeneratorWindow")
        AutoDatesetGeneratorWindow.resize(979, 656)
        self.centralwidget = QWidget(AutoDatesetGeneratorWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_operation_bar = QWidget(self.centralwidget)
        self.widget_operation_bar.setObjectName(u"widget_operation_bar")

        self.horizontalLayout_3.addWidget(self.widget_operation_bar)

        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 239, 495))
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.label_tell_save_path = QLabel(self.page_3)
        self.label_tell_save_path.setObjectName(u"label_tell_save_path")
        self.label_tell_save_path.setMinimumSize(QSize(0, 35))
        self.label_tell_save_path.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_tell_save_path.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_tell_save_path)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_set_saving_path = QPushButton(self.page_3)
        self.btn_set_saving_path.setObjectName(u"btn_set_saving_path")
        self.btn_set_saving_path.setMinimumSize(QSize(0, 50))
        icon = QIcon()
        icon.addFile(u":/icons/toolbox/toolbox/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_set_saving_path.setIcon(icon)

        self.verticalLayout_3.addWidget(self.btn_set_saving_path)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page_3, u"\u6570\u636e\u96c6\u6839\u8def\u5f84\u751f\u6210")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 239, 495))
        self.verticalLayout_10 = QVBoxLayout(self.page_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_7)

        self.widget = QWidget(self.page_4)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_display_label = QPushButton(self.widget)
        self.btn_display_label.setObjectName(u"btn_display_label")
        self.btn_display_label.setMinimumSize(QSize(20, 20))
        self.btn_display_label.setMaximumSize(QSize(20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/icons/toolbox/toolbox/label.gif", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_display_label.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_display_label)

        self.setting_label = QLabel(self.widget)
        self.setting_label.setObjectName(u"setting_label")
        self.setting_label.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_5.addWidget(self.setting_label)


        self.verticalLayout_10.addWidget(self.widget)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.lineEdit_label_name = QLineEdit(self.page_4)
        self.lineEdit_label_name.setObjectName(u"lineEdit_label_name")
        self.lineEdit_label_name.setMinimumSize(QSize(0, 50))

        self.verticalLayout_10.addWidget(self.lineEdit_label_name)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_6)

        self.toolBox.addItem(self.page_4, u"\u8bbe\u7f6e\u6570\u636e\u96c6\u6807\u7b7e")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 239, 495))
        self.verticalLayout_11 = QVBoxLayout(self.page_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_auto_setings = QWidget(self.page_5)
        self.widget_auto_setings.setObjectName(u"widget_auto_setings")
        self.verticalLayout_5 = QVBoxLayout(self.widget_auto_setings)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)

        self.widget_timer_settings = QWidget(self.widget_auto_setings)
        self.widget_timer_settings.setObjectName(u"widget_timer_settings")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_timer_settings)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_display_freq = QLabel(self.widget_timer_settings)
        self.label_display_freq.setObjectName(u"label_display_freq")

        self.horizontalLayout_4.addWidget(self.label_display_freq)

        self.time_set_spinBox = QSpinBox(self.widget_timer_settings)
        self.time_set_spinBox.setObjectName(u"time_set_spinBox")
        self.time_set_spinBox.setMinimum(1)
        self.time_set_spinBox.setMaximum(10)

        self.horizontalLayout_4.addWidget(self.time_set_spinBox)

        self.label_s = QLabel(self.widget_timer_settings)
        self.label_s.setObjectName(u"label_s")

        self.horizontalLayout_4.addWidget(self.label_s)


        self.verticalLayout_5.addWidget(self.widget_timer_settings)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.btn_possible_help = QPushButton(self.widget_auto_setings)
        self.btn_possible_help.setObjectName(u"btn_possible_help")
        self.btn_possible_help.setMinimumSize(QSize(0, 50))
        icon2 = QIcon()
        icon2.addFile(u":/icons/toolbox/toolbox/check_infos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_possible_help.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.btn_possible_help)

        self.btn_auto_start = QPushButton(self.widget_auto_setings)
        self.btn_auto_start.setObjectName(u"btn_auto_start")
        self.btn_auto_start.setEnabled(False)
        self.btn_auto_start.setMinimumSize(QSize(0, 50))
        icon3 = QIcon()
        icon3.addFile(u":/icons/toolbox/toolbox/capture_hand.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_auto_start.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.btn_auto_start)

        self.btn_auto_manual = QPushButton(self.widget_auto_setings)
        self.btn_auto_manual.setObjectName(u"btn_auto_manual")
        self.btn_auto_manual.setEnabled(False)
        self.btn_auto_manual.setMinimumSize(QSize(0, 50))
        self.btn_auto_manual.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.btn_auto_manual)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.verticalLayout_11.addWidget(self.widget_auto_setings)

        self.toolBox.addItem(self.page_5, u"\u91c7\u96c6\u8bbe\u8ba1")

        self.horizontalLayout_3.addWidget(self.toolBox)

        self.widget_display_and_settings = QWidget(self.centralwidget)
        self.widget_display_and_settings.setObjectName(u"widget_display_and_settings")
        self.widget_display_and_settings.setMinimumSize(QSize(700, 0))
        self.verticalLayout = QVBoxLayout(self.widget_display_and_settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_displaying = QWidget(self.widget_display_and_settings)
        self.widget_displaying.setObjectName(u"widget_displaying")
        self.widget_displaying.setMinimumSize(QSize(0, 400))
        self.verticalLayout_2 = QVBoxLayout(self.widget_displaying)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_displayRuntimeCapture = QLabel(self.widget_displaying)
        self.label_displayRuntimeCapture.setObjectName(u"label_displayRuntimeCapture")

        self.verticalLayout_2.addWidget(self.label_displayRuntimeCapture)


        self.verticalLayout.addWidget(self.widget_displaying)

        self.widget_settings_of_camera = QWidget(self.widget_display_and_settings)
        self.widget_settings_of_camera.setObjectName(u"widget_settings_of_camera")
        self.horizontalLayout = QHBoxLayout(self.widget_settings_of_camera)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_depatch_gain = QWidget(self.widget_settings_of_camera)
        self.widget_depatch_gain.setObjectName(u"widget_depatch_gain")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_depatch_gain)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_open_this = QPushButton(self.widget_depatch_gain)
        self.btn_open_this.setObjectName(u"btn_open_this")
        self.btn_open_this.setMinimumSize(QSize(0, 50))
        icon4 = QIcon()
        icon4.addFile(u":/icons/toolbox/toolbox/camera.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_open_this.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.btn_open_this)

        self.comboBox_cameralist = QComboBox(self.widget_depatch_gain)
        self.comboBox_cameralist.setObjectName(u"comboBox_cameralist")
        self.comboBox_cameralist.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_2.addWidget(self.comboBox_cameralist)


        self.horizontalLayout.addWidget(self.widget_depatch_gain)


        self.verticalLayout.addWidget(self.widget_settings_of_camera)


        self.horizontalLayout_3.addWidget(self.widget_display_and_settings)

        AutoDatesetGeneratorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AutoDatesetGeneratorWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 979, 33))
        AutoDatesetGeneratorWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AutoDatesetGeneratorWindow)
        self.statusbar.setObjectName(u"statusbar")
        AutoDatesetGeneratorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AutoDatesetGeneratorWindow)

        self.toolBox.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(AutoDatesetGeneratorWindow)
    # setupUi

    def retranslateUi(self, AutoDatesetGeneratorWindow):
        AutoDatesetGeneratorWindow.setWindowTitle(QCoreApplication.translate("AutoDatesetGeneratorWindow", u"MainWindow", None))
        self.label_tell_save_path.setText(QCoreApplication.translate("AutoDatesetGeneratorWindow", u"\u6839\u8def\u5f84: ", None))
        self.btn_set_saving_path.setText(QCoreApplication.translate("AutoDatesetGeneratorWindow", u"\u8bbe\u7f6e\u5bfc\u51fa\u4f4d\u7f6e", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("AutoDatesetGeneratorWindow", u"\u6570\u636e\u96c6\u6839\u8def\u5f84\u751f\u6210", None))
        self.btn_display_label.setText("")
        self.setting_label.setText(QCoreApplication.translate("AutoDatesetGeneratorWindow", u"\u5f53\u524d\u6807\u7b7e\uff1a", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("AutoDatesetGeneratorWindow", u"\u8bbe\u7f6e\u6570\u636e\u96c6\u6807\u7b7e", None))
        self.label_display_freq.setText(QCoreApplication.translate("AutoDatesetGeneratorWindow", u"\u91c7\u96c6\u9891\u7387", None))
        self.label_s.setText(QCoreApplication.translate("AutoDatesetGeneratorWindow", u"s", None))
        self.btn_possible_help.setText(QCoreApplication.translate("AutoDatesetGeneratorWindow", u"\u67e5\u770b\u5e2e\u52a9", None))
        self.btn_auto_start.setText(QCoreApplication.translate("AutoDatesetGeneratorWindow", u"\u5f00\u542f\u81ea\u52a8\u91c7\u96c6", None))
        self.btn_auto_manual.setText(QCoreApplication.translate("AutoDatesetGeneratorWindow", u"\u7acb\u523b\u8fdb\u884c\u4e00\u6b21\u91c7\u96c6", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("AutoDatesetGeneratorWindow", u"\u91c7\u96c6\u8bbe\u8ba1", None))
        self.label_displayRuntimeCapture.setText(QCoreApplication.translate("AutoDatesetGeneratorWindow", u"\u8bf7\u9009\u62e9\u53ef\u7528\u7684\u6444\u50cf\u5934\uff0c\u7136\u540e\u6253\u5f00 ;)", None))
        self.btn_open_this.setText(QCoreApplication.translate("AutoDatesetGeneratorWindow", u"\u6253\u5f00\u6444\u50cf\u5934", None))
    # retranslateUi

