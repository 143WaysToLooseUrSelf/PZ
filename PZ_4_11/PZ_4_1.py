# Дано целое число N (>0).
# Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).


try:
    N = int(input("Введите целое число N: " + "\n"))

    if N <= 0:
        raise ValueError("N должно быть больше 0")

    result = 1.0
    for i in range(1, N + 1):
        result *= 1.0 + (i / 10)  # i / 10 = дробное значение

    print("Произведение 1.1 * 1.2 * 1.3 * ... *" + "\n" f"{N} = {result:.2f}")

except ValueError as e:
    print(f"[-] Ошибка:", str(e))
