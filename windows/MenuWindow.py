from PyQt5.QtCore import QSize, Qt, QMargins, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QToolButton, QGridLayout
from windows.ConfigWindow import ConfigWindow


class MenuWindow(QWidget):

    clicked = pyqtSignal()

    def __open_config_smartband(self):
        try:
            self.clicked.emit("config")
        except Exception as e:
            print(e)


    def __init_monitoring(self):
       pass

    def __open_configure_core_application(self):
        pass

    def __open_about(self):
        pass

    def __set_css_padrao_button(self, button):
        button.setStyleSheet("width: 120px; height: 120px; font-size:9px; font-weight: bold;text-transform:capitalize;")
        button.setIconSize(QSize(70, 70))

    def __get_button_config_smartband(self):
        icon_smartband = QIcon("./icons/wristwatch.svg")
        button = QToolButton()
        button.setIcon(icon_smartband)
        self.__set_css_padrao_button(button)
        button.setText("Configurar pulseira")
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.clicked.connect(self.__open_config_smartband)
        return button

    def __get_button_init_monitoring(self):
        icon_init_monitoring = QIcon("./icons/heartbeat.svg")
        button = QToolButton()
        button.setIcon(icon_init_monitoring)
        self.__set_css_padrao_button(button)
        button.setText("Inicar Monitoramento")
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.clicked.connect(self.__init_monitoring)
        return button

    def __get_button_configure_core_application(self):
        icon_configure_core_application = QIcon("./icons/settings.svg")
        button = QToolButton()
        button.setIcon(icon_configure_core_application)
        self.__set_css_padrao_button(button)
        button.setText("Configurar Aplicação")
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.clicked.connect(self.__open_configure_core_application)
        return button

    def __get_button_about(self):
        icon_about = QIcon("./icons/about.svg")
        button = QToolButton()
        button.setIcon(icon_about)
        self.__set_css_padrao_button(button)
        button.setText("Sobre")
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.clicked.connect(self.__open_about)
        return button

    def init_window(self):
        layout = QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setContentsMargins(QMargins(46, 1, 4, 1))
        layout.setHorizontalSpacing(40)
        self.button_config_smartband = self.__get_button_config_smartband()
        button_init_monitoring = self.__get_button_init_monitoring()
        button_configure_application_core = self.__get_button_configure_core_application()
        button_about = self.__get_button_about()

        layout.addWidget(self.button_config_smartband, 0, 0)
        layout.addWidget(button_init_monitoring, 0, 1)
        layout.addWidget(button_configure_application_core, 2, 0)
        layout.addWidget(button_about, 2, 1)
        self.setMinimumSize(380, 400)
        self.setMaximumSize(380, 400)
        self.setLayout(layout)

    def __init__(self):
        super().__init__()
        self.init_window()


