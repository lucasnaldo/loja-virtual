# -*- coding: utf-8 -*-
from loja.extensions.marshmallow import ma


class ProdutoSchema(ma.Schema):

    class Meta:
        fields = ('nome', 'preco', 'descricao', 'dt_criacao')

# serialize one produto
produto_schema = ProdutoSchema()

# serialize all produtos
produtos_schema = ProdutoSchema(many=True)
