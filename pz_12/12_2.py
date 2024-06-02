# Составить генератор (yield), который выводит из строки только буквы


def extr():
    input_str = str(input("Введите вашу строку: \n"))
    for chax in input_str:
        if chax.isalpha():
            yield chax


letters_gen = extr()
letters = "".join(letters_gen)
print(letters)
