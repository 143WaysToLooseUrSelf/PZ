import re

import re

def extract_letters(text):
    for letter in re.findall(r'[a-zA-Z]', text):
        yield letter

# Пользователь вводит строку
user_input = input("Введите строку: ")
letters_generator = extract_letters(user_input)

# Выводим буквы, извлеченные из введенной строки
for letter in letters_generator:
    print(letter, end="")