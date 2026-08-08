import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_hello_body(client):
    response = client.get("/")
    data = response.get_json()
    assert data["message"] == "Hello World!"
    assert data["status"] == "ok"
    assert data["version"] == "1.0.0"


def test_health_status_code(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_body(client):
    response = client.get("/health")
    data = response.get_json()
    assert data["status"] == "healthy"


def test_ruta_inexistente_da_404(client):
    response = client.get("/no-existe")
    assert response.status_code == 404
