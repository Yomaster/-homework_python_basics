user_month = 0
while not 1 <= user_month <= 12:
    user_month = int(input('Введите число месяца: '))

seasons = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for season, a in seasons.items():
    if user_month in a:
        print(f'Ваше время года {season}')
