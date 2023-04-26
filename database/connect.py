import psycopg2

from cliente.sql import SQLCliente
from livro.sql import SQlLivro
from aluguel.sql import SQLAluguel
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
        cursor.execute(SQlLivro._SCRIPT_CREATE_TABLE)
        cursor.execute(SQLAluguel._SCRIPT_CREATE_TABLE)
        self._connect.commit()

    def sql_new(self):
        return