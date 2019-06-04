"""
Примеры некоторых стандартных итерабельных объектов.
Пример 3: диапазон
"""

# В Python 3 range -- это итерабельный объект, который задаёт диапазон.
# В Python 2 для этого служит xrange, а range является функцией,
# которая возвращает список.
my_range = range(2, 17, 2)

for counter in my_range:
    print(counter)
