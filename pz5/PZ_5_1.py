#  Составить функцию, которая напечатает сорок любых символов.

from random import randint

symbols_list = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'g', 'x', 'l', 's', 'z', 'w']


def symb():
    try:
        word = len(symbols_list) - 1
        print('Ваши 40 символов: ')
        result = ""
        for i in range(40):  # цикл для выбора 40 символов
            a = randint(0, word)
            res = symbols_list[a]  # выбирает символ из списка по случайному индексу
            result += res  # добавляет символ к результату
        print(result)
    except ValueError:
        print("Произошла ошибка!")
        symb()


symb()
