with open("numbers.txt", 'r+', encoding='utf-8') as f:
   rus_list=['Один', 'Два', 'Три', 'Четыре']
   init_list=f.readlines()
   i=0
for el in init_list:
         el=el.split()
         el=list(el.pop(2))
         el=el.insert(0, rus_list[i])
         i+=1
         print(el)