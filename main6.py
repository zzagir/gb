from itertools import count, cycle

a = 10
my_list = [b for b in range(8)]
counter = count()
cycler = cycle(my_list)

print([next(counter) for b in range(a)])
print([next(cycler) for b in range(a)])
