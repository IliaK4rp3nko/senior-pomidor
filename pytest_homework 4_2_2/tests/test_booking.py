from constants import BASE_URL


class TestBookings:
    # POST: создание бронирования
    def test_create_booking(self, booking_data, auth_session):
        create_booking = auth_session.post(
            f"{BASE_URL}/booking", json=booking_data
        )
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == booking_data[
            'firstname'
        ], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == booking_data[
            'lastname'
        ], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == booking_data[
            'totalprice'
        ], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == booking_data[
            'depositpaid'
        ], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == (
            booking_data['bookingdates']['checkin']
        ), "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == (
            booking_data['bookingdates']['checkout']
        ), "Дата выезда не совпадает"
        
        delete_booking = auth_session.delete(
            f"{BASE_URL}/booking/{booking_id}"
        )
        assert delete_booking.status_code == 201, (
            f"Ошибка при удалении букинга с ID {booking_id}")
        
        get_deleted_booking = auth_session.get(
            f"{BASE_URL}/booking/{booking_id}"
        )
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

    # GET: список бронирований
    def test_get_booking_ids(self, auth_session):
        response = auth_session.get(f"{BASE_URL}/booking/")
        assert response.status_code == 200, (
            "Статус ответа на запрос списка бронирований не 200"
        )
        bookings = response.json()
        
        assert isinstance(bookings, list), (
            "Ответ запроса не является списком"
        )
        assert len(bookings) > 0, "Список бронирований пуст"
        assert any("bookingid" in i for i in bookings)
    
    # GET: бронирование по параметрам
    def test_get_bookings_sorted_by_name(self, booking_data, auth_session):
        create_booking = auth_session.post(
            f"{BASE_URL}/booking", json=booking_data
        )
        assert create_booking.status_code == 200
        
        get_booking_wiwh_sorted_by_name = auth_session.get(
            f"{BASE_URL}/booking?firstname={booking_data['firstname']}&"
            f"lastname={booking_data['lastname']}"
        )
        assert get_booking_wiwh_sorted_by_name.status_code == 200, "Статус ответа не 200"
        bookings = get_booking_wiwh_sorted_by_name.json()
        assert isinstance(bookings, list), "В ответе ожидаем список со словарями"
        assert len(bookings) > 0, "Список бронирований пуст"
        
    def test_get_bookings_sorted_by_date(self, booking_data, auth_session):
        get_booking_sorted_by_date = auth_session.get(
        f"{BASE_URL}/booking?checkin={booking_data['bookingdates']['checkin']}&"
        f"checkout={booking_data['bookingdates']['checkout']}")
        assert get_booking_sorted_by_date.status_code == 200, "Статус ответа не 200"
        bookings = get_booking_sorted_by_date.json()
        assert isinstance(bookings, list), "В ответе ожидаем список со словарями"
        assert len(bookings) > 0, "Список бронирований пуст"

        response_fail = auth_session.get(
            f"{BASE_URL}/booking?firstname='test_user'"
        )
        assert response_fail.status_code == 200, "Код ответа не 200"
        assert len(response_fail.json()) == 0
    
    # PATCH: обновление бронирования
    def test_patch_booking(self, booking_data, auth_session):
        create_booking = auth_session.post(
            f"{BASE_URL}/booking", json=booking_data
        )
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        
        updated_data = {
            "firstname": "UpdatedName",
            "lastname": "UpdatedLastName"
        }
        patch_response = auth_session.patch(
            f"{BASE_URL}/booking/{booking_id}", json=updated_data
        )
        assert patch_response.status_code == 200
        
        get_booking = auth_session.get(
            f"{BASE_URL}/booking/{booking_id}"
        )
        assert get_booking.status_code == 200
        booking_data_response = get_booking.json()
        assert booking_data_response["firstname"] == updated_data[
            "firstname"], "Имя не обновилось"
        assert booking_data_response["lastname"] == updated_data[
            "lastname"], "Фамилия не обновилась"
        
        delete_booking = auth_session.delete(
            f"{BASE_URL}/booking/{booking_id}"
        )
        assert delete_booking.status_code == 201
        
        get_deleted_booking = auth_session.get(
            f"{BASE_URL}/booking/{booking_id}"
        )
        assert get_deleted_booking.status_code == 404
