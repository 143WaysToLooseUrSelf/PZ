# В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).
from functools import reduce

n = int(input("Введите номер строки: "))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

row = matrix[n]
sum_row = sum(row)
proizvedenie = reduce(lambda x, y: x * y, row)

print(f"Сумма элементов строки {n}: {sum_row}")
print(f"Произведение элементов строки {n}: {proizvedenie}")
