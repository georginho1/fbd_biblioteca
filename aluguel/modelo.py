class Aluguel(object):
    def __init__(self,cliente, livro, dataRetirada, dataEntrega, id = None):
        self.cliente = cliente
        self.livro = livro
        self.dataRetirada = dataRetirada
        self.dataEntrega = dataEntrega
        self.id = id

    def get_json(self):
        return {
            'id': self.id,
            'cliente': self.cliente.get_json(),
            'livro':self.livro.get_json(),
            'dataRetirada':self.dataRetirada,
            'dataEntrega': self.dataEntrega
        }