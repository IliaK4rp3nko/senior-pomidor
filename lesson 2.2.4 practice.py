def temp_converter(f_temp: float) -> str:
    c_temp = (f_temp - 32)*5/9
    return f'{f_temp} по Фаренгейту равняется {c_temp} по Цельсию'

print(temp_converter(100))
