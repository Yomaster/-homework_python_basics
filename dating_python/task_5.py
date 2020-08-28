proceeds = int(input('Введите информацию о доходе фирмы: '))
costs = int(input('Введите информацию о издержках фирмы: '))
if proceeds > costs:
    print('Выручка фирмы больше издержек')
    profitability = proceeds - costs
    print('Рентабельность равна', profitability)
    number_employees = int(input('Сколько сотрудников работают в вашей фирме: '))
    profitability_employees = profitability / number_employees
    print('Прибыль фирмы в расчете на одного сотрудника равняется', profitability_employees)
elif proceeds < costs:
    print('Компания несет убытки')
elif proceeds == costs:
    print('Экономика компании находится в стагнации')
