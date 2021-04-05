from functools import reduce

num_list = [el for el in range(100, 1001) if el % 2 == 0]


def main_func(el, el_next):
    return el * el_next


print(reduce(main_func, num_list))
