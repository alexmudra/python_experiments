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

bids = data["data"]['bids']
for b in bids:
    # pprint(b)

    amount = b["value"]["amount"]
    currency = b["value"]["currency"]

    for tenderer in b["tenderers"]:
        print("The user name is: " + str(tenderer["name"]), end=' ')
    print(str(amount) +' '+ str(currency))




    # print(Colors.WARNING + "This is name: " + Colors.ENDC + Colors.OKBLUE + str(name) + Colors.ENDC)
    # print(Colors.WARNING + "This is amount: " + Colors.ENDC + Colors.OKBLUE + str(amount) + Colors.ENDC)
    # print(Colors.WARNING + "This is currency: " + Colors.ENDC + Colors.OKBLUE + str(currency) + Colors.ENDC)





