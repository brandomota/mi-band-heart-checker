from PyQt5.QtWidgets import QWidget


class ConfigWindow(QWidget):
    def __init__(self):
        super(ConfigWindow, self).__init__()
        self.__init_window()

    def __init_window(self):
        self.setWindowTitle("segunda tela")
