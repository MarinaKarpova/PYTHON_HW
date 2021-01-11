number1 = int(input("Введите числитель"))
number2 = int(input("Введите знаменатель"))


def devision(number1, number2):

    try:
        quotient = number1 / number2
        print(f"Частное равно {quotient}")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")


devision(number1, number2)
