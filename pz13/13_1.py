import random
from functools import reduce

N = int(input("Введите размер матрицы: "))
matrix = [[random.randint(-10, 10) for el in range(N)] for row in range(N)]
print(f"Исходная матрица: {matrix}")

for row in matrix:
    print(row)

cols = [reduce(lambda x, y: x + y, [row[i] for row in matrix]) for i in range(N)]
print(f"Сумма элементов каждого столбца: {cols}")

matrix[1] = cols
print(f"Матрица после замены 2й строки на сумму столбцов: {matrix}")
for row in matrix:
    print(row)
