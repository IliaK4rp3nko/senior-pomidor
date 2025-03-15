def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) == len(s2):
        for i in s1:
            if i in s2:
                anagram_true = True
            else:
                return False
        return True
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False

def is_palindrome(s):
    cleaned_s = [i.lower() for i in s if i.isalnum()]  # Оставляем только буквы и цифры, приводим к нижнему регистру
    return cleaned_s == cleaned_s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True

print(is_palindrome("racecar"))                        # True

print(is_palindrome("hello"))                        # False

def longest_word(s):
    s_list = s.split()
    longest_word = max(s_list, key = len)
    return longest_word

print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits")) # "extraordinary”

def format_phone_number(digits):
    return f'({digits[:3]}) {digits[3:6]}-{digits[7:10]}'

print(format_phone_number("1234567890")) # "(123) 456-7890”

def remove_duplicates(s):
    new_s = ""
    for i in s:
        if i not in new_s:
           new_s += i
    # Можно решить через new_s = "".join(sorted(set(s), key=s.index))
    return new_s

print(remove_duplicates("programming")) # "progamin”

def is_unique(s):
    unique_s = remove_duplicates(s)
    return s == unique_s

print(is_unique("abcdef")) # True
print(is_unique("hello"))  # False