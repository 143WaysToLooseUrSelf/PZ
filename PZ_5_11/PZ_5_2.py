# Описать функцию SortInc3(A, B, C), меняющую содержимое переменных
# A, B, C таким образом, чтобы их значения оказались упорядоченными
# по возрастанию (A,B, C — вещественные параметры, являющиеся одновременно входными и
# выходными. С помощью этой функции упорядочить по возрастанию два данных
# набора из трех чисел: (Ai, Bi, Ci) и (A2, B2, C2).


def SortInc3():
    A = float(input("Введите значение A: "))
    B = float(input("Введите значение B: "))
    C = float(input("Введите значение C: "))

    sorted_values = sorted([A, B, C])
    return sorted_values[0], sorted_values[1], sorted_values[2]


A1, B1, C1 = SortInc3()
print("Упорядоченный набор (A1, B1, C1):", A1, B1, C1)

A2, B2, C2 = SortInc3()
print("Упорядоченный набор (A2, B2, C2):", A2, B2, C2)
