input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [el for num, el in enumerate(input_list) if input_list[num - 1] < input_list[num] and el != input_list[0]]


print(result_list)