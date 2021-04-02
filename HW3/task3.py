"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(dig_a, dig_b, dig_c):
    temp_list = [dig_a, dig_b, dig_c]
    temp_list.pop(min(temp_list))
    return temp_list[0] + temp_list[1]


print(my_func(10, 15, 2))
