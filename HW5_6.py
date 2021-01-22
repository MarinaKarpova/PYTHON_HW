my_dict={}
with open('subjects.txt', encoding='utf-8') as f:
    for line in f:
        new_line=line.split()
        print(new_line)
        subject=new_line[0]
        hours=[]
        hour=line[line.find(':')+1:line.find("(")]



