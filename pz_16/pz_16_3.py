# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle


class student:

    def __init__(self, name, sec_n, marks):
        self.name = name
        self.sec_n = sec_n
        self.marks = marks

    @staticmethod
    def ave_marks(marks):
        average = sum(marks) / len(marks)
        return average

    @staticmethod
    def res(average):
        st_is_otl = 4.5 <= average <= 5
        return st_is_otl


def save_def(stude, file):
    with open(file, 'wb') as f:  # wb - запись в 2ичном ф
        pickle.dump(stude, f)  # запись в файл f


def load_def(file):
    with open(file, 'rb') as f:  # rb - чтение в 2ичном ф
        studen = pickle.load(f)
    return studen


Kovalkin = student('Артём', 'Ковалкин', [2, 5, 5, 3, 4, 5, 4])
Vitebsk = student('Денис', 'Витебск', [3, 2, 5, 4, 4, 5, 5])
KioRio = student('Стас', 'КиоРио', [5, 4, 5, 4])

students_info = [Kovalkin, Vitebsk, KioRio]

for stud in students_info:
    save_def(stud, 'students.pkl')
    students = load_def('students.pkl')
    print(students.ave_marks(students.marks))
    print('Student is otlichnik -', students.res(students.ave_marks(students.marks)))
