def division(dividend, divisor):
    """Выполняет деление двух чисел.

    Возвращает частное. Если делитель был равен
    нулю возвращает строку-предупреждение.
    """
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return 'Деление на ноль запрещено'


user_numbers = int(input('Введите делимое: ')), int(input('Введите делитель: '))
print(division(*user_numbers))
