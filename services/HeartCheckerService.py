from .QueriesService import QueriesService

class HeartCheckerService:
    def __init__(self):
        self.service = QueriesService()

    def save_data(self, mac, name, id=0):
        self.service.save_smartband_data(mac,name, id)

    def get_config_data(self):
        return self.service.get_configuration_smartband()
