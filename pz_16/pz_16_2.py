# �������� ����� "�������", ������� �������� ���������� � �����, �������� � ����.
# �������� ������ "�������" � "�������", ������� ����������� �� ������
# "�������". ������ ����� ������ ����� �����, ������� ������� ���������� �
# ���� �������.

class human:
    def __init__(self, name, age, sex):  # method
        self.name = name
        self.age = age
        self.sex = sex


class man(human):
    def __init__(self, name, age, sex):  # method
        super().__init__(name, age, sex)


class woman(human):
    def __init__(self, name, age, sex):  # method
        super().__init__(name, age, sex)


Vitaliy = man('Vitek', '25', '�������')

print("��� �������� -", Vitaliy.sex)
