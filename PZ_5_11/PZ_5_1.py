import random


def chars():
    char = ''
    for i in range(40):
        char += chr(random.randint(75, 120))
    print(f"Cтрока из 40 символов: {char}")
    print(f"Количество символов: {len(char)}")


chars()
