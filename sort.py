def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
numbers = [35, 52, 99, 86, 12]
print("Исходный список чисел:", numbers)
sorted_numbers = selection_sort(numbers)
print("отсортированный массив: ", sorted_numbers)
