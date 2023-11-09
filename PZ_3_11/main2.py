# Дано целое число, лежащее в диапазоне 1–999.
# Вывести его строку-описание вида «четное двузначное число»,
# «нечетное трехзначное число» и т. д.

try:
    num = int(input("Введите целое число от 1 до 999: "))

    if num < 1 or num > 999:
        print("[-] Число должно быть в диапазоне от 1 до 999")
    else:
        description = ""

        if num % 2 == 0:
            description += "четное "
        else:
            description += "нечетное "

        if num < 10:
            description += "однозначное число"
        elif num < 100:
            description += "двузначное число"
        else:
            description += "трехзначное число"

        print(description)

except ValueError:
    print("[-] Ошибка: Введите целое число")
