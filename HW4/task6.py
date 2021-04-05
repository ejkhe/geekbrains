from itertools import cycle

# Первый скрипт
# for i in count(3, 1):
#     print(i)
#     if i == 10:
#         break


# Второй скрипт
test_list = [el for el in range(10)]
num_end = 0
for i in cycle(test_list):
    if num_end < 20:
        print(i)
        num_end += 1
    else:
        break
