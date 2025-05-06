import random
import time

# 1. Генерация списка из 10000 случайных чисел
my_list = [random.randint(0, 100000) for _ in range(10000)]
print(f"Сгенерирован список из {len(my_list)} элементов")

# 2. Функции сортировки
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    for i in range(left+1, right+1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key_item
    return arr

def merge(arr, left, mid, right):
    len_left = mid - left + 1
    len_right = right - mid
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    i = j = 0
    k = left
    while i < len_left and j < len_right:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len_left:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len_right:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def tim_sort(arr):
    min_run = 32
    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i+min_run-1), n-1))
    size = min_run
    while size < n:
        for left in range(0, n, 2*size):
            mid = left + size - 1
            right = min((left + 2*size - 1), (n-1))
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2
    return arr

# 3. Тестирование всех алгоритмов на одном списке
test_list = my_list.copy()

# Selection Sort
start_time = time.time()
selection_sorted = selection_sort(test_list.copy())
selection_time = time.time() - start_time

# Bubble Sort
start_time = time.time()
bubble_sorted = bubble_sort(test_list.copy())
bubble_time = time.time() - start_time

# TimSort
start_time = time.time()
tim_sorted = tim_sort(test_list.copy())
tim_time = time.time() - start_time

# 4. Вывод результатов
print("\nВремя выполнения сортировок:")
print(f"Selection Sort: {selection_time:.5f} секунд")
print(f"Bubble Sort:    {bubble_time:.5f} секунд")
print(f"TimSort:        {tim_time:.5f} секунд")

# 5. Проверка что все сортировки дают одинаковый результат
print("\nПроверка корректности сортировки:")
print("Selection и Bubble совпадают:", selection_sorted == bubble_sorted)
print("Selection и TimSort совпадают:", selection_sorted == tim_sorted)
