"""Дан отсортированный массив различных целых чисел nums и целевое значение target. 
Если целевое значение найдено в массиве, верните его индекс. 
Если нет, верните индекс, куда это значение должно быть вставлено, чтобы массив остался отсортированным.

Ввод: nums = [1,3,5,6], target = 5
Вывод: 2

Ввод: nums = [1,3,5,6], target = 2
Вывод: 1

Ввод: nums = [1,3,5,6], target = 7
Вывод: 4"""


def find_element(lst, target):
    if target in lst:
        return lst.index(target)
    else:
        for i in range(len(lst)):
            if lst[i] == target - 1:
                return i+1
            
a = [1,3,5,6]
b = 5
print(find_element(a, b)) 

"""Дан непустой массив целых чисел nums, где каждый элемент встречается дважды,
 кроме одного. Найдите этот уникальный элемент.

Ввод: nums = [4,1,2,1,2]
Вывод: 4
Ввод: nums = [1]
Вывод: 1"""

def find_unique_element(nums: list) -> int:
    for i in nums:
        nums.remove(i)
        if i in nums:
            continue
        else:
            return i

nums = [1]
print(find_unique_element(nums))

"""**Задача 4.**

Преобразуйте положительное число в перевернутый массив цифр - 
вывести цифры числа в обратном порядке.
#35231 => [1,3,2,5,3]
#0 => [0]
#23582357 => [7,5,3,2,8,5,3,2]"""

def number_to_list(num: int)->list:
    return sorted([int(i) for i in str(num)])

num = 35231
print(number_to_list(num))

"""**Задача 5.**

Верните количество гласных в заданной строке. 
В задаче считаем "a", "e", "i", "o", "u" гласными, а "y" - нет. 
На вход подается строка только из строчных букв и/или пробелов.
#"aeiou" => 5#"y" => 0
#"bcdfghjklmnpqrstvwxz y" => 0
#"abracadabra" => 5"""
def vowels_find(str_input):
    vowels = ["a", "e", "i", "o", "u"]
    cnt = 0
    for i in str_input:
        if i in vowels:
            cnt += 1
    return cnt
str_input = "aeiou"
print(f' vovels_find {vowels_find(str_input)}')

"""**Задача 6.**

Напишите функцию, которая принимает список положительных целых 
чисел и строк и возвращает новый список, состоящий только из чисел.
#[1, 2, 'a', 'b'] => [1, 2]
#[1, 'a', 'b', 0, 15] => [1, 0, 15]
#[1, 2, 'a', 'b'] => [1, 2]"""

def only_numbers(list_input):
    return [i for i in list_input if isinstance(i, int)]

list_input = [1, 'a', 'b', 0, 15]
print(f'only_numbers {only_numbers(list_input)}')

"""Напишите функцию, которая будет возвращать список из n чисел, кратных x.

#(1, 5) => [1, 2, 3, 4, 5])
#(3, 5) => [3, 6, 9, 12, 15])
#(50, 5) => [50, 100, 150, 200, 250])"""

def find_list_from_x(tpl):
    x, n = tpl
    return [x*i for i in range(1,n+1)]

tpl = (3, 5)
print(f"find_list_from_x{find_list_from_x(tpl)}")

"""Дана строка s и целое число k, обозначающее количество позиций, 
на которые нужно "перевернуть" (сдвинуть) первый символ строки вправо. 
Напишите функцию, которая принимает строку s и число k, и возвращает строку после выполнения переворота.

Требования:
Функция должна корректно работать для любых значений k, включая случаи, когда k больше длины строки.
Гарантируется, что строка s не пустая.

Ввод 1: s = "AbeSimp" k = 1
Вывод 1: "pAbeSim"

Ввод 2: s = "AbeSimp" k = 3
Вывод 2: "mpAbeSi"

Ввод 3: s = "Hello" k = 7
Вывод: "oHell"""

def rotate_string(s, k):
    if k > len(s):
        return s[-1] + s[:-1]
    return s[-k] + s[:-k]

s = "AbeSimp"
k = 1
print(rotate_string(s, k))