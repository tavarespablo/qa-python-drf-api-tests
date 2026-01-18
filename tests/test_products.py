from client.api_client import APIClient

BASE_URL = "https://fakestoreapi.com"

def test_get_products_returns_success():
    client = APIClient(BASE_URL)
    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() != []