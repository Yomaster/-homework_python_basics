import json

with open('task_7.txt', 'r', encoding='utf-8') as f:
    dict_info = {}
    total_profit = 0
    count = 0
    for line in f:
        list_info = line.split(' ')
        profit = int(list_info[2]) - int(list_info[3])
        if profit > 0:
            total_profit += profit
            count += 1
    print('Средняя прибыль компаний без убытков:', total_profit / count)
    total_profit = 0
    f.seek(0)
    for line in f:
        list_info = line.split(' ')
        profit = int(list_info[2]) - int(list_info[3])
        total_profit += profit
        dict_info.update({list_info[0]: profit})
    f.seek(0)
    average_profit = total_profit / len(list(f))

list_info_full = [dict_info, {'Средняя прибыль компаний': average_profit}]

with open('task_7.json', 'w') as f:
    json.dump(list_info_full, f)
