import io, sqlite3

class QueriesService():
    def __init__(self):
        self.__conn = sqlite3.connect("data.db")
        self.__conn.row_factory = sqlite3.Row
        self.__cursor = self.__conn.cursor()

    def run_sql_initial(self):
        file = io.open('./scripts/initial.sql', 'r').read()
        self.__conn.executescript(file)

    def save_smartband_data(self,mac,name, id):
        try:
            if id == 0:
                query = """INSERT INTO CONFIG_SMARTBAND (NAME, MAC_ADDRESS) VALUES('{name}', '{mac}');"""
                query.format(name=name,mac=mac)
            else:
                query = """UPDATE CONFIG_SMARTBAND SET NAME = '{name}', MAC_ADDRESS = '{mac}' WHERE ID = {id}"""
                query.format(name=name,mac=mac,id=id)

            self.__cursor.execute(query)
            self.__conn.commit()
        except Exception as e:
            print(e)

    def get_configuration_smartband(self):
        self.__cursor.execute("""
        SELECT * FROM CONFIG_SMARTBAND ORDER BY name;
        """)

        return self.__cursor.fetchone()

    def get_configuration_core_application(self):
        self.__cursor.execute("""
        SELECT * FROM CONFIG_CORE;
        """)

        return self.__cursor.fetchone()

    def save_core_data(self, data):

        if 'ID' not in data:
            query = """INSERT INTO CONFIG_CORE (PHONE_NUMBER, TIME_BETWEEN_CONSULTS) VALUES('{phone}', '{time}') """
            query.format(phone=data['PHONE_NUMBER'],time=data['TIME_BETWEEN_CONSULTS'])
        else:
            query = """UPDATE CONFIG_CORE SET PHONE_NUMBER = '{phone}', TIME_BETWEEN_CONSULTS = '{time}' WHERE ID = {id}""".format(phone=data['PHONE_NUMBER'],
                                                                                                                                   time=data['TIME_BETWEEN_CONSULTS'],
                                                                                                                                   id=data['ID'])

        self.__cursor.execute(query)
        self.__conn.commit()
