from itertools import cycle

my_list = (input("Введите элементы для списка").split())
print(my_list)
a = int(input("Сколько раз напечатать каждый элемент?"))
c = 0
for el in cycle(my_list):
    if c > a:
        break
    print(el)
    c += 1
