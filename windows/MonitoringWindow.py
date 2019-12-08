import _thread
from PyQt5.QtCore import Qt, pyqtSignal, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolButton
from time import sleep
from services.MiBandService import MiBandService
from services.QueriesService import QueriesService


class MonitoringWindow(QWidget):
    clicked = pyqtSignal()
    __is_monitoring = False

    def __init__(self):
        super(MonitoringWindow, self).__init__()
        self.queriesService = QueriesService()
        self.__init_window()
        self.__init_monitoring()

    #
    # def event(self, event):
    #     if event.type() == QEvent.ShowToParent:
    #       self.__init_monitoring()
    #
    #     if event.type() == QEvent.HideToParent and self.__is_monitoring:
    #         self.__stop_monitoring()
    #
    #     return super(MonitoringWindow, self).event(event)

    def __get_label_header(self):
        label = QLabel()
        label.setText("Monitoramento")
        label.setStyleSheet("font-weight:bold;font-size:30px;")
        label.setContentsMargins(70,0,0,40)
        return label

    def __open_main_window(self):
        self.clicked.emit()

    def __get_button_back_menu(self):
        icon = QIcon("./icons/back.svg")
        button = QToolButton()
        button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        button.setIcon(icon)
        button.setText("Voltar")
        button.clicked.connect(self.__open_main_window)
        return button

    def __set_color_black_label_bpm(self, label):
        label.setStyleSheet("font-size:50px;color:black;font-weight:bold")
        return label

    def __get_label_bpm(self):
        label = QLabel()
        label.setText("%d BPM" % self.__actual_bpm)
        label.setContentsMargins(100,0,0,0)

        return self.__set_color_black_label_bpm(label)

    def __get_mac_address_band(self):
        return self.queriesService.get_mac_address()

    def __get_time_sleep_check(self):
        return self.queriesService.get_time_sleep_check()



    def __init_monitoring(self):
        mac_address = self.__get_mac_address_band()
        time_sleep_check = self.__get_time_sleep_check()
        self.__start_heart_check(mac_address, time_sleep_check)
        #self._thread = _thread.start_new_thread()
        self.__is_monitoring = True

    def __start_heart_check(self,mac_address, time_sleep_check):
        miband = MiBandService(mac_address=mac_address, debug=True)
        miband.setSecurityLevel(level='medium')
        miband.initialize()
        sleep(10)
        miband.get_heart_rate_one_time()
        #sleep(120)

        # while True:
        #     self.__actual_bpm =
        #     print(self.__actual_bpm)
        #     sleep(time_sleep_check)

    def __stop_monitoring(self):
        print(self._thread)
        pass


    def __init_window(self):
        layout = QVBoxLayout()
        self.__actual_bpm = 0
        layout.addStretch(0.8)
        label_header = self.__get_label_header()
        button_back = self.__get_button_back_menu()
        self.label_bpm = self.__get_label_bpm()
        layout.addWidget(button_back)
        layout.addWidget(label_header)
        layout.addStretch(0.1)
        layout.addWidget(self.label_bpm)
        self.setContentsMargins(0,0,0,175)
        self.setLayout(layout)
        self.setMaximumSize(400, 400)
        self.setMinimumSize(400, 400)