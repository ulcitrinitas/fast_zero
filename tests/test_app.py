from http import HTTPStatus

def test_root_deve_retornar_uma_msg_e_um_ok(client):
    
    response = client.get("/")
    
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Rodando no fastapi"}


def test_criar_usuario(client):
    
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