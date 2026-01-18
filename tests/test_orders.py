from jsonschema import validate
from client.api_client import APIClient
from config.settings import BASE_URL
from data.endpoints import ORDERS
from data.test_data import load_json_schema

def test_get_orders_schema():
    client = APIClient(BASE_URL)
    response = client.get(ORDERS)

    assert response.status_code == 200

    schema = load_json_schema("order_schema.json")
    orders = response.json()

    validate(instance=orders[0], schema=schema)