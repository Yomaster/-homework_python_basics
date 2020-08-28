user_time = int(input('Введите количество секунд: '))
hours = user_time // 3600
minutes = (user_time - 3600 * hours) // 60
seconds = user_time - 3600 * hours - 60 * minutes
print(f'Время в формате чч:мм:сс: {hours}:{minutes}:{seconds}')
