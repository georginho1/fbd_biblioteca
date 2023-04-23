
class Livro(object):
    def __init__(self, nome,autor, id = None):
        self.nome = nome
        self.autor = autor
        self.id = id

    def get_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'autor': self.autor
        }