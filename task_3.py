class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._salary = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._salary.get("wage") + self._salary.get("bonus")


a = Position('Иван', 'Иванов', 'Директор', 100000, 50000)
print(a.get_full_name())
print(a.get_total_income())
