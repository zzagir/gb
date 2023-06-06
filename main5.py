revenue = int(input('Введите выручку: '))
cost = int(input('Введите издержку: '))
if revenue >= cost:
    print('Вы работаете в прибыль!:')
    rentable = revenue / cost * 100
    print(f'{rentable}%')
else:
    print('Вы работаете в убыток!')

staff = int(input('Введите количество сотрудников: '))
salary = rentable/staff
print(salary)