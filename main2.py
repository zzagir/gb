def register(name, surname, year, city, email, number):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город: {city}, Еmail: {email}, Телефон: {number}')


register(
    name=input('Введите имя: '),
    surname=input('Введите фамилию: '),
    year=input('Введите год рождения: '),
    city=input('Введите город: '),
    email=input('Введите email: '),
    number=input('Введите номер телефона: ')
)
