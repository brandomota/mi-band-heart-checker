from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolButton


class MonitoringWindow(QWidget):
    def __init__(self):
        super(MonitoringWindow, self).__init__()
        self.__init_window()

    def __get_label_header(self):
        label = QLabel()
        label.setText("Monitoramento")
        label.setStyleSheet("font-weight:bold;font-size:16px;")

        return label

    def __get_button_back_menu(self):
        button = QToolButton()
        return button

    def __init_window(self):
        layout = QVBoxLayout()
        layout.addStretch(1)
        label_header = self.__get_label_header()
        button_back = self.__get_button_back_menu()
        layout.addWidget(label_header)
        self.setLayout(layout)
        self.setMaximumSize(300, 300)
        self.setMinimumSize(300, 300)