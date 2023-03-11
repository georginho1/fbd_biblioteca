from flask import Flask, make_response, jsonify, request, Response
from database.connect import ConnectDataBase
from cliente.modelo import Cliente
from cliente.dao import DaoCliente

app = Flask(__name__)
ConnectDataBase().init_table()

dao_cliente = DaoCliente()


@app.route('/cliente/add/', methods=['POST'])
def add_cliente():
    data_cliente = dict(request.form)
    cliente = Cliente(**data_cliente)
    id = dao_cliente.salvar(cliente)
    cliente.id = id
    return make_response({})

@app.route('/clientes/', methods=['GET'])
def clientes():
    parametros = request.args
    buscar = parametros.get('buscar', None)
    clientes = dao_cliente.get_cliente(buscar)
    return make_response(jsonify(clientes))

@app.route('/cliente/<int:id>/', methods=['GET'])
def cliente_by_id(id: int):
    cliente = dao_cliente.get_by_id(id)
    if not cliente:
        return Response({}, status=404)
    return make_response(jsonify(cliente.get_json()))

@app.route('/cliente/<int:id>/', methods=['PUT'])
def atualizar_cliente(id: int):
    data_cliente = dict(request.form)
    cliente = dao_cliente.get_by_id(id)

    cliente.nome = data_cliente.get('nome')
    cliente.telefone = data_cliente.get('telefone')
    cliente.endereco = data_cliente.get('endereco')
    cliente.cpf = data_cliente.get('cpf')
    if dao_cliente.atualizar(cliente):
        return make_response(jsonify(cliente.get_json()))
    return Response({}, status=404)

app.run()