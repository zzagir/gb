def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    result = my_list[0] + my_list[1]
    print(result)


my_func(
    a=int(input('Введите число 1: ')),
    b=int(input('Введите число 2: ')),
    c=int(input('Введите число 3: '))
)
