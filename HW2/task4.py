user_input = input("Введите строку >>> ")
words_list = user_input.split()
for i, item in enumerate(words_list):
    if len(item) > 10:
        print(i + 1, item[:10])
    else:
        print(i + 1, item)
