class Car:
    def __init__(self, speed, color, name, is_polce):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_polce

    def go(self):
        return f"{self.name} поехала."

    def stop(self):
        return f"{self.name} остановилась."

    def turn(self, direction):
        return f"{self.name} повернула на {direction}."

    def show_speed(self):
        return f"Текущая скорость {self.name} = {self.speed}."


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Внимание! Привышение скорости")
        return f"Текущая скорость {self.name} = {self.speed}."


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Внимание! Привышение скорости")
        return f"Текущая скорость {self.name} = {self.speed}."


class PoliceCar(Car):
    pass


car = TownCar(30, "white", "oka", False)
print(car.show_speed())
car2 = SportCar(330, "red", "lamborghini", False)
print(car2.show_speed())
car3 = WorkCar(80, "grey", "logan", False)
print(car3.show_speed())
car4 = PoliceCar(200, "white/blue", "skoda", True)
print(car4.show_speed())
print(car4.turn("лево"))