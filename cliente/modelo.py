class Cliente(object):
    def __init__(self, nome, telefone, endereco, cpf, id = None):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cpf = cpf
        self.id = id

    def get_sql_insert(self):
        return

    def get_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco':self.endereco,
            'cpf':self.cpf
        }