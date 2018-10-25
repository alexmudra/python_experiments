import json
from pprint import pprint

'''
Відкрити файл json і перевести всі поля json в стрінгу
'''


path = 'my.json'

# with open(path, 'r') as f:
#     data = json.loads(f.read())
# print("1->>>>>>",data)


with open(path) as json_data:
    data = json.load(json_data)
#print("2->>>>>" ,data)

'''
Вивести з json нейм і амоунт + карренсі
'''


bids = data["data"]['bids']
for b in bids:
    pprint(b)


