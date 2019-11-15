from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QHBoxLayout, QToolButton


class App:

    def __get_button_config_pulseira(self):
        icon_pulseira = QIcon("./icons/wristwatch.svg")
        button = QToolButton()
        button.setIcon(icon_pulseira)
        button.setStyleSheet("width: 120px; height: 120px")
        button.setIconSize(QSize(50,50))
        button.setText("Configurar pulseira...")
        #button.setToolButtonStyle('ToolButtonTextUnderIcon')
        return  button

    def __init__(self):
        app = QApplication([])

        window_main = QWidget()
        layout = QHBoxLayout()
        layout.addStretch(1)
        button_config_pulseira = self.__get_button_config_pulseira()

        layout.addWidget(button_config_pulseira)
        window_main.setMinimumSize(400, 400)
        window_main.setLayout(layout)
        window_main.setWindowTitle("MiBand Heart Check")
        window_main.show()
        app.exec_()



app = App()