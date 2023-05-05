class SQLAluguel:
    _NOME_TABELA = 'aluguel'
    _TABLE_CLIENTE = 'cliente'
    _TABLE_LIVRO = 'livro'
    _SCRIPT_CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA}(' \
                           f'id serial primary key,' \
                           f'dataRetirada varchar(10),' \
                           f'dataEntrega varchar(10),' \
                           f'cliente_id int references cliente(id),' \
                           f'livro_id int references livro(id))'

    _SCRIPT_INSERT = f'INSERT INTO {_NOME_TABELA}(cliente_id,livro_id, dataRetirada,dataEntrega ) ' \
                        f'values(%s, %s, %s, %s) RETURNING id'

    _SELECT_BY_CLIENTE_ID = f'SELECT dataRetirada, dataEntrega, livro_id FROM {_NOME_TABELA} WHERE cliente_id=%s'

    _SELECT_BY_LIVRO_ID = f'SELECT dataRetirada, dataEntrega, cliente_id FROM {_NOME_TABELA} WHERE livro_id=%s'

    _SELECT_ALL_AND_CLIENTE = (f'select al.dataRetirada, al.dataEntrega, cl.nome, cl.cpf from {_NOME_TABELA} as al '
                               f'inner join {_TABLE_CLIENTE} as cl on cl.cliente_id = cl.id;')

