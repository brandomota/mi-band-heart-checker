from PyQt5.QtCore import QSize
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QStackedWidget, QMainWindow

from windows.ConfigWindow import ConfigWindow
from windows.MenuWindow import MenuWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__init_window()

    def __change_screen(self, target):
        print(target)

    def __init_window(self):
        self.setMaximumSize(QSize(400,400))
        self.setMinimumSize(QSize(400,400))
        self.setWindowTitle("MiBand Heart Check")
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.menu_window_widget = MenuWindow()
        self.config_window_widget = ConfigWindow()
        self.central_widget.addWidget(self.menu_window_widget)
        self.central_widget.addWidget(self.config_window_widget)
        self.menu_window_widget.clicked.connect(self.__change_screen)
        self.central_widget.setCurrentWidget(self.menu_window_widget)

