# Дана строка, содержащая полное имя файла. Выделить из этой строки название
# первого каталога (без символов «\»). Если файл содержится в корневом каталоге, то
# вывести символ «\».

def dirx():
    file_path = input('Введите путь до вашего файла: ')
    try:
        parts = file_path.split("\\")  # для разделения строки по символу «\»
        if len(parts) > 1:  # больше 1, что означает, что в пути присутствует символ «\», тогда
            print(parts[0])  # печатаем первый элемент parts[0], который представляет название первого каталога.
        else:
            print("\\")
    except ValueError:
        print("Ошибка при обработке пути")


dirx()

# C:\Users\tax\holehe\holehe
# C:\\Users\\Baxdew\\Documents\\pz7_11.txt
# F:\Users\tax\Videos\Counter-strikeGlobalOffensive
