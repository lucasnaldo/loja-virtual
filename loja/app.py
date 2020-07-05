# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_jwt_extended import jwt_required, JWTManager

from loja.extensions import database, marshmallow
from loja.extensions.cors import cors
from loja.views import clientes, pedidos, produtos, login


def create_app():
    app = Flask(__name__)

    app.secret_key = 'admin'
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']

    jwt = JWTManager(app)

    register_blueprints(app)
    register_extensions(app)

    return app


def register_extensions(app):
    database.init_app(app, criar_tabelas=True)
    marshmallow.init_app(app)


def register_blueprints(app):
    origins = app.config.get("CORS_ORIGIN_WHITELIST", "*")
    cors.init_app(app, origins=origins)

    cors.init_app(clientes.blueprint, origins=origins)
    cors.init_app(pedidos.blueprint, origins=origins)
    cors.init_app(produtos.blueprint, origins=origins)
    cors.init_app(login.blueprint, origins=origins)

    app.register_blueprint(clientes.blueprint)
    app.register_blueprint(pedidos.blueprint)
    app.register_blueprint(produtos.blueprint)
    app.register_blueprint(login.blueprint)


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)

