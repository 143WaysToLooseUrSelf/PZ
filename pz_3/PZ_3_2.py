# Дано целое число, лежащее в диапазоне 1–999.
# Вывести его строку-описание вида «четное двузначное число»,
# «нечетное трехзначное число» и т. д.
def bax():
    try:
        number = int(input("Введите число в диапазоне от 1 до 999: "))

        if 1 <= number <= 9:
            print("однозначное число")
        elif 10 <= number <= 99:
            if number % 2 == 0:
                print("четное двузначное число")
            else:
                print("нечетное двузначное число")
        elif 100 <= number <= 999:
            if number % 2 == 0:
                print("четное трехзначное число")
            else:
                print("нечетное трехзначное число")
        else:
            raise ValueError("[-] Ошибка: Введите число в диапазоне от 1 и 999")

    except ValueError as e:
        print(f"[-] Ошибка: {e}")
        bax()


bax()