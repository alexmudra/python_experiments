import json
from pprint import pprint

import my.json


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


