from constants import BASE_URL


class TestBookings:
    # POST ручка на создание брони
    def test_create_booking(self, booking_data, auth_session):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

    # GET ручка обшая (список бронирований)
    def test_get_booking_ids(self, auth_session):
        responce = auth_session.get(f"{BASE_URL}/booking/")
        assert responce.status_code == 200, "Статус ответа на запрос списка бронирований не 200"
        bookings = responce.json()

        assert isinstance(bookings, list), "Ответ запроса на список бронирований не является списком"
        assert len(bookings) > 0, "Список бронирований пуст"
        assert any("bookingid" in i for i in bookings)

    # GET ручка с квери параметрами
    def test_get_bookings_whith_query(self, booking_data, auth_session):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200

        responce = auth_session.get(f"{BASE_URL}/booking?"
                                    f"firstname={booking_data['firstname']}"
                                    f"&lastname={booking_data['lastname']}"
                                    f"&checkin={booking_data['bookingdates']['checkin']}"
                                    f"&checkout={booking_data['bookingdates']['checkout']}")
        assert responce.status_code == 200, "Статус ответа на запрос списка бронирований с сортировкой не 200"
        bookings = responce.json().get("bookingid")
        assert len(bookings) > 0, "Список бронирований с сортировкой по имени пуст"
        
        assert bookings["firstname"] == booking_data["firstname"], "Ошибка: найдено бронирование с другим именем"
        assert bookings["lastname"] == booking_data["lastname"], "Ошибка: найдено бронирование с другой фамилией"
        assert bookings["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"], "Ошибка: check-in не совпадает"
        assert bookings["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"], "Ошибка: check-out не совпадает"

        responce_fail = auth_session.get(f"{BASE_URL}/booking?firstname='test_user'")
        assert responce_fail.status_code == 404, "Код ответа на несуществующий firstname не 404"

    # PATCH ручка
    def test_patch_booking(self, booking_data, auth_session):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании бронирования"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id, "ID бронирования не найден"

        updated_data = {"firstname": "UpdatedName", "lastname": "UpdatedLastName"}
        patch_response = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=updated_data)
        assert patch_response.status_code == 200, "Ошибка при обновлении бронирования"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Ошибка при получении обновленного бронирования"
        booking_data_response = get_booking.json()
        assert booking_data_response["firstname"] == updated_data["firstname"], "Имя не обновилось"
        assert booking_data_response["lastname"] == updated_data["lastname"], "Фамилия не обновилась"
        
        #Удаляем озданные данные и проверяем, что удаление произошло верно, в базе нет созданных данных. Вопрос к Сергею, так это делается?
        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, "Ошибка при удалении бронирования"
 
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Бронирование не было удалено"
    
    #PUT ручка на изменение брони
    def test_update_booking(self, booking_data, updated_booking_data, auth_session):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании бронирования"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id, "ID бронирования не найден"

        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=updated_booking_data)
        assert update_booking.status_code == 200, "Ошибка при обновлении данных бронирования"
        
        get_updated_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_updated_booking.status_code == 200, "Ошибка при получении обновленного бронирования"
        updated_response = get_updated_booking.json()

        assert updated_response["firstname"] == updated_booking_data["firstname"], "Имя не обновилось"
        assert updated_response["lastname"] == updated_booking_data["lastname"], "Фамилия не обновилась"
        assert updated_response["totalprice"] == updated_booking_data["totalprice"], "Цена не обновилась"
        assert updated_response["depositpaid"] == updated_booking_data["depositpaid"], "Статус депозита не обновился"
        assert updated_response["bookingdates"]["checkin"] == updated_booking_data["bookingdates"]["checkin"], "Дата заезда не обновилась"
        assert updated_response["bookingdates"]["checkout"] == updated_booking_data["bookingdates"]["checkout"], "Дата выезда не обновилась"

        # Удаление бронирования (чтобы не засорять сервер тестовыми данными, надеюсь, это правильно)
        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, "Ошибка при удалении бронирования"




