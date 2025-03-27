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