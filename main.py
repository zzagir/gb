f = open('file.txt', 'w', encoding='utf-8')
print(input('Введите имя: '), file=f)
print(input('Введите фамилию: '), file=f)
f.close()
