from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolButton

class MonitoringWindow(QWidget):
    clicked = pyqtSignal()

    def __init__(self):
        super(MonitoringWindow, self).__init__()
        self.__init_window()

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