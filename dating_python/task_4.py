# Сложное решение

while True:
    user_number = int(input('Введите целое положительное число: '))
    if user_number > 0:
        break

a = 0
length_str = 1
max_number = 9
super_max = 9
count_mega = user_number

while user_number - 10 ** length_str >= 0:
    length_str += 1

while True:
    while True:
        if length_str == 0:
            break
        max_number = count_mega // (10 ** (length_str - 1))
        count_mega -= max_number * (10 ** (length_str - 1))
        length_str -= 1
        if max_number == super_max:
            a = 1
            break
    if a == 1:
        break
    a = 0
    super_max -= 1
    while user_number - 10 ** length_str >= 0:
        length_str += 1
    count_mega = user_number
print(max_number)

# Новое решение

user_number = input('Введите число: ')
max_n = 9
while True:
    max_n = str(max_n)
    if max_n in list(user_number):
        break
    max_n = int(max_n)
    max_n -= 1
print(max_n)
