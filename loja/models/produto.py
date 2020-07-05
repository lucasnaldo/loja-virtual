# -*- coding: utf-8 -*-
import datetime
from loja.extensions.database import db


class Produto(db.Model):

    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), unique=False)
    preco = db.Column(db.Integer, unique=False)
    descricao = db.Column(db.String(120), unique=False)
    dt_criacao = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
