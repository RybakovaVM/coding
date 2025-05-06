def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
numbers = [35, 52, 99, 86, 12]
print("Исходный список чисел:", numbers)
sorted_numbers = buble_sort(numbers)
print("отсортированный массив: ", sorted_numbers)
