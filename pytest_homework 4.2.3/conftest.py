import pytest
import requests
from constant import BASE_URL, HEADERS
from faker import Faker

fake = Faker()

@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(HEADERS)
    auth_data = {
        "grant_type": "password",
        "username": "llKx2ll@gmail.com",
        "password": "password123",
        "scope": "",
        "client_id": "",
        "client_secret": ""
    }
    auth_response = session.post(f"{BASE_URL}/api/v1/login/access-token", data=auth_data)
    assert auth_response.status_code == 200, f"Ошибка при получении токена: {auth_response.text}"
    token = auth_response.json().get("access_token")
    assert token is not None, "Токен не получен"
    session.headers.update({"Authorization": f"Bearer {token}"})
    print(f'Токен авторизации {token}')
    return session

    
@pytest.fixture()
def item_data():
    return {
  "title": fake.random_int(min=100, max=10000),
  "description": fake.random_int(min=100, max=10000),
}

