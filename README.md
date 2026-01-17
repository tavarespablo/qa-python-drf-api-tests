# QA Python DRF API Tests

This is an API test project in Python, inspired in the Django REST Framework organization and mentality.
The goal is to showcase professional QA practices, such as:
- Clean architecture
- Separation of responsibilities
- Escalable tests

---

## Stack

- Python 3.10+
- Pytest
- Requests
- GitHub Actions (CI)

---

## Project Structure
```
qa-python-drf-api-tests/
│
├─ tests/
│   ├─ __init__.py
│   ├─ test_products.py
│   ├─ test_orders.py
│
├─ client/
│   ├─ __init__.py
│   └─ api_client.py
│
├─ schemas/
│   ├─ product_schema.json
│   └─ order_schema.json
│
├─ data/
│   └─ test_data.py
│
├─ config/
│   └─ settings.py
│
├─ .github/
│   └─ workflows/
│       └─ api-tests.yml
│
├─ requirements.txt
├─ README.md
└─ .gitignore
```
## Setting Up

### 1. Create new Virtual Environment
python -m venv venv

### 2. Activate Environment
- Windows:
```
.venv\Scripts\Activate
```
### 3. Install dependencies
pip install -r requirements.txt

### 4. Execute tests
pytest

## CI/CD
The pipeline runs automatically in pull requests to the `main` branch, running:
- Dependencies installation
- pytest execution

File: `.github/workflows/api-tests.yml`

---

## Status
This README is being expanded along with the project's evolution.
