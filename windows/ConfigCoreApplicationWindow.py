from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class ConfigCoreApplicationWindow(QWidget):
    clicked = pyqtSignal()

    def __init(self):
        super(ConfigCoreApplicationWindow, self).__init__()
        self.__init_window()

    def __get_label_number_phone(self):
        label = QLabel()

    def __init_window(self):
        layout = QVBoxLayout()
        label_number_phone = self.__get_label_number_phone()
        self.setLayout(layout)
        self.setMaximumSize(400, 400)
        self.setMinimumSize(400, 400)

