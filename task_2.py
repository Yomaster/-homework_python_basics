"""
Реализация проекта расчета суммарного расхода ткани на
производство одежды.
"""

from abc import ABC, abstractmethod


class Closes(ABC):

    # Атрибут, который будет содержать общий расчет расхода ткани
    # для всех элементов всех дочерних классов
    total_expense = 0

    def __init__(self):
        """Реализует подсчет расхода ткани для всех элементов
        дочерних классов.
        """
        Closes.total_expense = Closes.total_expense + round(self.tissue_consumption, 2)

    @staticmethod
    def validate_value(value):
        if value < 0:
            raise ValueError("необходимо ввести положительное число.")

    @property
    @abstractmethod
    def tissue_consumption(self):
        """Абстрактный метод, который будет реализован
        в каждом дочернем классе.

        Подразумевает реализацию подсчета расхода ткани
        для каждого элемента.
        """
        pass


class Coat(Closes):
    """Класс пальто."""
    def __init__(self, v):
        self.validate_value(v)
        self.v = v
        super().__init__()

    @property
    def tissue_consumption(self):
        return round(self.v / 6.5 + 0.5, 2)


class Costume(Closes):
    """Класс костюм."""
    def __init__(self, h):
        self.validate_value(h)
        self.h = h
        super().__init__()

    @property
    def tissue_consumption(self):
        return round(self.h * 2 + 0.3, 2)


if __name__ == '__main__':
    a = Coat(15)
    a1 = Coat(7.1)
    b = Costume(5)
    b2 = Costume(7)
    b3 = Costume(9)

    print(a.tissue_consumption)
    print(b.tissue_consumption)

    print(Costume.total_expense)
