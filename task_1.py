with open('user_file.txt', 'w') as f:
    user_text = 1
    while user_text:
        user_text = input('Введите строку текста: ')
        f.write(f'{user_text}\n')
