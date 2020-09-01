my_list = [7, 5, 3, 3, 2]
count = int(input('Сколько элементов в рейтинг вы хотите добавить? '))
while count > 0:
    count -= 1
    idx = len(my_list) - 1
    user_number = int(input('Введите целое положительное число: '))
    while True:
        if user_number < my_list[idx]:
            my_list.insert(idx+1, user_number)
            break
        elif user_number == my_list[idx]:
            my_list.insert(idx+1, user_number)
            break
        elif user_number > my_list[idx] and idx > 0:
            idx -= 1
            continue
        else:
            my_list.insert(0, user_number)
            break
print(my_list)
