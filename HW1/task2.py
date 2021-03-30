import datetime

seconds = int(input("Введите время в секундах: "))
print(f"Результат: {datetime.timedelta(seconds=seconds)}")
