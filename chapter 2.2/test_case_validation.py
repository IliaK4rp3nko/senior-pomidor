def test_case_validated_stats():
    def validation():
        while True:
            try:
                numder = int(input("Введите количество тесткейсов сделанных за день: "))
                if numder >= 0:
                    return numder
                else:
                    print("Количество тест-кейсов не может быть отрицательным.")
            except ValueError:
                print("Некорректный ввод. Введите число.")

    monday = validation()
    tuesday = validation()
    wednesday = validation()
    thursday = validation()
    friday = validation()

    cnt = monday + tuesday + wednesday + thursday + friday
    avg = cnt / 5

    if avg >= 10:
        print("Отличная работа за неделю!")
    else:
        print("Работать нужно больше, солнце еще высоко и неделя имеет выходные дни.")

# Запуск функции
test_case_validated_stats()