# -*- coding: utf-8 -*-
import datetime
from typing import Union
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token, create_refresh_token

from loja.extensions.database import db
from loja.models import Cliente
from loja.serializers import cliente_schema, clientes_schema


blueprint = Blueprint("login", __name__, url_prefix="/v1/login")

# create login endpoint
@blueprint.route("/", methods=["POST"])
def login():
    email = request.json['email']
    password = request.json['password']

    all_users = Cliente.query.all()
    result = clientes_schema.dump(all_users)

    for item in result:
        if email == item['email'] and password == item['password']:
            ret = {
                'access_token': create_access_token(identity=email),
                'refresh_token': create_refresh_token(identity=email)
            }

        else:
            ret = {"Usuario nao encontrado"}    

    return jsonify(ret), 200
