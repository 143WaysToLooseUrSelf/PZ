#  Составить функцию, которая напечатает сорок любых символов.

from random import randint

symbols_list = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'g', 'x']


def symb():
    try:
        word = len(symbols_list) - 1
        print('Ваши 40 символов: ')
        result = ""
        for i in range(40):
            a = randint(0, word)
            res = symbols_list[a]
            result += res
        print(result)
    except ValueError:
        print("Произошла ошибка!")
        symb()


symb()
