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
    return A, B, C  # возвращает упорядоченные числа в виде кортежа A, B, C


# Запрос ввода трех чисел для первого набора
A1, B1, C1 = map(float, input("Введите три числа через пробел для первого набора: ").split())
A1, B1, C1 = SortInc3(A1, B1, C1)
print("Упорядоченный набор (A1, B1, C1):", A1, B1, C1)

# Запрос ввода трех чисел для второго набора
A2, B2, C2 = map(float, input("Введите три числа через пробел для второго набора: ").split())
A2, B2, C2 = SortInc3(A2, B2, C2)
print("Упорядоченный набор (A2, B2, C2):", A2, B2, C2)

# map - для преобразования введенных пользователем строковых
# значений в числовой формат
