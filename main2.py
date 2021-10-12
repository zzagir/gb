lines = 0
words = 0
letters = 0

for line in open('file2.txt', 'r', encoding='utf-8'):
    lines += 1
    letters += len(line)
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'

print("Строк:", lines)
print("Слов:", words)
print("Букв:", letters)