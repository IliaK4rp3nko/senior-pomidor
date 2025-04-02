import requests
from constant import BASE_URL, API_HEADERS


class TestAuth:
    def test_valid_token(self, auth_session):
        response = auth_session.post(
        f"{BASE_URL}/login/test-token",
        headers=API_HEADERS
    )
        assert response.status_code == 200, (
        f"Ожидался статус 200, получен {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
        json_data = response.json()
    
        assert "email" in json_data, "Ответ не содержит email"
        assert "is_active" in json_data, "Ответ не содержит is_active"
        assert "full_name" in json_data, "Ответ не содержит full_name"
        assert "id" in json_data, "Ответ не содержит id"
        
        assert isinstance(json_data["email"], str), (
            "email должен быть строкой"
            )
        assert isinstance(json_data["is_active"], bool), (
            "is_active должен быть bool"
            )
        assert isinstance(json_data["full_name"], str), (
            "full_name должен быть строкой"
            )
        assert isinstance(json_data["id"], str), "id должен быть строкой"

    def test_invalid_token(self, auth_session):
        auth_session.headers.update = {
            "authorization": "qwertyuiojhfdw234567890-098rewazxcvbnkloiuyq2345678"
        }
        response = requests.post(
            f"{BASE_URL}/login/test-token"
        )
        assert response.status_code == 401, (
            f"Ожидался статус 401, получен {response.status_code}. "
            f"Тело ответа: {response.text}"
        )
        assert "detail" in response.json(), (
            "Ответ не содержит описание ошибки"
        )

    def test_no_token(self):
        headers = {"accept": "application/json"}
        response = requests.post(
            f"{BASE_URL}/login/test-token",
            headers=headers
        )
        assert response.status_code == 401, (
            f"Ожидался статус 401, получен {response.status_code}. "
            f"Тело ответа: {response.text}"
        )
        assert "detail" in response.json(), (
            "Ответ не содержит описание ошибки"
        )