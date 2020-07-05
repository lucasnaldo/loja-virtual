# -*- coding: utf-8 -*-
from .cliente_schema import ClienteSchema, cliente_schema, clientes_schema
from .pedido_schema import PedidoSchema, pedido_schema, pedidos_schema
from .pedido_schema import ItensPedidoSchema, item_pedido_schema, itens_pedido_schema
from .produto_schema import ProdutoSchema, produto_schema, produtos_schema


__all__ = [
    "ClienteSchema",
    "cliente_schema",
    "clientes_schema",
    "PedidoSchema",
    "pedido_schema",
    "pedidos_schema",
    "ProdutoSchema",
    "produto_schema",
    "produtos_schema",
    "ItensPedidoSchema",
    "item_pedido_schema",
    "itens_pedido_schema"
]
