initial_distance = int(input('Сколько километров спортсмен пробежал в первый день: '))
end_distance = int(input('Введите расстояние, чтобы узнать день, на который спортсмен сможет его пробежать: '))
day = 1
while True:
    print(f'{day}-й день: {round(initial_distance, 2)}')
    if initial_distance / end_distance < 1:
        initial_distance += initial_distance * 0.1
        day += 1
    else:
        break

print(f'на {day}-й день спортсмен достиг результата — не менее {end_distance} км.')
