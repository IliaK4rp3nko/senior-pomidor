def calculator():
    def plus(x, y):
        return x + y

    def minus(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if x == 0 or y == 0:
            return "Ошибка: деление на ноль"
        return x / y 

    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    operation = input("Выберите операцию (+, -, *, /): ")

    if operation == "+":
        result = plus(a, b)
    elif operation == "-":
        result = minus(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        result = "Ошибка: неверная операция"

    print(f"Результат: {result}")

calculator()