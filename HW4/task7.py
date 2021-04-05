def fact(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
        yield factorial


result = [el for el in fact(4)]
print(result)
