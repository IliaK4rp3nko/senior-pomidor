def check_grade(score):
    if 90 <= score <= 100:
        return "Отлично"
    elif 75 <= score <= 89:
        return "Хорошо"
    elif 50 <= score <= 74:
        return "Удовлетворительно"
    else:
        return "Неудовлетворительно"
print(f"Оценка за {90} баллов: {check_grade(90)}")

def is_even(number):
    if number % 2 == 0:
        return "Четное"
    else:
        return "Нечетное"

print(is_even(4))
print(is_even(7))

def find_max(a, b):
    if a > b:
        return f'Максимальное из чисел {a} и {b}: {a}.'
    else:
        return f'Максимальное из чисел {a} и {b}: {b}.'

print(find_max(10, 20))

def check_number(number):
    if number > 0:
        if number % 2 == 0:
            return f"Число {number} положительное и чётное."
        else:
            return f"Число {number} положительное, но нечётное."
    elif number < 0:
        return f"Число {number} отрицательное."
    else:
        return "Число равно нулю."

print(check_number(8))
print(check_number(-5))
print(check_number(7))
print(check_number(0))

def check_string_length(string, length):
    return "Длина строки достаточная" if len(string) > length else "Строка слишком короткая"

print(check_string_length("Python", 5))
print(check_string_length("Hi", 5))