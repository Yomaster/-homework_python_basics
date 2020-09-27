"""
Реализация класса, производящего валидацию даты.
"""


class Date:
    """Класс дата."""

    __date = None

    def __init__(self, date_str='31-01-2000'):
        """Принимает значение даты в строковом формате вида '31-01-2000'"""
        Date.__date = date_str
        self.date_str = date_str
        self.result_validation = Date.validation()

    @classmethod
    def type_conversion(cls):
        """Конвертирует строку в необходимый для дальнешей обработки данных
        формат.
        """
        date_list = list(map(int, cls.__date.split('-')))
        return date_list

    @staticmethod
    def validation():
        """Производит валидацию и возвращает соответствующую информацию в
        строковом виде.
        """
        date_list = Date.type_conversion()
        day = date_list[0]
        month = date_list[1]
        year = date_list[2]
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if not 1 <= day <= 31:
                return 'Количество дней не соответствует заданному месяцу'
        if month in [4, 6, 9, 11]:
            if not 1 <= day <= 30:
                return 'Количество дней не соответствует заданному месяцу'
        if month == 2 and year % 4 == 0:
            if not 1 <= day <= 29:
                return 'Количество дней не соответствует заданному месяцу'
        if month == 2 and year % 4 != 0:
            if not 1 <= day <= 28:
                return 'Количество дней не соответствует заданному месяцу'
        if not 1 <= month <= 12:
            return 'Неверное количество месяцев'
        return 'Верная дата'

    def __str__(self):
        return f'{self.result_validation}: {self.date_str}'


a = Date('01-02-2017')
b = Date('02-13-2000')
c = Date('31-09-2020')

print(a)
print(b)
print(c)
