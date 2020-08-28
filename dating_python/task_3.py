user_number = 0

while not 1 <= user_number <= 9:
    user_number = int(input('Введите число от 1 до 9: '))

two_digit_number = int(f'{user_number}{user_number}')
three_digit_number = int(f'{user_number}{user_number}{user_number}')
sum_numbers = user_number + two_digit_number + three_digit_number

print(sum_numbers)
