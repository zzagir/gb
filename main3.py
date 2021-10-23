class NotANumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


result_list = []
while True:
    value = input('Введите число для добавления в список или stop для выхода: ')

    if value == 'stop':
        print(f'Ваш список: {result_list}')
        break

    try:
        if not value.isnumeric():
            raise NotANumberException('NaN!')
        result_list.append(int(value))
        print(f'Список на данный момент: {result_list}')
    except NotANumberException as error:
        print('Вы ввели не число')
