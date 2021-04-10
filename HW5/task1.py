"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("task1.txt", "w") as file:
    user_input = input("Введите текст ")
    while user_input:
        print(user_input, file=file)
        user_input = input("Введите текст ")
        if not user_input:
            break
