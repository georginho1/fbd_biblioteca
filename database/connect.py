import psycopg2

from cliente.sql import SQLCliente

class ConnectDataBase:
    def __init__(self):
        self._connect = psycopg2.connect(
            host="localhost",
            database ="fbd_biblioteca",
            user="postgres",
            password="root"
        )

    def get_instance(self):
        return self._connect

    def init_table(self):
        cursor = self._connect.cursor()
        cursor = self._connect.cursor()
        cursor.execute(SQLCliente._SCRIPT_CREATE_TABLE)
        self._connect.commit()

    def sql_new(self):
        return