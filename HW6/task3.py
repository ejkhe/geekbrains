class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


worker = Position("Василий", "Пупкин", "Директор", 100000, 10000)
print(worker.get_full_name())
print(worker.get_total_income())
