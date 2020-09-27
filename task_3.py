"""
Реализация создания списка и проверки его на
наличие только чисел с применением собственного
класса-исключения.
"""


class OwnError(ValueError):
    """Класс-исключение."""
    def __init__(self, txt):
        self.txt = txt


def creating_list_numbers():
    """Создает список и пошагово заполняет его данными
    пользователя.

    При вводе типа данных "не число" выводит соответствующее
    предупреждение.

    По окончанию возвращает готовый список.
    """

    user_list = []
    while True:
        try:
            user_number = input('Введите число для заполнения списка. Для окончания ввода введите знак "!": ')
            if user_number == "!":
                break
            not_error_count = 0
            for i in range(len(user_number)):
                for valid_elements in range(10):
                    if str(valid_elements) == user_number[i]:
                        not_error_count += 1
                        break
                    if user_number[0] == '-' and len(user_number) > 1 and list(user_number).count('-') == 1:
                        not_error_count += 1
                        break
                    if user_number[i] == '.' and len(user_number) > 1 and list(user_number).count('.') == 1:
                        not_error_count += 1
                        break
            if not_error_count != len(user_number):
                raise OwnError('Необходимо ввести число')
            else:
                user_list.append(float(user_number))
        except OwnError as err:
            print(err)
    return user_list


print('Ваш список:', creating_list_numbers())
