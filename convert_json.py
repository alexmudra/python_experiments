import json
from pprint import pprint


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(dir(Colors))

# print(Colors.RED + "RED" + Colors.ENDC)

'''
Відкрити файл json і перевести всі поля json в стрінгу
'''
path = 'my.json'

# with open(path, 'r') as f:
#     data = json.loads(f.read())
# print("1->>>>>>",data)

with open(path) as json_data:
    data = json.load(json_data)

'''
Вивести з json нейм і амоунт + карренсі
'''
"""
Часткове рішення 1
"""
bids = data["data"]['bids']

for b in bids:
    pprint(b)
print("---------------------------------------\n")
print("Info from NAME" + str(b['tenderers'][0]))



'''
Вивести з json нейм і амоунт + карренсі
'''
'''
Моє рішення 2
'''

amount = b["value"]["amount"]
currency = b["value"]["currency"]
valueAdded = b["value"]["valueAddedTaxIncluded"]

for tenderer in b["tenderers"]:
    print(str(tenderer["name"]), end=' ')
    print(str(amount) + " " + str(currency) + " " +str(valueAdded))


