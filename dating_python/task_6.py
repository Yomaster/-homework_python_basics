initial_distance = int(input('Сколько километров спортсмен пробежал в первый день: '))
end_distance = int(input('Введите расстояние, чтобы узнать день, на который спортсмен сможет его пробежать: '))
overall_result = initial_distance
day = 1
print(f'{day}-й день: {round(initial_distance, 2)}')
while overall_result / end_distance < 1:
    overall_result += overall_result * 0.1
    day += 1
    print(f'{day}-й день: {round(overall_result, 2)}')

print(f'на {day}-й день спортсмен достиг результата — не менее {end_distance} км.')
