# -*- coding: utf-8 -*-
from loja.extensions.marshmallow import ma


class ClienteSchema(ma.Schema):

    class Meta:
        fields = ('id', 'nome', 'email', 'password', 'endereco', 'data_nascimento', 'dt_criacao')


# serialize one cliente
cliente_schema = ClienteSchema()

# serialize all clientes
clientes_schema = ClienteSchema(many=True)
