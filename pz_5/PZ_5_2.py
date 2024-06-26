# Описать функцию SortInc3(A, B, C), меняющую содержимое переменных
# A, B, C таким образом, чтобы их значения оказались упорядоченными
# по возрастанию (A,B, C — вещественные параметры, являющиеся одновременно входными и
# выходными. С помощью этой функции упорядочить по возрастанию два данных
# набора из трех чисел: (Ai, Bi, Ci) и (A2, B2, C2).


def SortInc3(A, B, C):
    if A > B:
        A, B = B, A
    if B > C:
        B, C = C, B
    if A > B:
        A, B = B, A
    print(A, B, C)


Ai, Bi, Ci = map(float, input("Введите три числа через пробел: ").split())  # разбивает строку на отдельные числа
A2, B2, C2 = map(float, input("Введите три числа через пробел: ").split())  # преобразует числа из строкового
# формата во float

print("Значения первого набора:")
SortInc3(Ai, Bi, Ci)

print("Значения второго набора:")
SortInc3(A2, B2, C2)
