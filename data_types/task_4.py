user_words = input('Введите несколько слов разделяя их пробелами: ')
for number, word in enumerate(user_words.split(' '), 1):
    print(number, word[:10])
