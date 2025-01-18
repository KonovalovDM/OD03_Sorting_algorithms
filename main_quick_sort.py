# Быстрая сортировка (Quick Sort)

import time

s = [5, 18, 7, 0, -5, 4, 14, 3, 27, -2, 21, 8, -13, 2, 6, 10, 23, 15, 27, 23]
n = len(s)
print(f'\nЗаданный список:\n {s}')
print(f'\nКоличество элементов в списке:\n {n}')

"""
- **Оптимизация:** 
Используется генератор списков для всех трех частей (`left`, `center`, `right`),
что улучшает читаемость кода.

- **Переиспользование переменной:** 
Используется переменная `sorted_s` для хранения отсортированного списка, 
чтобы избежать повторного вызова `quick_sort()` в строке `print`.

- **Измерение времени:** 
- `time.perf_counter()`: Используется для измерения времени с высокой точностью.
- Умножение на 1,000,000: Переводит время из секунд в микросекунды (1 секунда = 1,000,000 микросекунд).
"""

# Улучшенный алгоритм быстрой сортировки
def quick_sort(s):
    if len(s) <= 1:
        return s
    element = s[0]
    left = [i for i in s if i < element]
    center = [i for i in s if i == element]
    right = [i for i in s if i > element]
    return quick_sort(left) + center + quick_sort(right)

# Начало измерения времени
start_time = time.perf_counter()

# Сортировка
sorted_s = quick_sort(s)

# Окончание измерения времени
end_time = time.perf_counter()

# Время выполнения в микросекундах
elapsed_time_microseconds = (end_time - start_time) * 1_000_000

print(f'\nОтсортированный список:\n {sorted_s}')
print(f'\nВремя выполнения сортировки:\n {elapsed_time_microseconds:.3f} микросекунд')