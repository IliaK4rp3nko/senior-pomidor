from constant import BASE_URL, HEADERS

class TestItems:
    def test_create_item(self, item_data, auth_session):
        auth_session.headers.update({"Content-Type": "application/json", "accept": "application/json"})
        print(auth_session.headers, auth_session.url)
        response = auth_session.post(f"{BASE_URL}/api/v1/items", json=item_data)
        assert response.status_code == 201, f"Неверный статус код: {response.status_code}, тело ответа: {response.text}"
        item_id = response.json().get("id")
        assert item_id is not None, f"Не удалось получить ID созданного айтема. Ответ: {response.json()}"
    
    def test_get_items(self, auth_session):
        responce = auth_session.get(f"{BASE_URL}/api/v1/items")
        assert responce.status_code == 200, "Статус ответа  на гет айтем не 200"
        assert isinstance(responce.json(), list)
