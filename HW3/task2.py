"""
 Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
name = input("Введите имя ")
lastname = input("Введите фамилию ")
year = input("Введите год рождения ")
city = input("Введите город проживания ")
email = input("Введите email ")
phone = input("Введите номер телефона ")


def person_info(name, lastname, year, city, email, phone):
    return f"Имя: {name} Фамилия: {lastname} Год рождения {year} Город: {city} Email: {email} Телефон: {phone}"


print(person_info(name=name, lastname=lastname, year=year, city=city, email=email, phone=phone))
