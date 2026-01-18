import json
from pathlib import Path

def load_json_schema(filename):
    schema_path = Path(__file__).parent.parent / "schemas" / filename
    with open(schema_path, "r") as file:
        return json.load(file)