# Дана строка, содержащая полное имя файла. Выделить из этой строки название
# первого каталога (без символов «\»). Если файл содержится в корневом каталоге, то
# вывести символ «\».

def dirx(file_path):
    try:
        parts = file_path.split("\\")
        if len(parts) > 1:
            return parts[0]
        else:
            return "\\"

    except ValueError:
        return "Ошибка при обработке пути"


file_name = "C:\\Users\\Baxdew\\Documents\\pz7_11.txt"
directory = dirx(file_name)
print(directory)
