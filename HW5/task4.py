"""
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
result_list = []
translate_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("task4.txt") as file:
    for i in file:
        item = i.split(" ", 1)
        result_list.append(translate_dict[item[0]] + " " + item[1])

with open("task4RU.txt", "w") as file_ru:
    file_ru.writelines(result_list)
