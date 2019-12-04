import re

from PyQt5.QtCore import pyqtSignal, Qt, QRegularExpression
from PyQt5.QtGui import QIcon, QIntValidator, QRegularExpressionValidator
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QFormLayout, QToolButton, QMessageBox

from services.QueriesService import QueriesService


class ConfigCoreApplicationWindow(QWidget):
    clicked = pyqtSignal()

    def __init__(self):
        super(ConfigCoreApplicationWindow, self).__init__()
        self.__init_window()
        self.__service = QueriesService()
        self.__load_data()

    def __load_data(self):
        self.config_data = {}
        data = self.__service.get_configuration_core_application()
        self.config_data['ID'] = data['ID'] if data is not None else 0

        if data is not None:
            self.input_phone.setText(str(data['PHONE_NUMBER']))
            self.input_time_get_data_monitoring.setText(str(data['TIME_BETWEEN_CONSULTS']))

    def __get_label_number_phone(self):
        label = QLabel()
        label.setText("Número de telefone para notificações:")
        label.setStyleSheet("font-weight:bold;font-size:14px;")
        return label

    def __get_input_phone(self):
        input = QLineEdit()
        regex_phone = QRegularExpression("^(?:(55\d{2})|\d{2})[6-9]\d{8}$")
        input.setValidator(QRegularExpressionValidator(regex_phone))
        input.setMaximumWidth(265)
        return input

    def __get_label_time_get_data_monitoring(self):
        label = QLabel()
        label.setText("Intervalo de tempo para verificar dados:")
        label.setStyleSheet("font-weight:bold;font-size:14px;")
        return label

    def __get_input_time_get_data_monitoring(self):
        input = QLineEdit()
        input.setValidator(QIntValidator())
        input.setMaximumHeight(90)
        input.setMaximumWidth(100)
        input.setStyleSheet("font-size:30px;")
        input.setMaxLength(3)

        return input

    def __get_label_seconds(self):
        label = QLabel()
        label.setText("Minutos")
        label.setStyleSheet("font-weight:bold;font-size:14px;")

        return label

    def __save_data(self):
        self.config_data['TIME_BETWEEN_CONSULTS'] = self.input_time_get_data_monitoring.text()
        self.config_data['PHONE_NUMBER'] = self.input_phone.text()

        if len(self.config_data['PHONE_NUMBER']) == 0 or \
                len(self.config_data['TIME_BETWEEN_CONSULTS']) == 0 or self.config_data['PHONE_NUMBER'] == 0:
            QMessageBox.about(self, "Erro", "Dados são obrigatórios!")

        else:
            self.__service.save_core_data(self.config_data)
            self.clicked.emit()


    def __get_button_save(self):
        button = QToolButton()
        icon = QIcon("./icons/save.svg")
        button.setText("Salvar")
        button.setIcon(icon)
        button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        button.setStyleSheet("font-size:16px;margin-left:190px;margin-top:10px;")
        button.clicked.connect(self.__save_data)
        return button

    def __get_main_layout(self, child_layout):
        layout = QVBoxLayout()
        label_number_phone = self.__get_label_number_phone()
        self.input_phone = self.__get_input_phone()
        button_save = self.__get_button_save()
        label_time_get_data_monitoring = self.__get_label_time_get_data_monitoring()
        layout.addWidget(label_number_phone)
        layout.addWidget(self.input_phone)
        layout.addWidget(label_time_get_data_monitoring)
        layout.addLayout(child_layout)
        layout.addWidget(button_save)
        layout.setContentsMargins(60, 20, 0, 160)

        return layout

    def __get_child_layout(self):
        layout = QHBoxLayout()
        self.input_time_get_data_monitoring = self.__get_input_time_get_data_monitoring()
        label_seconds = self.__get_label_seconds()
        layout.addWidget(self.input_time_get_data_monitoring)
        layout.addWidget(label_seconds)
        return layout

    def __align_itens(self,layout):
        self.setLayout(layout)
        self.setMaximumSize(400, 400)
        self.setMinimumSize(400, 400)
        self.setContentsMargins(0, 80, 0, 0)

    def __init_window(self):
        self.setWindowTitle("Configurar")
        child_layout = self.__get_child_layout()
        layout = self.__get_main_layout(child_layout)
        self.__align_itens(layout)

