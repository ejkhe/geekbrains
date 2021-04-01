user_input = int(input("Введите месяц в виде целого числа от 1 до 12 >>> "))


dict_months = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
for i in dict_months.items():
    if user_input in i[1]:
        print(i[0])


