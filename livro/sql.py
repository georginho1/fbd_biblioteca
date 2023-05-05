
class SQlLivro:
    _NOME_TABELA= "livro"
    _SCRIPT_CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA}(' \
                           f'id serial primary key,' \
                           f'nome varchar(255),' \
                           f'autor varchar(255))'

    _SCRIPT_INSERT = f'INSERT INTO {_NOME_TABELA}(nome, autor) ' \
                     f'values(%s,%s) RETURNING id'

    _SELECT_ALL = f'SELECT * FROM {_NOME_TABELA}'

    _SELECT_ID = f'SELECT * FROM {_NOME_TABELA} WHERE ID=%s'

    _SELECT_BUSCA = "SELECT * FROM {} where nome ILIKE '%{}%'"

    _UPDATE_BY_ID = f'UPDATE {_NOME_TABELA} SET nome=%s, autor=%s' \
                    f'WHERE id=%s'