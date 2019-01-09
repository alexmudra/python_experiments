
#Створення кортежу
point = (1, 6)
print(point)
'''
(1, 6)
'''

#Змінити кортеж не можна
#Додати елемент в кортеж не можна
#Видалити елемент в кортежі не можна


#Розпакувати кортеж
x, y = point
print(x , y)
'''
1 6
'''

#Пройтись в циклі по елементам кортежа
for coordinate in point:
    print(coordinate)
'''
1
6
'''

#Конвертувати кортеж в список

tupple_to_list = list(point)
print(type(tupple_to_list))
'''
<class 'list'>
'''


#Конвертувати список в кортеж
list_to_tuple = tuple([1, 6])
print(type(list_to_tuple))
'''
<class 'tuple'>
'''

#Скласти кортежі
def collect_two_tuples():
    if (1, 2, 3, 4) + (5, 6, 7) == (1, 2, 3, 4, 5, 6, 7):
        print(True)
    else:
        print(False)

collect_two_tuples()
'''
True
'''
