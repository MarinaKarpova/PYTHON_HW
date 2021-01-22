with open('countnumbers.txt', 'w') as f:
  numbers=input("Введите набор чисел, разделенных пробелами")
  f.write(numbers)
  my_list=numbers.split()
  new_list = [int(el) for el in my_list]
  print(sum(new_list))
