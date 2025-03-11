def check_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b and b == c:
            print("Результат: Треугольник равносторонний.")
        elif a == b or b == c or a == c:
            print("Результат: Треугольник равнобедренный.")
        else:
            print("Результат: Треугольник разносторонний.")
    else:
        print("Результат: Треугольник нельзя построить с данными параметрами сторон.")

def triangle_calc():
    a = int(input("Введите длину первой стороны: "))
    b = int(input("Введите длину второй стороны: "))
    c = int(input("Введите длину третьей стороны: "))
    check_triangle(a, b, c)

triangle_calc()