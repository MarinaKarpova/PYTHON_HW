var1 = int(input("Введите первую переменную"))
var2 = int(input("Введите вторую переменную"))
var3 = int(input("Введите третью переменную"))

def total(var1, var2, var3):
    global var_list
    var_list = [var1, var2, var3]
    var_list.remove(min(var_list))
    return(sum(var_list))


total(var1, var2, var3)
print(f"Сумма наибольших двух аргументов равна {sum(var_list)}")