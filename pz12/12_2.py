# Составить генератор (yield), который выводит из строки только буквы


def extract():
    input_string = str(input("Введите вашу строку: "))
    for char in input_string:
        if char.isalpha():
            yield char


letters_gen = extract()


letters = ''.join(letters_gen)
print(letters)
