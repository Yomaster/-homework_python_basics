"""
Реализация программы работы с органическими клетками,
состоящими из ячеек.
"""


class Cell:
    """Класс ограническая клетка.

    Реализует несколько операций взаимодействия элементов.
    """

    def __init__(self, nucleuses):
        """Принимет число ячеек клетки."""
        if not isinstance(nucleuses, int) or nucleuses < 0:
            raise TypeError('принимаются только целые положительные числа.')
        self.nucleuses = nucleuses

    def __add__(self, other):
        """Реализует сложение ячеек двух клеток."""
        return Cell(self.nucleuses + other.nucleuses)

    def __sub__(self, other):
        """Реализует вычитание ячеек двух клеток.

        В случае отрицательного значения возвращает
        соответствующее исключение.
        """
        if self.nucleuses - other.nucleuses <= 0:
            raise ValueError('возможен только положительный результат операции.')
        return Cell(self.nucleuses - other.nucleuses)

    def __mul__(self, other):
        """Реализует умножение ячеек двух клеток."""
        return Cell(self.nucleuses * other.nucleuses)

    def __truediv__(self, other):
        """Реализует целочисленное деление ячеек двух клеток."""
        return Cell(self.nucleuses // other.nucleuses)

    def make_order(self, n):
        """Организуйте ячейки по рядам."""
        number_complete_rows = self.nucleuses // n
        if number_complete_rows == 0:
            return '*' * self.nucleuses
        number_elements_last_row = self.nucleuses % (n * number_complete_rows)
        last_row = '*' * number_elements_last_row
        all_rows = ['*' * n for _ in range(number_complete_rows)]
        all_rows.append(last_row)
        return '\n'.join(all_rows)


if __name__ == '__main__':
    a = Cell(17)
    b = Cell(2)
    sum_cell = a + b
    print(sum_cell.nucleuses)
    sub_cell = a - b
    print(sub_cell.nucleuses)
    mul_cell = a * b
    print(mul_cell.nucleuses)
    truediv_cell = a / b
    print(truediv_cell.nucleuses)
    print(a.make_order(5))
