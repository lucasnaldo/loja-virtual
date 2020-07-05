# -*- coding: utf-8 -*-
from loja.extensions.marshmallow import ma


class PedidoSchema(ma.Schema):

    class Meta:
        fields = ('id_cliente', 'valor_total', 'dt_criacao')

# serialize one pedido
pedido_schema = PedidoSchema()

# serialize all pedidos
pedidos_schema = PedidoSchema(many=True)


class ItensPedidoSchema(ma.Schema):

    class Meta:
        fields = ('id_pedido', 'id_produto', 'dt_criacao')

# serialize one item pedido
item_pedido_schema = ItensPedidoSchema()

# serialize all itens pedido
itens_pedido_schema = ItensPedidoSchema(many=True)
