# Дана непустая строка S. Вывести строку, содержащую символы строки S, между
# которыми вставлено по одному пробелу.


def bom():
    try:
        user = input("Введите строку: ")
        if ' ' in user:
            raise ValueError("Ошибка: строка содержит пробелы")
        else:
            result = ' '.join(user)
            print(result)
    except ValueError as e:
        print(e)
        bom()


bom()
