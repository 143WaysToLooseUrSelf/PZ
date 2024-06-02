n = int(input('Введите кол-во чисел в последовательности: '))
a = []

for i in range(n):
    a.append(int(input('Введите число: ')))

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] * a[j] % 26 == 0 and a[i] != a[j]:
            count += 1
print(f'Количество пар эл-тов последовательности, кот-ые / 26: \n{count}')
