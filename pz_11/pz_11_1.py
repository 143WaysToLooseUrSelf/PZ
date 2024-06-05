# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
#
# Исходные данные:
# Количество элементов:
# Максимальный элемент:
# Произведение элементов меньших 0 в первой половине:

from random import randint
with open('file.txt', 'w+') as file:
    file.write(str([randint(-10, 10) for i in range(10)]))
with open('file.txt', 'r+') as file:
    sti = (file.read()[1:][:-1].split(", "))

lis = []
for i in sti:
    lis.append(int(i))

num = 1
for i in sti[:5]:
    if int(i) < 0:
        num = num * int(i)

one = ('Исходные данные: ', lis)
two = ('Кол-во элементов: ', len(lis))
three = ('Минимальный элемент: ', min(lis))
four = ('Произведение элементов меньших 0 в первой половине:', num)

with open('res.txt', 'w+') as res:
    res.write(f'{str(one)}\n')
    res.write(f'{str(two)}\n')
    res.write(f'{str(three)}\n')
    res.write(f'{str(four)}')

with open('res.txt', 'r+') as res:
    print(res.read())