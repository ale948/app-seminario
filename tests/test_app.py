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