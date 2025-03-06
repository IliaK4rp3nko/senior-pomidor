def test_case_stats():
    monday = int(input("Введи общее количество кейсов сделанных за понедельник: "))

    tuesday = int(input("Введи общее количество кейсов сделанных за вторник: "))
    wednesday = int(input("Введи общее количество кейсов сделанных за среду: "))
    thursday = int(input("Введи общее количество кейсов сделанных за четверг: "))
    friday = int(input("Введи общее количество кейсов сделанных за пятницу: "))

    cnt = monday + tuesday + wednesday +thursday + friday
    avg = cnt / 5

    if avg >= 10:
        print ("Отличная работа!")
    else:
        print ("Попробуйте улучшить результат.")

test_case_stats()