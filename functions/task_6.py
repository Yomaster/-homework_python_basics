def int_func(string_text):
    """
    Принимает текст. Первую букву разделенных пробелом
    слов в этом тексте делает большой и возвращает
    результат.
    """
    text_list = string_text.split(' ')
    new_text_list = []
    for word in text_list:
        new_text_list.append(word.capitalize())
    return ' '.join(new_text_list)


user_string = input('Введите слова с маленькой буквы разделенные пробелами: ')
print(int_func(user_string))
