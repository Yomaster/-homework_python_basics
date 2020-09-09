def fact(n):
    f = 1
    for i in range(0, n):
        f *= i + 1
        yield f


user_number = int(input('Введите целое число: '))
for el in fact(user_number):
    print(el)
