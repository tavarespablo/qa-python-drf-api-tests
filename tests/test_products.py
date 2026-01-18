from client.api_client import APIClient
from config.settings import BASE_URL
from data.endpoints import PRODUCTS

def test_get_products_returns_success():
    client = APIClient(BASE_URL)
    response = client.get(PRODUCTS)

    assert response.status_code == 200
    assert response.json() != []