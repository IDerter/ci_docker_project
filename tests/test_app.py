import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, Docker CI/CD!'

def test_not_found(client):
    response = client.get('/non-existent-page')
    assert response.status_code == 404

def test_content_type(client):
    response = client.get('/')
    # Проверяем, что сервер возвращает текст в кодировке UTF-8
    assert 'text/html' in response.content_type

def test_post_method_not_allowed(client):
    response = client.post('/')
    # Маршрут '/' по умолчанию принимает только GET
    assert response.status_code == 405

def test_headers(client):
    response = client.get('/')
    # Проверяем, что в ответе есть стандартные заголовки (например, Content-Length)
    assert 'Content-Length' in response.headers
    assert int(response.headers['Content-Length']) > 0

def test_root_with_query_params(client):
    response = client.get('/?param=test')
    assert response.status_code == 200
    assert b'Hello, Docker CI/CD!' in response.data