with open('salary.txt', 'r+', encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    new_line = line.split()
    if float(new_line[1]) < 20000:
     print(new_line[0])
    salaries = []
    salaries=salaries.append(new_line[1])
    print(sum(salaries)/len(salaries))





