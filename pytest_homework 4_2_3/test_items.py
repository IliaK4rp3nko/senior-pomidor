from constant import BASE_URL, API_HEADERS
import requests


class TestItems:
    # POST /items — создание нового элемента.
    def test_create_item(self, item_data, auth_session):
        response = auth_session.post(
            f"{BASE_URL}/items/", json=item_data, headers=API_HEADERS
            )
        assert response.status_code == 200, (
            f"Неверный статус код: {response.status_code}, "
            f"тело ответа: {response.text}"
        )
        item_id = response.json().get("id")
        assert item_id is not None, (
            f"Не удалось получить ID созданного айтема. "
            f"Ответ: {response.json()}"
        )
        responce_items = response.json()
        assert "title" in responce_items
        assert "description" in responce_items
        assert "id" in responce_items
        assert "owner_id" in responce_items

    def test_create_item_no_auth(self, item_data):
        response = requests.post(
            f"{BASE_URL}/items/",
            json=item_data, 
            headers=API_HEADERS
            )
        assert response.status_code == 401, (
            f"Ожидали 401, получили {response.status_code}, "
            f"тело ответа: {response.text}"
        )

    def test_create_item_empty_json(self, auth_session, ):
        response = auth_session.post(
            f"{BASE_URL}/items/",
            json={},
            headers=API_HEADERS
            )
        assert response.status_code == 422, (
            f"Ожидали 422, получили {response.status_code}, "
            f"тело ответа: {response.text}"
        )

    # GET /api/v1/items/ 
    def test_get_items(self, auth_session):
        response = auth_session.get(
            f"{BASE_URL}/items/?skip=0&limit=100", headers=API_HEADERS
            )
        assert response.status_code == 200, (
            f"Статус код а получение списка айтемов "
            f"ожидался 200 а получен {response.status_code}"
        )
        response_data = response.json()
        assert "data" in response_data, "В ответе нет ключа data"
        assert "count" in response_data, "В ответе нет ключа count"
        assert isinstance(response_data["data"], list), (
            "Ключ data не является списком")
        assert len(response_data["data"]) != 0, "Список айтемов пуст"
        assert isinstance(response_data["count"], int)
        assert len(response_data["data"]) == response_data["count"], (
            "Не правильный подсчет каунтера")
        assert "title" in response_data["data"][0]
        assert "description" in response_data["data"][0]
        assert "id" in response_data["data"][0]
        assert "owner_id" in response_data["data"][0]
    
    def get_items_without_auth(self):
        response = requests.get(
            f"{BASE_URL}/items/?skip=0&limit=100", headers=API_HEADERS
        )
        assert response.status_code == 401, (
            f"Статус код а получение списка айтемов ,tбез торизации"
            f"ожидался 401 а получен {response.status_code}"
        )

    # PUT /items/{id} — полное обновление элемента.
    # Позитивный кейс
    def test_update_item(self, item_data, auth_session, item_data_updated):
        post_response = auth_session.post(
            f"{BASE_URL}/items/", json=item_data, headers=API_HEADERS
        )
        assert post_response.status_code == 200, (
            f"Неверный статус код при создании: "
            f"{post_response.status_code}, тело ответа: {post_response.text}"
        )
        item_id = post_response.json().get("id")
        owner_id = post_response.json().get("owner_id")

        put_response = auth_session.put(
            f"{BASE_URL}/items/{item_id}", json=item_data_updated
        )
        assert put_response.status_code == 200, (
            f"Неверный статус код при обновлении: "
            f"{put_response.status_code}, тело ответа: {put_response.text}"
        )
        json_data = put_response.json()
        assert json_data["title"] == item_data_updated["title"], (
            f"Заголовок не обновился. "
            f"Ожидалось: {item_data_updated['title']}, "
            f"получено: {json_data['title']}"
        )
        assert json_data["description"] == item_data_updated["description"], (
            f"Описание не обновилось. "
            f"Ожидалось: {item_data_updated['description']}, "
            f"получено: {json_data['description']}"
        )
        assert json_data["id"] == item_id, (
            f"ID элемента не совпадает. "
            f"Ожидалось: {item_id}, получено: {json_data['id']}"
        )
        assert json_data["owner_id"] == owner_id, (
            f"ID владельца не совпадает. "
            f"Ожидалось: {owner_id}, получено: {json_data['owner_id']}"
        )

    # Негативные кейсы
    def test_update_nonexistent_item(self, auth_session, item_data_updated):
        non_existent_id = 99999
        put_response = auth_session.put(
            f"{BASE_URL}/items/{non_existent_id}", json=item_data_updated
        )
        assert put_response.status_code == 422, (
            f"Неверный статус код. Ожидался 422, "
            f"получен {put_response.status_code}. "
            f"Тело ответа: {put_response.text}"
        )
        assert 'detail' in put_response.json(), (
            "Ответ не содержит сообщение об ошибке"
        )

    def test_update_item_without_auth(self, auth_session,
                                      item_data, item_data_updated):
        post_response = auth_session.post(
            f"{BASE_URL}/items/", json=item_data
        )
        item_id = post_response.json().get("id")

        put_response = requests.put(
            f"{BASE_URL}/items/{item_id}", json=item_data_updated
        )
        assert put_response.status_code == 401, (
            f"Неверный статус код. "
            f"Ожидался 401, получен {put_response.status_code}. "
            f"Тело ответа: {put_response.text}"
        )

    def test_update_item_with_invalid_data(self, auth_session, item_data):
        post_response = auth_session.post(
            f"{BASE_URL}/items/", json=item_data
        )
        item_id = post_response.json().get("id")

        invalid_data = {
            "title": "",  # Некорректный заголовок
            "description": "Valid description"
        }
        put_response = auth_session.put(
            f"{BASE_URL}/items/{item_id}", json=invalid_data
        )
        assert put_response.status_code == 422, (
            f"Неверный статус код. Ожидался 422, "
            f"получен {put_response.status_code}. "
            f"Тело ответа: {put_response.text}"
        )
        assert "detail" in put_response.json(), (
            "Ответ не содержит сообщение об ошибке"
        )

    # DELETE /items/{id} — удаление элемента.
    # Позитивный кейс
    def test_delete_item(self, auth_session, item_data):
        post_response = auth_session.post(
            f"{BASE_URL}/items/", json=item_data, headers=API_HEADERS
            )
        assert post_response.status_code == 200, (
            f"Неверный статус код: {post_response.status_code}, "
            f"тело ответа: {post_response.text}")
        item_id = post_response.json().get("id")
        
        delete_response = auth_session.delete(f"{BASE_URL}/items/{item_id}")
        assert delete_response.status_code == 200, (
            f"Неверный статус код при удалении: "
            f"{delete_response.status_code}, тело ответа: {delete_response.text}"
        )
        
        get_response = auth_session.get(f"{BASE_URL}/items/{item_id}")
        assert get_response.status_code == 404, "Удалённый элемент всё ещё доступен."
    
    # Негативные кейсы
    def test_delete_nonexistent_item(self, auth_session):
        non_existent_id = 99999
        delete_response = auth_session.delete(f"{BASE_URL}/items/{non_existent_id}")
        assert delete_response.status_code == 422, (
            f"Неверный статус код. Ожидался 422, "
            f"получен {delete_response.status_code}. "
            f"Тело ответа: {delete_response.text}"
        )
        
    def test_delete_item_without_auth(self, auth_session, item_data):
        post_response = auth_session.post(
            f"{BASE_URL}/items/", json=item_data
        )
        item_id = post_response.json().get("id")
        
        delete_response = requests.delete(f"{BASE_URL}/items/{item_id}")
        assert delete_response.status_code == 401, (
            f"Неверный статус код. "
            f"Ожидался 401, получен {delete_response.status_code}. "
            f"Тело ответа: {delete_response.text}"
        )
