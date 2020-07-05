# -*- coding: utf-8 -*-
import datetime
from loja.extensions.database import db


class Pedido(db.Model):

    __tablename__ = 'Pedido'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cliente = db.Column(db.String(80), unique=False)
    valor_total = db.Column(db.String(80), unique=False)
    dt_criacao = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, id_cliente, valor_total):
        self.id_cliente = id_cliente
        self.valor_total = valor_total

class ItensPedido(db.Model):

    __tablename__ = 'ItensPedido'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_pedido = db.Column(db.Integer, unique=False)
    id_produto = db.Column(db.String(80), unique=False)
    quantidade = db.Column(db.Integer, unique=False)

    def __init__(self, id_pedido, id_produto, quantidade):
        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.quantidade = quantidade