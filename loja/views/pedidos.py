# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, JWTManager

from loja.extensions.database import db
from loja.models import Pedido, ItensPedido, Produto
from loja.serializers import pedido_schema, pedidos_schema, item_pedido_schema, itens_pedido_schema
from loja.serializers import produto_schema


blueprint = Blueprint("pedidos", __name__, url_prefix="/v1/pedidos")

# create pedido endpoint
@blueprint.route("/", methods=["POST"])
@jwt_required
def add_pedido():

    itens_pedido = request.json['itens_pedido']
    id_cliente = request.json['id_cliente']

    # itens pedido e soma de valores
    valor_total = 0
    for itens in itens_pedido:
        id_pedido = 1
        id_produto = itens['id_produto']
        quantidade = itens['quantidade']

        produto = Produto.query.get(id_produto)
        prod = produto_schema.dump(produto)
        valor = prod['preco']

        valor_total = valor_total + (quantidade * valor)
        str_valor_total = "R${},00".format(valor_total)
        
        new_item = ItensPedido(id_pedido, id_produto, quantidade)

        #insert new order item
        db.session.add(new_item)
        db.session.commit()

    new_pedido = Pedido(id_cliente, str_valor_total)

    #insert new order
    db.session.add(new_pedido)
    db.session.commit()

    return pedido_schema.jsonify(new_pedido)

# get all pedidos endpoint
@blueprint.route("/", methods=["GET"])
def get_pedido():
    all_pedidos = Pedido.query.all()
    result = pedidos_schema.dump(all_pedidos)

    return jsonify(result)


# get pedido detail endpoint
@blueprint.route("/<id>", methods=["GET"])
def pedido_detail(id):
    pedido = Pedido.query.get(id)

    return pedido_schema.jsonify(pedido)

# update pedidos by id endpoint
@blueprint.route("/<id>", methods=["PUT"])
@jwt_required
def pedido_update(id):
    pedido = Pedido.query.get(id)

    id_cliente = request.json['id_cliente']
    valor_total = request.json['valor_total']
    dt_criacao = request.json['dt_criacao']

    pedido.id_cliente = id_cliente
    pedido.valor_total = valor_total
    pedido.dt_criacao = dt_criacao

    db.session.commit()

    return pedido_schema.jsonify(pedido)


# delete pedido by ID endpoint
@blueprint.route("/<id>", methods=["DELETE"])
@jwt_required
def pedido_delete(id):
    pedido = Pedido.query.get(id)
    db.session.delete(pedido)
    db.session.commit()

    return pedido_schema.jsonify(pedido)


# get all itens_pedido endpoint
@blueprint.route("/itens_pedidos", methods=["GET"])
def get_itens_pedidos():
    all_itens_pedidos = ItensPedido.query.all()
    result = itens_pedido_schema.dump(all_itens_pedidos)

    return jsonify(result)

# get item_pedido detail endpoint
@blueprint.route("/itens_pedidos/<id>", methods=["GET"])
def get_item_pedido():
    result = ItensPedido.query.get(id)

    return item_pedido_schema.jsonify(result)

