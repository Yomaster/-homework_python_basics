"""
Реализация класса матрицы с функционалом операции сложения,
по правилам линейной алгебры.
"""


class Matrix:
    """Класс матрица."""
    def __init__(self, list1):
        """Перед инициальизацией экземпляра производит полную проверку
        переданных данных на соответствие параметрам матрицы.
        """

        # Проверка на тип данных "список"
        if not isinstance(list1, list):
            raise TypeError('ожидаемый объект list.')

        # Проверка размера
        for i, line in enumerate(list1):
            if len(line) != len(list1[i-1]):
                raise ValueError('строки матрицы должны быть равной длины.')

        # Проверка каждого элемента
        for line in list1:
            for element in line:
                if not isinstance(element, int) and not isinstance(element, float):
                    raise TypeError('элементы матрицы должны быть числами.')
        self.list1 = list1

    def __str__(self):
        """Возвращает строковое представление экземпляра в привычном виде для матриц."""

        # Приводим каждый элемент к строковому типу
        matrix_str = []
        for line in self.list1:
            matrix_str.append(list(map(str, line)))

        # Для удобства на время преобразуем столбцы в строки
        matrix_columns = zip(*matrix_str)

        # Ищем самый длинный элемент в строке
        matrix_final = []
        for column in matrix_columns:
            max_size = max(list(map(len, column)))

            # Каждому элементу меньшего размера добавляем отступ
            # в виде определенного количества пробелов, которое равно
            # разнице размеров данного элемента с максимальным
            matrix_columns_final = []
            for element in column:
                if len(element) < max_size:
                    matrix_columns_final.append(' ' * (max_size - len(element)) + element)
                else:
                    matrix_columns_final.append(element)
            matrix_final.append(matrix_columns_final)

        # Возвращаем столбцы к первоначальному виду
        matrix_final = zip(*matrix_final)

        # Приводим элементы итератора к строковому типу,
        # разделяя каждый элемент в них двойным пробелом
        matrix_final_str = []
        for line in matrix_final:
            matrix_final_str.append('  '.join(line))

        # Приводим получившийся список к строковому типу необходимого вида
        # и передаем значение
        return '\n'.join(matrix_final_str)

    def __add__(self, other):
        """Перегружает оператор '+' для сложения матриц, делая соответствующую проверку"""
        if len(self.list1) != len(other.list1) or len(self.list1[0]) != len(other.list1[0]):
            raise ValueError('матрицы должны иметь одинаковый размер')
        matrix_sum = []
        for i, line in enumerate(self.list1):
            matrix_str = []
            for j, element in enumerate(line):
                matrix_str.append(element + other.list1[i][j])
            matrix_sum.append(matrix_str)
        return Matrix(matrix_sum)


if __name__ == '__main__':
    a = Matrix([[76, 9, 87], [-10, 98.5, 44], [12, 73, 12], [34, 6, 77]])
    b = Matrix([[311, 22, 5], [37, 43, 598], [51, 0, 18], [8, 86, 7]])
    c = Matrix([[1, 2], [3, 4]])

    print(a, '\n')
    print(b, '\n')
    print(a + b)
    # print(a + c)
