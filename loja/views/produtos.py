# -*- coding: utf-8 -*-
from typing import Union

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from loja.extensions.database import db
from loja.models import Produto
from loja.serializers import produto_schema
from loja.serializers import produtos_schema


blueprint = Blueprint("produtos", __name__, url_prefix="/v1/produtos")

# create produtos endpoint
@blueprint.route("/", methods=["POST"])
@jwt_required
def add_prod():
    nome = request.json['nome']
    preco = request.json['preco']
    descricao = request.json['descricao']
    
    new_prod = Produto(nome, preco, descricao)

    db.session.add(new_prod)
    db.session.commit()


    return produto_schema.jsonify(new_prod)

# get all produtos endpoint
@blueprint.route("/", methods=["GET"])
def get_prod():
    all_prods = Produto.query.all()
    result = produtos_schema.dump(all_prods)

    return jsonify(result)

# get produtos by id endpoint
@blueprint.route("/<id>", methods=["GET"])
def prod_detail(id):
    prod = Produto.query.get(id)

    return produto_schema.jsonify(prod)

# update produtos by id endpoint
@blueprint.route("/<id>", methods=["PUT"])
@jwt_required
def prod_update(id):
    prod = Produto.query.get(id)

    nome = request.json['nome']
    preco = request.json['preco']
    descricao = request.json['descricao']
    dt_criacao = request.json['dt_criacao']

    prod.nome = nome
    prod.preco = preco
    prod.descricao = descricao
    prod.dt_criacao = dt_criacao

    db.session.commit()

    return produto_schema.jsonify(prod)

# delete produtos by id endpoint
@blueprint.route("/<id>", methods=["DELETE"])
@jwt_required
def prod_delete(id):
    prod = Produto.query.get(id)
    db.session.delete(prod)
    db.session.commit()

    return produto_schema.jsonify(prod)
