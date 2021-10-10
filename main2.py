my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
for i in range(len(my_list) - 1):
    n = my_list[i]
    i += 1
    m = my_list[i]
    if m > n:
        new_list.append(m)
print(f'Исходный список: {my_list}')
print(f'Новый список: {new_list}')
