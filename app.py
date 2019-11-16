from PyQt5.QtWidgets import QApplication

from services.QueriesService import QueriesService
from windows.MainWindow import MainWindow

def exec_sql_initial():
    service = QueriesService()
    service.run_sql_initial()
    service.get_configuration_smartband()

exec_sql_initial()
app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec_()