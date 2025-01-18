# Сортировка выбором (Selection Sort)

import time
from typing import List

numbers = [5, 18, 7, 0, -5, 4, 14, 3, 27, -2, 21, 8, -13, 2, 6, 10, 23, 15, 27, 23]
n = len(numbers)
print(f'\nЗаданный список:\n {numbers}')
print(f'\nКоличество элементов в списке:\n {n}')

def selection_sort(arr: List[int]) -> None:
    """
    Функция сортирует список arr по возрастанию
    методом сортировки выбором.

    :param arr: Список целых чисел для сортировки.

    - **Аннотации типов:**
    Использованы для указания, что функция принимает список целых чисел (`List[int]`) и не возвращает значение (`None`).
    - **Проверка перед обменом:**
    Добавлено условие `if min_index != i`, чтобы избежать ненужных обменов, когда минимальный элемент уже находится на своем месте.
    """
    # Проходим по всему списку
    n = len(arr)
    for i in range(n):
        # Предполагаем, что первый элемент в неотсортированной части - это минимальный
        min_index = i
        # Ищем минимальный элемент в оставшейся части списка
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части, если они разные
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


# Начало измерения времени
start_time = time.perf_counter()

# Сортировка
selection_sort(numbers)

# Окончание измерения времени
end_time = time.perf_counter()

# Время выполнения в микросекундах
elapsed_time_microseconds = (end_time - start_time) * 1_000_000

print(f'\nОтсортированный список:\n {numbers}')
print(f'\nВремя выполнения сортировки:\n {elapsed_time_microseconds:.3f} микросекунд')