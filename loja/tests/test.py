import os
import tempfile
import copy
import pytest
# import requests

from loja.app import create_app
from loja.models import Cliente, Pedido, Produto
from loja.serializers import ClienteSchema, PedidoSchema, ProdutoSchema


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_clientes_request_vazio(client):   
    rv = client.post('/loja/v1/clientes', data={})
    assert rv.json['message'] == 'Nenhum dado recebido no request'

def test_clientes_request_vazio(client):   
    rv = client.post('/loja/v1/produtos', data={})
    assert rv.json['message'] == 'Nenhum dado recebido no request'

def test_clientes_request_vazio(client):   
    rv = client.post('/loja/v1/pedidos', data={})
    assert rv.json['message'] == 'Nenhum dado recebido no request'