def my_func(positional_only1, positional_only2, positional_only3, /):
    """
    Принимает только позиционные аргументы в ввиде чисел и возвращает
    сумму двух наибольших.
    """
    arguments = [positional_only1, positional_only2, positional_only3]
    arguments.sort()
    two_max_arguments = arguments[1:]
    return two_max_arguments[0] + two_max_arguments[1]


print(my_func(34, 66, 58))
