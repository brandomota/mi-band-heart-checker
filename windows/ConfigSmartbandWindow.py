from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QToolButton, QMessageBox
import re

from services.HeartCheckerService import HeartCheckerService

class ConfigSmartbandWindow(QWidget):

    clicked = pyqtSignal()

    def __init__(self):
        super(ConfigSmartbandWindow, self).__init__()
        self.service = HeartCheckerService()
        self.__init_window()

    def __get_new_input(self):
        input = QLineEdit()
        input.setStyleSheet("font-size: 14px;max-width: 270px;margin-left:12px;")
        return input

    def __get_new_label(self, text):
        label = QLabel(text)
        label.setStyleSheet("font-weight:bold;font-size:16px;margin-left:7px;")
        return label

    def __save_data(self):
        mac = self.input_mac_device.text()
        name = self.input_name_device.text()
        pattern = re.compile("^[a-fA-F0-9:]{17}|[a-fA-F0-9]{12}$")

        if pattern.match(mac) != None:
            if self.data_config != None:
                self.service.save_data(mac, name, self.data_config[0])
            else:
                self.service.save_data(mac, name)

            self.clicked.emit()
        else:
            QMessageBox.about(self, "Erro", "O endereço MAC é invalido!")

    def __get_button_save(self):
        button = QToolButton()
        icon = QIcon("./icons/save.svg")
        button.setText("Salvar")
        button.setIcon(icon)
        button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        button.setStyleSheet("font-size:16px;margin-left:208px;margin-top:10px;")
        button.clicked.connect(self.__save_data)
        return button

    def __init_window(self):
        self.data_config = self.service.get_config_data()
        self.setWindowTitle("Configurar Pulseira")
        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.setContentsMargins(50, 0, 0, 160)
        self.input_mac_device = self.__get_new_input()
        self.input_name_device = self.__get_new_input()
        self.input_mac_device.setMaxLength(17)
        self.input_name_device.setMaxLength(50)

        if self.data_config != None:
            self.input_mac_device.setText(self.data_config[1])
            self.input_name_device.setText(self.data_config[2])

        label_select_device = self.__get_new_label("Endereço MAC da pulseira:")
        label_name_device = self.__get_new_label("Nome da pulseira:")
        button_save = self.__get_button_save()
        layout.addWidget(label_select_device)
        layout.addWidget(self.input_mac_device)
        layout.addWidget(label_name_device)
        layout.addWidget(self.input_name_device)
        layout.addWidget(button_save)
        self.setLayout(layout)
        self.setMaximumSize(400, 400)
        self.setMinimumSize(400, 400)
