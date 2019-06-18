
values = [1, 2, 3, 4, 5]

#обходим список и используем формат
for elem in values:
    print('Check the value {}'.format(elem))

"""
Check the value 1
Check the value 2
Check the value 3
Check the value 4
Check the value 5
"""

# =============================================================
"""
 Реализуйте цикл my_for, который будет перебирать все значения итерабельного объекта iterable для функции callback. 
 Используйте переменные it – итератор, value – очередное значение. 
"""


def my_for(iterable, callback):
    it = iter(iterable)

    while True:
        try:
            value = next(it)
            callback(value)
        except StopIteration:
            break


def mes_prnt(value):
    print("Next value received:", value)

my_for(range(5), mes_prnt)
"""
Next value received: 0
Next value received: 1
Next value received: 2
Next value received: 3
Next value received: 4
"""

# ===========================================================================

"""
Реализуйте итерабельный объект SimpleIterable, который будет выдавать индексы index от 0 до 5.
"""


class SimpleIterable:
    def __getitem__(self, index):
        if 0 <= index <=5:
            return index
        else:
            raise IndexError


iterable = SimpleIterable()

for value in iterable:
    print('Here is the value {}'.format(value))
"""
Herew is the value 0
Herew is the value 1
Herew is the value 2
Herew is the value 3
Herew is the value 4
Herew is the value 5
"""
# =============================================================================


