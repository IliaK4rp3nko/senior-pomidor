def char_frequency(s):
    s_list = list(s)
    dictionary = {}
    for i in s_list:
        dictionary[i] = s_list.count(i)
    return dictionary

print(char_frequency("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def merge_dicts(dict1, dict2):
    dict3 = dict1.copy()
    for key, value in dict2.items():
        if key in dict3:
            dict3[key] += value
        else:
            dict3[key] = value
    return dict3

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))  # {"a": 1, "b": 5, "c": 4}

def dict_to_lists(my_dict):
    keys_list = []
    values_list =[]
    for key, value in my_dict.items():
        keys_list.append(key)
        values_list.append(value)
    return keys_list, values_list

my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, 3])

def group_by_first_letter(strings):
    result_dict = {}
    for string in strings:
        if string[0] not in result_dict.keys():
            result_dict[string[0]] = [word for word in strings if word[0]==string[0]]
    return result_dict

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
# {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}

def extract_subdict(my_dict, keys):
    new_dict = {}
    for key in keys:
        new_dict[key] = my_dict[key]
    return new_dict

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys))  # {"a": 1, "c": 3}

