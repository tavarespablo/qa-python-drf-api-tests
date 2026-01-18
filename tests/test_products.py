from jsonschema import validate
from data.test_data import load_json_schema
from data.endpoints import PRODUCTS
from client.api_client import APIClient
from config.settings import BASE_URL
from data.endpoints import PRODUCTS

def test_get_products_returns_success():
    client = APIClient(BASE_URL)
    response = client.get(PRODUCTS)

    assert response.status_code == 200
    assert response.json() != []

def test_get_products_schema():
    client = APIClient(BASE_URL)
    response = client.get(PRODUCTS)

    assert response.status_code == 200
    
    schema = load_json_schema("product_schema.json")
    products = response.json()

    # It validates the first item of the list
    validate(instance=products[0], schema=schema)