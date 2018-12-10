import json
from pprint import pprint



'''
нужно посчитать сколько элементов с типом int в списке (что лежит внутри каждого элемента проверять не надо) и вывести в консоль
а еще лучше посчитать сколько элементов каждого типа в списке, 
чтобы получилось что-то типа {'int': 3, 'str': 1, 'dict': 1, 'tuple': 1, 'bool': 1, 'NoneType': 1, 'set': 1, 'frozenset': 1}
'''

data = [1, '2', {'3': 3}, 4, (5,), True, 6, None, {7, 8}, frozenset({9, 10})]
pprint(data)



x = int(input("Input the text 1: "))
while x == 1:
    print("sdkfj")

