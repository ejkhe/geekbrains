user_list = [int(num) for num in input("Введите числа через пробел >>> ").split()]
print(user_list)

cur = 0
for i in range(int(len(user_list) / 2)):
    user_list[cur], user_list[cur + 1] = user_list[cur + 1], user_list[cur]
    cur += 2

print(user_list)
