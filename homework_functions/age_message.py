def age_message():
    today_year = 2025
    user_year = int(input("Введите год вашего рождения: "))
    user_age = today_year - user_year
    if user_age < 18:
        message = "Вы еще молоды, учеба — ваш путь!"
    elif user_age >= 18 and user_age <= 65:
        message = "Отличный возраст для карьерного роста!"
    else:
        message = "Пора наслаждаться заслуженным отдыхом!"
    print("Ваш возраст: ", user_age)
    print(message)

age_message()