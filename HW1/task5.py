proceeds = int(input("Введите выручку предприятия: "))
costs = int(input("Введите издержки предприятия: "))
if proceeds > costs:
    print("предприятие работает с прибылью.")
    print("Рентабельность выручки = ", (proceeds / costs))
    employees_number = int(input("Введите количество сотрудников на предприятии: "))
    print("Прибыль в расчете на 1 сотрудника ", (proceeds - costs) / employees_number)


else:
    print("Предприятие работает в убыток")
