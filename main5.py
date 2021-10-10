from functools import reduce


def my_func(a, b):
    return a * b


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list)
new_list = [reduce(my_func, my_list)]
print(new_list)
