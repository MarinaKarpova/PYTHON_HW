x = int(input("Введите действительное положительное число"))
y = int(input("Введите целое отрицательное число"))


def my_func(x, y):
    i = 1
    total=1
    while i <= abs(y):
        total *= x
        i += 1
    result = 1 / total
    print(result)


my_func(x, y)
