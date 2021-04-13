class Stationery:
    def __init__(self, title):
        self.title = title

    def drow(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def drow(self):
        print("Отрисовка ручкой")


class Pencil(Stationery):
    def drow(self):
        print("Отрисовка карандашом")


class Handle(Stationery):
    def drow(self):
        print("Отрисовка маркером")


stationery1 = Stationery("Кисть")
stationery1.drow()

stationery2 = Pen("Ручка")
stationery2.drow()

stationery3 = Pen("Карандаш")
stationery3.drow()

stationery4 = Pen("Маркер")
stationery4.drow()
