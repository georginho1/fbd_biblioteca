from flask import Response

from database.connect import ConnectDataBase
from cliente.modelo import Cliente
from cliente.sql import SQLCliente

class DaoCliente:
    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def salvar(self, cliente):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._SCRIPT_INSERT,
                       (cliente.nome, cliente.telefone, cliente.endereco, cliente.cpf)
                       )
        self.connect.commit()
        id = cursor.fetchone()[0]
        return id

    def get_cliente(self, buscar = None):
        cursor = self.connect.cursor()
        sql = SQLCliente._SELECT_BUSCA.format(SQLCliente._NOME_TABELA,buscar) if buscar else SQLCliente._SELECT_ALL

        cursor.execute(sql)
        clientes = []
        coluns_name = [desc[0] for desc in cursor.description]
        for cliente in cursor.fetchall():
            data = dict(zip(coluns_name, cliente))
            clientes.append(Cliente(**data).get_json())
        return clientes

    def get_by_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._SELECT_ID,(str(id)))
        cliente = cursor.fetchone()
        if not cliente:
            return None
        coluns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(coluns_name, cliente))
        return Cliente(**data)

    def atualizar(self, cliente):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._UPDATE_BY_ID,(cliente.nome, cliente.telefone, cliente.endereco, cliente.cpf, cliente.id))
        self.connect.commit()
        return True