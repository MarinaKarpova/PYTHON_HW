with open('123.txt', encoding='utf-8') as f:
     a =len(f.readlines())
     print(f' число строк в тексте: {a}')
with open('123.txt', encoding='utf-8') as f:
     for line in f.readlines():
        new_line = line.split()
        print(len(new_line))


