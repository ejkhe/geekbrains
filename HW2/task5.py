my_list = [7, 5, 3, 3, 2]
user_input = int(input("Введите число >>> "))
my_list.append(user_input)
my_list.sort(reverse=True)
print(my_list)