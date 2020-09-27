"""
Реализация класса склада с функциями приема оргтехники
и распределения ее в различные подразделения.
"""

from abc import ABC


class OfficeEquipmentWarehouse:
    """Класс склад.

    Принимает список подразделений,
    для которых необходимо произвести распределение.
    """

    __warehouse = {}
    __distributed_products = {}

    def __init__(self, *args):
        self._company_divisions = args

    def acceptance(self, product, quantity):
        """Рализует прием оргтехники на склад, производя
        соответствующую проверку типов данных товара.
        """

        if not isinstance(product, OfficeEquipment):
            raise TypeError('Неправильный тип данных оргтехники')
        if not isinstance(quantity, int):
            raise TypeError('Количество товаров должно быть числом')
        if not quantity > 0:
            raise TypeError('Количество товаров должно быть положительным числом')

        # Блок try except необходим для обработки добавления уже имеющегося на
        # складе товара
        try:
            self.__warehouse.update({product: quantity + self.__warehouse[product]})
        except KeyError:
            self.__warehouse.update({product: quantity})

    def revision(self):
        """Форматирует информацию о количестве товара на складе
         и возвращает данные в удобном для чтения формате.
         """

        revision_list = {}
        for product_cortege in self.__warehouse.items():
            revision_list.update({product_cortege[0].name: product_cortege[1]})
        return revision_list

    def distribution(self):
        """Производит распределение товара по подразделениям."""
        for division in self._company_divisions:
            OfficeEquipmentWarehouse.__distributed_products.update({division: {}})
        for product_cortege in self.__warehouse.items():
            integer_division = self.__warehouse[product_cortege[0]] // \
                               len(OfficeEquipmentWarehouse.__distributed_products)
            remainder = self.__warehouse[product_cortege[0]] % len(OfficeEquipmentWarehouse.__distributed_products)
            if integer_division != 0:
                for division in OfficeEquipmentWarehouse.__distributed_products:
                    OfficeEquipmentWarehouse.__distributed_products[division].update({product_cortege[0].name:
                                                                                      integer_division})
            if remainder != 0:
                count = 0
                for division in OfficeEquipmentWarehouse.__distributed_products:
                    OfficeEquipmentWarehouse.__distributed_products[division].update({product_cortege[0].name:
                                                                                      integer_division + 1})
                    count += 1
                    if count == remainder:
                        break
        return OfficeEquipmentWarehouse.__distributed_products


class OfficeEquipment(ABC):
    """Абстрактный класс оргтехники."""
    def __init__(self, name, price, max_format, dimensions):
        self.name = name
        self.price = price
        self.max_format = max_format
        self.dimensions = dimensions

    def __str__(self):
        return self.name


class Printer(OfficeEquipment):
    """Класс принтер."""
    def __init__(self, name, price, max_format, dimensions, printing_technology, printing_speed, amount_colors):
        super().__init__(name, price, max_format, dimensions)
        self.printing_technology = printing_technology
        self.printing_speed = printing_speed
        self.amount_colors = amount_colors


class Scanner(OfficeEquipment):
    """Класс сканер."""
    def __init__(self, name, price, max_format, dimensions, scanner_type, sensor_type, scanning_speed):
        super().__init__(name, price, max_format, dimensions)
        self.scanner_type = scanner_type
        self.sensor_type = sensor_type
        self.scanning_speed = scanning_speed


class MFP(OfficeEquipment):
    """Класс многофункциональное устройство."""
    def __init__(self, name, price, max_format, dimensions, printing_technology, printing_speed, amount_colors,
                 scanner_type):
        super().__init__(name, price, max_format, dimensions)
        self.printing_technology = printing_technology
        self.printing_speed = printing_speed
        self.amount_colors = amount_colors
        self.scanner_type = scanner_type


p = OfficeEquipmentWarehouse('Подразделение1', 'Подразделение2', 'Подразделение3')

a1 = Printer('Canon PIXMA TS304', 3988, 'A4', '430x143x282', 'пьезоэлектрическая струйная', 7.7, 4)
a2 = Printer('HP LaserJet Pro M15w', 7639, 'A4', '346x159x189', 'лазерная', 18, 1)
b1 = Scanner('Canon CanoScan LiDE 300', 4490, 'A4', '250x42x367', 'планшетный', 'CIS', 8)
b2 = Scanner('Brother ADS-1200', 18005, 'A4', '300x83x103', 'протяжный', 'CIS', 50)
c1 = MFP('HP LaserJet Pro MFP M28w', 9929, 'A4', '360x198x264', 'лазерная', 18, 1, 'планшетный')
c2 = MFP('Brother MFC-L2740DWR', 23818, 'A4', '409x316x398', 'лазерная', 30, 1, 'планшетный/протяжный')

p.acceptance(a1, 1)
p.acceptance(a1, 1)
p.acceptance(a2, 4)
p.acceptance(b1, 9)
p.acceptance(b2, 5)
p.acceptance(c1, 8)
p.acceptance(c2, 12)

print(p.revision())
print(p.distribution())
