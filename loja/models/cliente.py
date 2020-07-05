# -*- coding: utf-8 -*-
import datetime
from loja.extensions.database import db


class Cliente(db.Model):

    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    endereco = db.Column(db.String(120), unique=False, nullable=True)
    data_nascimento = db.Column(db.String(120), unique=False, nullable=True)
    dt_criacao = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, nome, email, password, endereco, data_nascimento):
        self.nome = nome
        self.email = email
        self.password = password
        self.endereco = endereco
        self.data_nascimento = data_nascimento
