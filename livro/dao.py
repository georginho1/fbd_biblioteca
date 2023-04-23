from flask import Response

from database.connect import ConnectDataBase
from livro.modelo import Livro
from livro.sql import SQlLivro
class DaoLivro:
    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def salvar(self, livro):
        cursor = self.connect.cursor()
        cursor.execute(SQlLivro._SCRIPT_INSERT,(livro.nome, livro.autor))

        self.connect.commit()
        id = cursor.fetchone()[0]
        return id

    def get_livro(self, buscar = None):
        cursor = self.connect.cursor()
        sql = SQlLivro._SELECT_BUSCA.format(SQlLivro._NOME_TABELA, buscar) if buscar else SQlLivro._SELECT_ALL

        cursor.execute(sql)
        livros = []
        coluns_name = [desc[0] for desc in cursor.description]
        for livro in cursor.fetchall():
            data = dict(zip(coluns_name, livro))
            livros.append(Livro(**data).get_json())
        return livros

    def get_by_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQlLivro._SELECT_ID,(str(id)))
        livro = cursor.fetchone()

        if not livro:
            return None
        coluns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(coluns_name, livro))
        return Livro(**data)

    def atualizar(self, livro):
        cursor = self.connect.cursor()
        cursor.execute(SQlLivro._UPDATE_BY_ID,(livro.nome,livro.autor))
        self.connect.commit()
        return True