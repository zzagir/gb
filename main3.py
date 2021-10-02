seasons = {'Это зима': (1, 2, 12),
           'Это осень': (3, 4, 5),
           'Это лето': (6, 7, 8),
           'Это весна': (9, 10, 11)}
month = int(input('Введите цифру месяца: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)