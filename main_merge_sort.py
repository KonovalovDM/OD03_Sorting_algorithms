# Сортировка слиянием (Merge Sort)

import time
from typing import List

numbers = [5, 18, 7, 0, -5, 4, 14, 3, 27, -2, 21, 8, -13, 2, 6, 10, 23, 15, 27, 23]
n = len(numbers)
print(f'\nЗаданный список:\n {numbers}')
print(f'\nКоличество элементов в списке:\n {n}')

def merge_sort(arr: List[int]) -> List[int]:
    """
    Функция сортирует список arr по возрастанию
    методом сортировки слиянием.

    :param arr: Список целых чисел для сортировки.
    :return: Новый отсортированный список.
    """
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две половины
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Слияние отсортированных половин
    return merge(left_half, right_half)

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Функция сливает два отсортированных списка в один отсортированный список.

    :param left: Отсортированный список.
    :param right: Отсортированный список.
    :return: Новый отсортированный список.
    """
    sorted_arr = []
    i = j = 0

    # Слияние двух половин
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

# Начало измерения времени
start_time = time.perf_counter()

# Сортировка
sorted_numbers = merge_sort(numbers)

# Окончание измерения времени
end_time = time.perf_counter()

# Время выполнения в микросекундах
elapsed_time_microseconds = (end_time - start_time) * 1_000_000

print(f'\nОтсортированный список:\n {sorted_numbers}')
print(f'\nВремя выполнения сортировки:\n {elapsed_time_microseconds:.3f} микросекунд')

"""
### Объяснение:
- **Рекурсия:** 
Функция `merge_sort` рекурсивно делит список на две части до тех пор, пока размер каждой части не станет меньше или равен 1.
- **Слияние:** 
Функция `merge` объединяет два отсортированных списка в один, сравнивая элементы и добавляя меньший элемент к итоговому списку.
- **Сложность:** 
Сортировка слиянием имеет временную сложность `O(n log n)`, что делает её эффективной для сортировки больших массивов.
"""