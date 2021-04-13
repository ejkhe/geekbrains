class Road:
    _length: int
    _width: int

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_road(self, depth):
        return (self._length * self._width * 25 * int(depth)) / 1000


road = Road(5000, 20)
print(f"Масса асфальта {road.weight_road(5)} тонн.")
