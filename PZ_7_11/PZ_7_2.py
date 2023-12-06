# Дана строка, содержащая полное имя файла. Выделить из этой строки название
# первого каталога (без символов «\»). Если файл содержится в корневом каталоге, то
# вывести символ «\».

import os

file_path = 'C:\\Users\\tax\\Desktop\\hashbreaker'
directory = os.path.dirname(file_path).split(os.path.sep)[1]

if directory:

    print(directory)
else:
    print('\\')
