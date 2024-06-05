# »з предложенного текстового файла (text.txt) вывести на экран его содержимое,
# количество знаков препинани€. —формировать новый файл, в который поместить текст в
# стихотворной форме вывед€ строки в обратном пор€дке.

with open('text.txt', 'r+') as txt:
    text = txt.read()
    amount =[]
    znaki =[',','!','?', 'Е', 'Ч',':']
    for i in text:
        if i in znaki:
            amount.append(i)
    print(f'{text}\n')
    print(' ол-во знаков препинани€ в тексте: ',len(amount))


with open('text.txt', 'r') as file:
    with open('file_res.txt', 'w') as file2:
        file2.write((''.join(file.readlines()[::-1])))