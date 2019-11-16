import io, sqlite3

class QueriesService():
    def __init__(self):
        self.__conn = sqlite3.connect("data.db")
        self.__cursor = self.__conn.cursor()

    def run_sql_initial(self):
        file = io.open('./scripts/initial.sql', 'r').read()
        self.__conn.executescript(file)

    def save_smartband_data(self,mac,name, id):
        try:
            if id == 0:
                query = """INSERT INTO CONFIG_SMARTBAND (NAME, MAC_ADDRESS) VALUES('{name}', '{mac}');""".format(name=name,
                                                                                                     mac=mac)
            else:
                query = """UPDATE CONFIG_SMARTBAND SET NAME = '{name}', MAC_ADDRESS = '{mac}' WHERE ID = {id}""".format(name=name,
                                                                                                                        mac=mac,
                                                                                                                        id=id)

            self.__cursor.execute(query)
            self.__conn.commit()
        except Exception as e:
            print(e)

    def get_configuration_smartband(self):
        data = []
        self.__cursor.execute("""
        SELECT * FROM CONFIG_SMARTBAND ORDER BY name;
        """)

        for row in self.__cursor.fetchall():
            data.append(row)

        if len(data) == 0:
            return None
        else:
            return list(data[0])