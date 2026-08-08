import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_hello_status_code(client):
    response = client.get("/")

    assert response.status_code == 200


def test_hello_message(client):
    response = client.get("/")

    assert response.json["message"] == "Hello World!"


def test_hello_status(client):
    response = client.get("/")

    assert response.json["status"] == "ok"


def test_hello_version(client):
    response = client.get("/")

    assert response.json["version"] == "1.0.0"


def test_health_status_code(client):
    response = client.get("/health")

    assert response.status_code == 200


def test_health(client):
    response = client.get("/health")

    assert response.json["status"] == "healthy"
