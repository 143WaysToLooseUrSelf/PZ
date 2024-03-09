# В последовательности на n целых чисел найти и вывести:
# 1. максимальный среди положительных
# 2. минимальный среди отрицательных
# 3. произведение элементов

import random
from functools import reduce

n = 5

num = [random.randint(-10, 10) for i in range(n)]
positive_max = max(filter(lambda x: x > 0, num))
negative_max = min(filter(lambda x: x < 0, num))
proizvedenie = reduce(lambda x, y: x * y, num)

print(f"Последовательность чисел: {num}")
print(f"Максимальное положительное число: {positive_max}")
print(f"Минимальное отрицательное число: {negative_max}")
print(f"Произведение элементов: {proizvedenie}")
