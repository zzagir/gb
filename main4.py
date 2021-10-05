# Первое решение с помощью **

def my_func(x, y):
    y = -y
    x = x ** y
    print(x)


my_func(
    x=int(input('Введите положительное число: ')),
    y=int(input('Введите отрицательное число: '))
)


# Второе решение с помощью цикла

def my_func2(x, y):
    for i in range(y - 1):
        x *= x
    return 1 / x


print(my_func2(
    x=int(input('Введите x: ')),
    y=int(input('Введите y: '))
))
