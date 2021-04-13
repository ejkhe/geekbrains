from time import sleep


class TrafficLight:
    __color: str

    def running(self):
        self.__color = "Красный"
        print(self.__color)
        sleep(7)
        self.__color = "Желтый"
        print(self.__color)
        sleep(2)
        self.__color = "Зеленый"
        print(self.__color)
        sleep(10)


TrafficLight = TrafficLight()
TrafficLight.running()
