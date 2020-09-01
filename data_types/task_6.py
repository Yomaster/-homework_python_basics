number_products = int(input('Какое количество товаров вы хотите добавить: '))
parameters_str = input('Введите через пробел названия параметров, которые вы добавите каждому товару: ')
dict_products = {}
parameters_list = []
list_products = []
i = 1
while number_products > 0:
    for parameter in parameters_str.split(' '):
        value_parameter = input(f'{parameter} товара {i}: ')
        dict_products.update({parameter: value_parameter})
    list_products.append((i, dict_products))
    dict_products = {}
    number_products -= 1
    i += 1

parameters_list = parameters_str.split(' ')
value_parameters = []
analytics = {}
a = 0

while a < len(parameters_list):
    i = 0
    for _ in list_products:
        value_parameters.append((list_products[i])[1].get(parameters_list[a]))
        i += 1
    value_parameters_copy = value_parameters.copy()
    analytics.update({parameters_list[a]: value_parameters_copy})
    a += 1
    value_parameters.clear()
print(analytics)
