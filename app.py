from PyQt5.QtWidgets import QApplication

from windows.MainWindow import MainWindow

app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec_()