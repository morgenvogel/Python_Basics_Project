from functools import reduce


def fact(n):
    try:
        yield reduce(lambda x, y: x * y, list(el for el in range(1, n + 1)))
    except TypeError:
        yield 0


for i in range(1, 4):
    print(list(fact(i)))
