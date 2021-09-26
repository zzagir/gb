sec = int(input('Введите секунды: '))
hour = sec // 3600

sec = sec % 3600
minute = sec // 60

sec = sec % 60
print(f'{hour}:{minute}:{sec}')