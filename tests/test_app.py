
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Welcome to CI/CD DevOps Pipeline" in response.data


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "success"


def test_about_endpoint(client):
    response = client.get("/about")

    assert response.status_code == 200
    assert response.json["version"] == "1.0.0"


def test_invalid_route(client):
    response = client.get("/invalid")

    assert response.status_code == 404


def test_order_calculation(client):
    response = client.post(
        "/api/orders/preview",
        json={
            "product": "Keyboard",
            "quantity": 2,
            "unit_price_paise": 150000
        }
    )

    assert response.status_code == 200
    assert response.json["order_summary"]["total_paise"] == 300000


def test_zero_quantity_rejected(client):
    response = client.post(
        "/api/orders/preview",
        json={
            "product": "Keyboard",
            "quantity": 0,
            "unit_price_paise": 150000
        }
    )

    assert response.status_code == 400


def test_negative_price_rejected(client):
    response = client.post(
        "/api/orders/preview",
        json={
            "product": "Keyboard",
            "quantity": 2,
            "unit_price_paise": -100
        }
    )

    assert response.status_code == 400


def test_empty_product_rejected(client):
    response = client.post(
        "/api/orders/preview",
        json={
            "product": "",
            "quantity": 2,
            "unit_price_paise": 150000
        }
    )

    assert response.status_code == 400


def test_invalid_json_rejected(client):
    response = client.post(
        "/api/orders/preview",
        data="invalid json",
        content_type="application/json"
    )

    assert response.status_code == 400
