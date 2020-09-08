def outputs_user_data(*, name, surname, year_birth, city_residence, email, phone_number):
    """
    Реализует вывод данных пользователя в одной строке.
    Принимает только именованные аргументы.
    """
    print(f'{name} {surname}, {year_birth} года рождения, город проживания: '
          f'{city_residence}, адрес электронной почты: '
          f'{email}, номер телефона: {phone_number}')


user_name = input('Ваше имя: ')
user_surname = input('Ваша фамилия: ')
user_year_birth = input('Ваш год рождения: ')
user_city_residence = input('Ваш город проживания: ')
user_email = input('Ваш адрес электронной почты: ')
user_phone_number = input('Ваш номер телефона: ')

outputs_user_data(name=user_name, surname=user_surname, year_birth=user_year_birth,
                  city_residence=user_city_residence, email=user_email, phone_number=user_phone_number)
