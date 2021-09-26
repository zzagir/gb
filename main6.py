a = int(input('Сколько вы бегаете в км?: '))
b = int(input('Введите цель в км: '))
percent = a / 100 * 10
day = 0
while a < b:
    day += 1
    percent = a / 100 * 10
    a = a + percent
    print(f'{day}-й день: {a}')

print(f'На {day}-й день спортсмен достиг не менее {b} киллометров')


