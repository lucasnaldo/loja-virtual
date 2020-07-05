# -*- coding: utf-8 -*-
import datetime
from typing import Union
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from loja.extensions.database import db
from loja.models import Cliente
from loja.serializers import cliente_schema
from loja.serializers import clientes_schema


blueprint = Blueprint("clientes", __name__, url_prefix="/v1/clientes")

# create clientes endpoint
@blueprint.route("/", methods=["POST"])
def add_user():
    nome = request.json['nome']
    email = request.json['email']
    password = request.json['password']
    endereco = request.json['endereco']
    data_nascimento = request.json['data_nascimento']
    
    new_user = Cliente(nome, email, password, endereco, data_nascimento)

    db.session.add(new_user)
    db.session.commit()

    return cliente_schema.jsonify(new_user)

# get all clientes endpoint
@blueprint.route("/", methods=["GET"])
def get_user():
    all_users = Cliente.query.all()
    result = clientes_schema.dump(all_users)
    lista_clean = []
    for item in result:
        result_clean = {}
        result_clean['nome'] = item['nome']
        result_clean['email'] = item['email']
        result_clean['endereco'] = item['endereco']
        result_clean['data_nascimento'] = item['data_nascimento']
        result_clean['dt_criacao'] = item['dt_criacao']
        lista_clean.append(result_clean)  

    return jsonify(lista_clean)

# get clientes by id endpoint
@blueprint.route("/<id>", methods=["GET"])
def user_detail(id):
    user = Cliente.query.get(id)

    return cliente_schema.jsonify(user)

# update clientes by id endpoint
@blueprint.route("/<id>", methods=["PUT"])
@jwt_required
def user_update(id):
    user = Cliente.query.get(id)

    nome = request.json['nome']
    email = request.json['email']
    password = request.json['password']
    endereco = request.json['endereco']
    data_nascimento = request.json['data_nascimento']

    user.nome = nome
    user.email = email
    user.password = password
    user.endereco = endereco
    user.data_nascimento = data_nascimento

    db.session.commit()

    return cliente_schema.jsonify(user)

# delete clientes by id endpoint
@blueprint.route("/<id>", methods=["DELETE"])
@jwt_required
def user_delete(id):
    user = Cliente.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return cliente_schema.jsonify(user)
