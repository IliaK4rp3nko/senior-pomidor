def number_sum():
    n = int(input("Введите число: "))
    n_numbers_list = [i for i in range(1,n+1)]
    print("Числа: ", *n_numbers_list)
    print("Сумма чисел: ", sum(n_numbers_list))

number_sum()