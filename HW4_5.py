from functools import reduce


def f_1(el_1, el_2):
    return el_1 * el_2


print(reduce(f_1, [el for el in range(100, 1000, 2) if el % 2 == 0]))
