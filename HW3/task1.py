"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""

dig_a = input("Введите число a >>> ")
dig_b = input("Введите число b >>> ")

if dig_a.isdigit() and dig_b.isdigit():
    dig_a = int(dig_a)
    dig_b = int(dig_b)
else:
    print("Ошибка введено не число")


def division(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        return "На ноль делить нельзя"


print(division(dig_a, dig_b))
