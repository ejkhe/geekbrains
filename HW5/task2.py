"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

amount_str = 0

with open("task2.txt") as file_read:
    for i, item in enumerate(file_read.readlines()):
        amount_str = i
        print("Количество слов в строке № ", i + 1, "-", len(item.split()))

print("Всего строк в файле ", amount_str + 1)