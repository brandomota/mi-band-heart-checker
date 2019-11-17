from PyQt5.QtCore import QSize
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QStackedWidget, QMainWindow

from windows.ConfigCoreApplicationWindow import ConfigCoreApplicationWindow
from windows.ConfigSmartbandWindow import ConfigSmartbandWindow
from windows.MenuWindow import MenuWindow
from windows.MonitoringWindow import MonitoringWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__init_window()

    def __change_screen_main(self):
        self.central_widget.setCurrentWidget(self.menu_window_widget)

    def __change_screen_config_smartband(self):
        self.central_widget.setCurrentWidget(self.config_smartband_window_widget)

    def __change_screen_monitoring(self):
        self.central_widget.setCurrentWidget(self.monitoring_window_widget)

    def __change_screen_config_core(self):
        self.central_widget.setCurrentWidget(self.config_core_window_widget)

    def __change_screen_about(self):
        pass

    def __define_bindings_widgets(self):
        self.menu_window_widget.clicked_menu_config_smartband.connect(self.__change_screen_config_smartband)
        self.menu_window_widget.clicked_menu_monitoring.connect(self.__change_screen_monitoring)
        self.menu_window_widget.clicked_menu_about.connect(self.__change_screen_about)
        self.menu_window_widget.clicked_menu_config_core.connect(self.__change_screen_config_core)
        self.config_smartband_window_widget.clicked.connect(self.__change_screen_main)
        self.monitoring_window_widget.clicked.connect(self.__change_screen_main)
        self.config_core_window_widget.clicked.connect(self.__change_screen_main)

    def __add_screen_widgets(self):
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.menu_window_widget = MenuWindow()
        self.config_smartband_window_widget = ConfigSmartbandWindow()
        self.monitoring_window_widget = MonitoringWindow()
        self.config_core_window_widget = ConfigCoreApplicationWindow()
        self.central_widget.addWidget(self.menu_window_widget)
        self.central_widget.addWidget(self.config_smartband_window_widget)
        self.central_widget.addWidget(self.monitoring_window_widget)
        self.central_widget.addWidget(self.config_core_window_widget)

    def __init_window(self):
        self.setMaximumSize(QSize(400,400))
        self.setMinimumSize(QSize(400,400))
        self.setWindowTitle("MiBand Heart Check")

        self.__add_screen_widgets()
        self.__define_bindings_widgets()

        self.central_widget.setCurrentWidget(self.menu_window_widget)

