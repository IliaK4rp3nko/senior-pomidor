def grams_to_kilo_converter(grams: int) -> str:
    kilos = round(grams/1000)
    return f'В {grams} грамм содержится {kilos} полных килограмм'

print(grams_to_kilo_converter(12345))

def last_digit(digit: int) -> str:
    lst_dgt = str(digit)[-1]
    return f' Последняя цифра числа {digit}: {lst_dgt}'

print (last_digit(12345))

def even_number(digit: int) -> str:
    if digit > 0 and digit % 2 == 0:
        return f'Число {digit} является положительным и четным'
    else:
        return f'Число {digit} не подходит под условия'

print(even_number(4))
print(even_number(7))

def digit_in_range(digit: int) -> str:
    if digit >= 0 and digit <= 100:
        return f'Число {digit} находится в диапазоне от 0 до 100'
    else:
        return f'Число {digit}  не входит в диапазон от 0 до 100'

print(digit_in_range(150))
print(digit_in_range(100))

def multiple_digit(digit: int) -> str:
    if digit % 3 == 0:
        return f'Число {digit} кратно 3'
    else:
        return f'Число {digit} не кратно 3'

print(multiple_digit(9))
print(multiple_digit(10))