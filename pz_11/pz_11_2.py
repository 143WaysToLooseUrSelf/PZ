# �� ������������� ���������� ����� (text.txt) ������� �� ����� ��� ����������,
# ���������� ������ ����������. ������������ ����� ����, � ������� ��������� ����� �
# ������������ ����� ������ ������ � �������� �������.

with open('text.txt', 'r+') as txt:
    text = txt.read()
    amount =[]
    znaki =[',','!','?', '�', '�',':']
    for i in text:
        if i in znaki:
            amount.append(i)
    print(f'{text}\n')
    print('���-�� ������ ���������� � ������: ',len(amount))


with open('text.txt', 'r') as file:
    with open('file_res.txt', 'w') as file2:
        file2.write((''.join(file.readlines()[::-1])))