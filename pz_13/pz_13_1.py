# В матрице найти минимальный и максимальные элементы.

import random

N = int(input("Введите размер матрицы: "))
matrix = [[random.randint(-10, 10) for i in range(N)] for j in range(N)]

minimal = matrix[0][0]
maxa = 0

for i in range(N):
    for j in range(N):
        if matrix[i][j] < minimal:
            minimal = matrix[i][j]
        elif matrix[i][j] > maxa:
            maxa = matrix[i][j]

print('Исходная матрица:', matrix)
print('Максимальный элемент: ', maxa)
print('Минимальный элемент: ', minimal)
