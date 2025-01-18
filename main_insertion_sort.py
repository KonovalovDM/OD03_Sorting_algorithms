# Сортировка вставками (Insertion Sort)

import time
from typing import List

numbers = [5, 18, 7, 0, -5, 4, 14, 3, 27, -2, 21, 8, -13, 2, 6, 10, 23, 15, 27, 23]
n = len(numbers)
print(f'\nЗаданный список:\n {numbers}')
print(f'\nКоличество элементов в списке:\n {n}')

def insertion_sort(arr: List[int]) -> None:
    """
    Функция сортирует список arr по возрастанию
    методом сортировки вставками.

    :param arr: Список целых чисел для сортировки.
    """
    # Проходим по всему списку начиная со второго элемента
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы arr[0..i-1], которые больше ключа, на одну позицию вперед
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Начало измерения времени
start_time = time.perf_counter()

# Сортировка
insertion_sort(numbers)

# Окончание измерения времени
end_time = time.perf_counter()

# Время выполнения в микросекундах
elapsed_time_microseconds = (end_time - start_time) * 1_000_000

print(f'\nОтсортированный список:\n {numbers}')
print(f'\nВремя выполнения сортировки:\n {elapsed_time_microseconds:.3f} микросекунд')