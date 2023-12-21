# Дана строка, содержащая полное имя файла. Выделить из этой строки название
# первого каталога (без символов «\»). Если файл содержится в корневом каталоге, то
# вывести символ «\».

def dirx(file_path):
    try:
        parts = file_path.split("\\")  # для разделения строки по символу «\»
        if len(parts) > 1:  # больше 1, что означает, что в пути присутствует символ «\», тогда
            return parts[0]  # мы возвращаем первый элемент parts[0], который представляет название первого каталога.
        else:
            return "\\"

    except ValueError:
        return "Ошибка при обработке пути"


file_name = input('Введите путь до вашего файла: ')
directory = dirx(file_name)
print(directory)

# C:\Users\tax\holehe\holehe
# C:\\Users\\Baxdew\\Documents\\pz7_11.txt
# F:\Users\tax\Videos\Counter-strikeGlobalOffensive
