# Организовать и вывести последовательность А из n чисел. Из
# последовательности А получить две последовательности В и С: в последовательности В –
# четные элементы А, в С – нечетные элементы А. Произвести суммирование
# соответствующих элементов последовательностей В и С. Найти минимальный элемент
# полученной последовательности.

import random

try:
    N = int(input("Введите кол-во случайных чисел N: "))  # Запрашиваем у пользователя количество чисел
    if N <= 0:
        raise ValueError("Число N должно быть больше нуля")

    random_x = [random.randint(-100, 100) for i in range(N)]
    print(f"Последовательность из N случайных чисел:{random_x}")

    positive = [num for num in random_x if num > 0]
    negative = [num for num in random_x if num < 0]

    count_positive = len(positive)
    count_negative = len(negative)
    all_count = len(random_x)

    print(f"\nКол-во элементов:{all_count}")
    print(f"\nПоложительные числа:{positive}")
    print(f"Количество положительных чисел: {count_positive}")

    print(f"\nОтрицательные числа:{negative}")
    print(f"Количество отрицательных чисел: {count_negative}")

except Exception as e:
    print(f"Произошла ошибка: {e}")

