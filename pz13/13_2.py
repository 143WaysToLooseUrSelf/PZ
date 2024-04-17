# В матрице найти минимальный элемент в предпоследней строке.

import random

N = int(input("Введите размер матрицы: "))
matrix = [[random.randint(-10, 10) for el in range(N)] for row in range(N)]
print(f"Исходная матрица: {matrix}")

minel = min(matrix[-2])
print(f"Минимальный элемент в предпоследней строке {minel}")
