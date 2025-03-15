def sum_numbers(n):
    cnt = 0
    for i in range(n+1):
        cnt += i
    return f'Сумма чисел от 1 до {n}: {cnt}'

print(sum_numbers(5))

def find_min(numbers):
    min_num = numbers[0]
    for i in numbers:
        if i < min_num:
            min_num = i
    return f'Минимальное число в списке {numbers}: {min_num}'

print(find_min([3, 1, 4, 1, 5]))

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    cnt = 0
    for i in string:
        if i in vowels:
            cnt += 1
    return f'Количество гласных в строке "{string}": {cnt}'

print(count_vowels("Hello world"))

def print_diamond(rows):
    for i in range(rows):
        print(i * '*')
    for i in range(rows -2, -1, -1):
        print(i * '*')

print_diamond(5)