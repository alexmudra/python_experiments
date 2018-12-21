import json


from pprint import pprint

'''
нужно посчитать сколько элементов с типом int в списке (что лежит внутри каждого элемента проверять не надо) и вывести в консоль

а еще лучше посчитать сколько элементов каждого типа в списке, 
чтобы получилось что-то типа {'int': 3, 'str': 1, 'dict': 1, 'tuple': 1, 'bool': 1, 'NoneType': 1, 'set': 1, 'frozenset': 1}
'''

data = [1, 4, {'3': 3}, 4, (5,), True, 6, None, {7, 8}, frozenset({9, 10})]
data_s = [1, 2]
pprint(data)
pprint(data_s)

#TODO: доробити цикл із умовою(21-12-2018)

print("The elements in list DATA is", len(data))
print("The elements in list data_s is", len(data_s))

for x in data:

    integer = type(int)
    stringa = type(str)


    if x is integer:
        print("Integer")
    elif x is bool(x):
        print("Boolean")
    elif x is stringa:
        print("String")
    elif x is dict(x):
       print("Dictionary")
    elif x is set(x):
        print("Set")