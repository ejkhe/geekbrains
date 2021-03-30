first_result = int(input("Введите результаты первого дня: "))
purpose = int(input("Введите желаемое кол-во километров: "))
day_number = 1
while purpose >= first_result:
    print(f"{day_number} -й день: {first_result:.2f}")
    first_result = first_result + (first_result * 0.1)
    day_number += 1
print(f" На {day_number}-й день спортсмен дости результата {purpose}")
