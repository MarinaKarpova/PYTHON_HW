import json
firms = {}
average_profit=[]
with open('firms.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data=line.split()
        profit=int(data[2]) - int(data[3])
        firms[0]=profit
        average_profit.append(profit)

average_profit = sum(average_profit)/len(average_profit)
out_data = [firms, {'average_profit': average_profit}]
with open('firms.json', 'w+') as f_json:
    json.dump(out_data, f_json)
    print(json.load(f_json))