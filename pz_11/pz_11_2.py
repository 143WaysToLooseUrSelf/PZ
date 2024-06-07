# Из предложенного текстового файла (text.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить текст в
# стихотворной форме выведя строки в обратном порядке.

with open('text.txt', 'r+') as txt:
    text = txt.read()
    amount =[]
    znaki =[',','!','?', '...', '—',':']
    for i in text:
        if i in znaki:
            amount.append(i)
    print(f'{text}\n')
    print('Кол-во знаков препинания в тексте: ',len(amount))


with open('text.txt', 'r') as file:
    with open('file_res.txt', 'w') as file2:
        file2.write((''.join(file.readlines()[::-1])))