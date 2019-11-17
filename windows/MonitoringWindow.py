from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
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

    def __open_main_window(self):
        try:
            from windows.MenuWindow import MainWindow
            main_window = MainWindow()
            main_window.show()

            #self.close()
        except Exception as e:
            print(e)


    def __get_button_back_menu(self):
        icon = QIcon("./icons/back.svg")
        button = QToolButton()
        button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        button.setIcon(icon)
        button.setText("Voltar")
        button.clicked.connect(self.__open_main_window)
        return button

    def __init_window(self):
        layout = QVBoxLayout()
        layout.addStretch(1)
        label_header = self.__get_label_header()
        button_back = self.__get_button_back_menu()
        layout.addWidget(button_back)
        layout.addWidget(label_header)
        self.setLayout(layout)
        self.setMaximumSize(300, 300)
        self.setMinimumSize(300, 300)