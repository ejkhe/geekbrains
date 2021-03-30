user_number = int(input("Введите целое положительное число: "))
max_digit = 0
while user_number > 0:
    temp_var = user_number % 10
    if temp_var >= max_digit:
        max_digit = temp_var
    user_number //= 10
print(max_digit)
