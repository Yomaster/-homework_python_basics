with open('task_2.txt', 'r', encoding='utf-8') as f:
    print('Количество строк в файле:', len(list(f)))
    f.seek(0)
    for idx, item in enumerate(f, 1):
        print(f'Количество элементов в строке {idx}, разделенных пробелами:', len(item.split(' ')))
