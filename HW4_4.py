my_list = [3, 4, 4, 6, 7, 11, 11, 43, 56, 77, 88, 88]
my_set = {el for el in my_list if my_list.count(el) == 1}
print(my_set)
