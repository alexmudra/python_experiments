import json
from json import *
import requests

# Серелізація - це трансформація даних в байти. Запис даних кудись - наприклад в файл. В основному використову
# эться метод dumps.

#damp - напряму записує в json (із пітона в джейсом)
# damps - із пітона в строку. А строку можна зберегти в змінну і робити маніпуляції.

# Десерелізація - це трансформація даних. Зчитування з файла. В основному loads.

#https://www.w3schools.com/python/python_json.asp  подивитися



# записати їх в файл

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}


# записуємо дані в стрінгу
w_to_str = dumps(data)
print(w_to_str)

#записуємо дані в файл
dump(data, open("w_file.json", 'w'),indent=4)

#indent=4) ставить 4 пробіли
# sep = "."


a = (8, "Q")

b = dumps(a)
c = loads(b)

print(a == b)
print("It's a: ",type(a))
print("It's b: ",type(b))
"""
It's a:  <class 'tuple'>
It's b:  <class 'str'>
"""


q = load(open("w_file.json", 'r'))
print(q)

#https://jsonplaceholder.typicode.com

r = requests.get("https://jsonplaceholder.typicode.com/todos")
e = loads(r.text)
print(e)