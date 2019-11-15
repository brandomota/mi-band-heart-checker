from PyQt5.QtWidgets import QGridLayout, QWidget


class HeartCheckerService:
    def __init__(self):
        pass

    def open_configure_smartband_view(self,parent):
        window_configure_smartband = QWidget(parent=parent)
        window_configure_smartband.setWindowTitle("Configurar Pulseira")
        layout = QGridLayout()
        window_configure_smartband.show()
        return window_configure_smartband