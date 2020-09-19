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
        if not isinstance(v, int) and not isinstance(v, float) or v < 0:
            raise TypeError('необходимо ввести положительное число.')
        self.v = v
        super().__init__()

    @property
    def tissue_consumption(self):
        return round(self.v / 6.5 + 0.5, 2)


class Costume(Closes):
    """Класс костюм."""
    def __init__(self, h):
        if not isinstance(h, int) and not isinstance(h, float) or h < 0:
            raise TypeError('необходимо ввести положительное число.')
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
