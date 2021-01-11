word = input("Введите слово, состоящее из маленьких латинских букв")


def int_func():
    list(word)
    i = 0
    if ord(word[i]) < 97 or ord(word[i]) > 122:
        print("пожалуйста, вводите только маленькие латинские буквы")
        i += 1
    if ord(word[i]) >= 97 and ord(word[i]) <= 122:
        print(str((word).title()))


my_list = list(input("Введите слова, разделенные пробелом"))
my_list = my_list[::2]
for el in my_list:
    int_func()
print(my_list)