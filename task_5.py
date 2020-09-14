import random

with open('task_5.txt', 'w') as f:
    list_numbers = [str(random.randint(1, 100)) for _ in range(20)]
    f.write(' '.join(list_numbers))
with open('task_5.txt') as f:
    str_numbers = f.read()
    list_numbers = list(map(int, str_numbers.split(' ')))
    print('Сумма чисел равна', sum(list_numbers))
