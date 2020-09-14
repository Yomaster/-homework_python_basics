with open('task_3.txt', 'r', encoding='utf-8') as f:
    list_salaries = []
    low_income = []
    for line in f:
        surname, salary = line.split(' ')
        if int(salary) < 20000:
            low_income.append(surname)
        list_salaries.append(int(salary))
average_salary = sum(list_salaries) / len(list_salaries)
print('Фамлии сотрудников, оклад которых менее 20 тыс.:', ', '.join(low_income))
print('Средней величина дохода сотрудников состовляет', average_salary)
