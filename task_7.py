"""Реализация собственного класса комплексных
чисел, их сложения и умножения."""


class ComplexNumber:
    """Класс комплексное число."""
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        if self.real_part != 0:
            return f'({self.real_part}+{self.imaginary_part}j)'
        return f'{self.imaginary_part}j'

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)

    def __mul__(self, other):
        return ComplexNumber(self.real_part * other.real_part - self.imaginary_part * other.imaginary_part,
                             self.real_part * other.imaginary_part + self.imaginary_part * other.real_part)


# Проверка в сравнении со встроенным типом данных комплексных чисел
a1 = ComplexNumber(1, 7)
a2 = ComplexNumber(0, 9)
c1 = complex(1, 7)
c2 = complex(0, 9)

print(a1)
print(c1)
print(a1 + a2)
print(c1 + c2)
print(a1 * a2)
print(c1 * c2)

