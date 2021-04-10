"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
"""
import re
from functools import reduce

subj = {}
with open('task6.txt', 'r') as file:
    for line in file:
        subject, lecture, practice, lab = line.split()
        subj[subject] = re.findall('\d+', lecture) + re.findall('\d+', practice) + re.findall('\d+', lab)

for i in subj:
    subj[i] = reduce(lambda x, y: int(x) + int(y), subj[i])
print(subj)