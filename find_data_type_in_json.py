import json
from collections import Counter



from pprint import pprint

'''
нужно посчитать сколько элементов с типом int в списке (что лежит внутри каждого элемента проверять не надо) и вывести в консоль

а еще лучше посчитать сколько элементов каждого типа в списке, 
чтобы получилось что-то типа {'int': 3, 'str': 1, 'dict': 1, 'tuple': 1, 'bool': 1, 'NoneType': 1, 'set': 1, 'frozenset': 1}
'''

data = [1, 4, {'3': 3}, 4, (5,), True, 6, None, {7, 8}, frozenset({9, 10})]
print('Elenments of data:',  data)
print("The len elements in list DATA is", len(data))

data_s = [4, 9]
print('Elements of data_s:', data_s)
print("The elements in list DATA_S is", len(data_s))


#TODO: добавити счьотчик на кожну ітераццю

for x in (data_s):

    if type(x) is int:
        print(Counter(data_s),"Integer")
    elif type(x) is bool:
        print("Boolean")
    elif type(x) is str:
        print("String")
    elif type(x) is dict:
        print("Dictionary")
    elif type(x) is set:
        print("Set")
    elif type(x) is tuple:
        print("Tuple")
    elif type(x) is frozenset:
        print("FrozenSet")

    c = Counter(data_s)

    print(c)

