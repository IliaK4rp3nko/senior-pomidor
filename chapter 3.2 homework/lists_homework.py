def remove_duplicates(lst):
    no_duplicate_set = set(lst)
    return list(no_duplicate_set)

print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]

def generate_squares(n):
    lst = [x**2 for x in range(1, n+1)]
    return lst

print(generate_squares(5))  # [1, 4, 9, 16, 25]

def merge_lists(list1, list2):
    merged = list1 + list2
    unique_list = list(set(merged))
    return unique_list

print(merge_lists([1, 2, 3], [3, 4, 5]))  # [1, 2, 3, 4, 5]

def is_sorted(lst):
    sorted_list = sorted(lst)
    return sorted_list == lst

print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False

def merge_lists(list1, list2):
    len_list = len(list1)
    new_list = []
    for i in range(len_list):
        new_list.append(list1[i] + list2[i])
    return new_list

print(merge_lists([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]

