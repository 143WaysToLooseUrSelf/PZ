import random

N = int(input("Введите размер матрицы: "))
matrix = [[random.randint(-10, 10) for el in range(N)] for row in range(N)]
print(f"Исходная матрица: {matrix}")

for row in matrix:
    print(row)

minel = min(matrix[-2])
print(f"Минимальный элемент в предпоследней строке {minel}")