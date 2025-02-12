# Пузырьковая сортировка (Bubble Sort)

import time

mas = [5, 18, 7, 0, -5, 4, 14, 3, 27, -2, 21, 8, -13, 2, 6, 10, 23, 15, 27, 23]
n = len(mas)
print(f'\nЗаданный список:\n {mas}')
print(f'\nКоличество элементов в списке:\n {n}')

"""
- **Флаг `swapped`:** 
Добавлен флаг, который отслеживает, произошел ли обмен элементов.
Если за одну полную итерацию обмен не произошел, значит, массив уже отсортирован, и цикл можно завершить досрочно.

- **Измерение времени:** 
- **`time.perf_counter()`:** 
Используется для измерения времени с высокой точностью.
- **Умножение на 1,000,000:** 
Переводит время из секунд в микросекунды (1 секунда = 1,000,000 микросекунд).
"""



# Начало измерения времени
start_time = time.perf_counter()

# Улучшенный алгоритм сортировки пузырьком
for run in range(n-1):
    swapped = False
    for i in range(n-1-run):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]
            swapped = True
    if not swapped:
        break

# Окончание измерения времени
end_time = time.perf_counter()

# Время выполнения в микросекундах
elapsed_time_microseconds = (end_time - start_time) * 1_000_000

print(f'\nОтсортированный список:\n {mas}')
print(f'\nВремя выполнения сортировки:\n {elapsed_time_microseconds:.3f} микросекунд')