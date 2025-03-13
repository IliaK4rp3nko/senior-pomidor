def get_unique_elements(lst):
    no_duplicate_set = set(lst)
    return list(no_duplicate_set)

print(get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))  # [1, 2, 3, 4, 5]

def is_unique_list(lst):
    unique = set(lst)
    return lst == list(unique)

print(is_unique_list([1, 2, 3, 4]))  # True
print(is_unique_list([1, 2, 2, 3]))  # False

def get_unique_vowels(s):
    vowels = ['a', 'e','i', 'o', 'u']
    result_set = set()
    for letter in vowels:
        if letter in s.lower():
            result_set.add(letter)
    return result_set

print(get_unique_vowels("Hello World"))  # {'e', 'o'}
