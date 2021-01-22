with open('my_file.txt', 'w', encoding='utf-8') as f:
  text = input("Введите ваши данные")
  if text!='':
    f.write(text+'\n')