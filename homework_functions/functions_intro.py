def greet_user(name):
    return f'Привет, {name}! Добро пожаловать в мир Python!'

def calculate_sum(a, b):
    summ = a + b
    return f'Сумма введенных чисел {summ}'

def greet_summ_func():
    name = input("Введите ваше имя: ")
    print(greet_user(name))
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print(calculate_sum(a, b))

greet_summ_func()


