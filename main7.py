from itertools import count
from math import factorial


def fgen():
    for i in count(1):
        yield factorial(i)


x = 0
for q in fgen():
    if x < 15:
        print(q)
        x += 1
    else:
        break
