from http import HTTPStatus
from fastapi.testclient import TestClient

from fast_zero.app import app

def test_root_deve_retornar_uma_msg_e_um_ok():
    client = TestClient(app)
    
    response = client.get("/")
    
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Rodando no fastapi"}


def test_criar_usuario():
    client = TestClient(app)
    
    response = client.post("/users/", json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret'
        })
    
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1
    }