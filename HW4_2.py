from random import randint

list_length = int(input("Укажите желаемую длину списка"))
list_1 = []
while len(list_1) < list_length:
    list_1.append(randint(0, 1000000))
print(list_1)
i = 1
i +=1
list_2 = [el for el in list_1 if el > list_1[(list_1.index(el)-1)]]

print(list_2)
