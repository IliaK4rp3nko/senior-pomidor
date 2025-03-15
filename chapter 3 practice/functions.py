def rectangle_area(length, width):
    area = length * width
    return f"Площадь прямоугольника с длиной {length} и шириной {width} равна {area}."

print(rectangle_area(5, 3))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"В {seconds} секундах содержится {hours} час(ов) и {minutes} минут(ы)."

print(convert_seconds(3672))

def power_of(number, exponent=2):
    result =  number ** exponent
    return f"Число {number} в степени {exponent} равно {result}."

print(power_of(3, 2))
print(power_of(3))

def count_items(*args):
    res =  len(args)
    return f"Количество переданных элементов: {res}."

print(count_items(1, 2, 3, 4, 5))
print(count_items("apple", "banana", "cherry"))
