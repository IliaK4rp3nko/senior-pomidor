import pytest
import requests
from constant import BASE_URL, HEADERS
from faker import Faker

fake = Faker()

@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    auth_data = {
        "grant_type": "password",
        "username": "llKx2ll@gmail.com",
        "password": "password123",
        "scope": "",
        "client_id": "",
        "client_secret": ""
    }
    auth_response = session.post(f"{BASE_URL}/login/access-token", data = auth_data, headers=HEADERS)
    token = auth_response.json().get("access_token")
    session.headers.update({"authorization": f"Bearer {token}"})
    return session

    
@pytest.fixture()
def item_data():
    return {
  "title": fake.word(),
  "description": fake.text()
}
    
@pytest.fixture()
def item_data_updated():
    return{
  "title": "test_title",
  "description": "test_description" 
}

