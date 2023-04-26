from database.connect import ConnectDataBase
from aluguel.sql import SQLAluguel

class DaoAluguel():
    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def salvar(self, aluguel):
        cliente = aluguel.cliente
        livro = aluguel.livro

        cursor = self.connect.cursor()

        cursor.execute(SQLAluguel._SCRIPT_INSERT,(cliente.id,livro.id, aluguel.dataRetirada,aluguel.dataEntrega))

        self.connect.commit()
        id = cursor.fetchone()[0]
        return id
    def get_por_cliente(self,id_cliente):
        cursor = self.connect.cursor()
        sql = SQLAluguel._SELECT_BY_CLIENTE_ID

        cursor.execute(sql, (str(id_cliente)))
        alugueis = []
        coluns_name = [desc[0] for desc in cursor.description]
        for cliente in cursor.fetchall():
            data = dict(zip(coluns_name, cliente))
            alugueis.append(data)
        return alugueis
