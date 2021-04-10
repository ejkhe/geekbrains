"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
try:
    with open('task5.txt', 'w+') as file:
        user_input = input('Введите числа через пробел \n')
        file.writelines(user_input)
        number = user_input.split()

        print(sum(map(int, number)))
except IOError:
    print('ООшибка ввода-вывода')
except ValueError:
    print('Неправильный ввод')