def bubble_sort(numbers: list) -> list:
    n = len(numbers)
    for i in range(n):
        done = False
        for a in range(n - 1 - i):
            if numbers[a] > numbers[a + 1]:
                numbers[a], numbers[a + 1] = numbers[a + 1], numbers[a]
                done = True
        if not done:
            break
    return numbers

print(bubble_sort([3, 5, 9, 7, 2, 1, 4, 6, 8]))