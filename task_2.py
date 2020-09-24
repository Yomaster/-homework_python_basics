"""Реализация класса-исключения для случаев деления на ноль."""


class OwnError(Exception):
    """Класс-исключение."""
    def __init__(self, txt):
        self.txt = txt


def division(dividend, divisor):
    """Функция деления с использованием собственного
    класса-исключения.
    """
    if divisor == 0:
        raise OwnError("На ноль делить нельзя!")
    return dividend / divisor


user_number1 = int(input('Введите делимое: '))
user_number2 = int(input('Введите делитель: '))

try:
    result = division(user_number1, user_number2)
    print(f"Результат деления равен: {result}")
except OwnError as err:
    print(err)
