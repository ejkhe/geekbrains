"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
"""
result = 0
qt = False

while not qt:
    user_input = input("Введи числа через пробел или Q для выхода ").split()
    if "Q" in user_input:
        index = user_input.index("Q")
        if index > 0:
            for i in user_input[:index]:
                result += int(i)
        qt = True
        print(result)
        break
    else:
        for i in user_input:
            result += int(i)
        print(result)
