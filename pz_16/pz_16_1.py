# Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
# Добавьте методы для вычисления среднего балла и определения, является ли студент
# отличником.

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
        return 4.5 <= average <= 5


Vitaliy = student('Виталий', 'Savage', [5, 5, 5, 5, 4, 5, 3])

print(Vitaliy.ave_marks(Vitaliy.marks))
print('Student is otlichnik -', Vitaliy.res(Vitaliy.ave_marks(Vitaliy.marks)))