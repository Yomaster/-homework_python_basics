with open('task_4_en.txt', 'r', encoding='utf-8') as f:
    with open('task_4_ru.txt', 'w', encoding='utf-8') as f_ru:
        list_numerals = ['Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
        for line in f:
            main_line = line.split(' ')[1:]
            main_line.insert(0, list_numerals[int(main_line[1])])
            f_ru.write(' '.join(main_line))
