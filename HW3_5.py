numbers = input("Введите числа через пробел")
print(numbers.split())
numbers = numbers[::2]


def total():
    print("Если хотите узнать сумму этих чисел - нажмите Enter, если хотите завершить программу"
          " - нажмите клавишу q")
    for el in numbers:
        el = int(el)

    if numbers[-1] == "q":
        print("Программа завершена")
    else:
        print(f'Сумма введеных чисел равна {sum(numbers)}')
        answer = (input("Хотите добавить еще несколько чисел?")).lower
        while answer == "да":
            numbers1 = input("Введите числа через пробел")
            print(numbers1.split())
            print(f'Сумма ВСЕХ введеных числе равна {sum(numbers) + sum(numbers1)}')
            if answer == "нет":
                break


total()
