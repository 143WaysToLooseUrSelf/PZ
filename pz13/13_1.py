# В матрице найти минимальный и максимальные элементы.

import random

N = int(input('Введите размер матрицы: '))
matrix = [[random.randint(0, 20) for i in range(N)] for i in range(N)]

print(f'Исходная матрица: {matrix}')
print('Минимальный элемент: ', min(min(matrix)))
print('Максимальный элемент: ', max(max(matrix)))
