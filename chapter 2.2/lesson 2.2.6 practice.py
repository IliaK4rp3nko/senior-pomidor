CITY_LIST = ['Москва', 'Лондон', 'Париж'] = ['Москва', 'Лондон', 'Париж']

def list_append(element):
    numbers = [1,2,3]
    numbers.append(element)
    return numbers

def delete_element_from_list(CITY_LIST, element):
    try:
        CITY_LIST.remove(element)
    except ValueError:
        print(f"Элемент '{element}' отсутствует в списке")
    return CITY_LIST

print(delete_element_from_list(CITY_LIST, 'Лондон'))
print(delete_element_from_list(CITY_LIST, 'Донецк'))

def get_element_by_index(CITY_LIST, index):
    try:
        return CITY_LIST[index]
    except IndexError:
        print(f"Индекс {index} выходит за пределы списка.")
        return None  # Можно вернуть None или другое значение по умолчанию

print(get_element_by_index(CITY_LIST, 1))
print(get_element_by_index(CITY_LIST, 5))
