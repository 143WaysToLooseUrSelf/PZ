# Из заданной строкиот образить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"


import string


def fab():
    stroka = '"--msg-template=\"$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'

    for symbol in stroka:
        if symbol in string.punctuation:  # проверяет, является ли текущий символ символом пунктуации
            yield symbol  # возврат символа


for symbol in fab():
    print(symbol, end='')  # без переноса строки
