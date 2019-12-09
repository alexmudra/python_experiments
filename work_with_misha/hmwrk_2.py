"""
1) Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

2) Яша плавал в бассейне размером N × M метров и устал. В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков (не обязательно от ближайшего) и y метров от одного из коротких бортиков. Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик? Программа получает на вход числа N, M, x, y. Программа должна вывести число метров, которое нужно проплыть Яше до бортика.

3)Дано натуральное число. Выведите его последнюю цифру.

В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.

Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.

Выведите два целых числа: время окончания урока в часах и минутах.

5)  Улитка ползет по вертикальному шесту высотой h метров, поднимаясь за день на a метров, а за ночь спускаясь на b метров. На какой день улитка доползет до вершины шеста?

Программа получает на вход натуральные числа h, a, b.

Программа должна вывести одно натуральное число. Гарантируется, что a>b.

НА фори

1) Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N, затем вводится ровно N целых чисел. Какое наименьшее число переменных нужно для решения этой задачи?

2) Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). Программа должна вывести номер потерянной карточки.

Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.

"""



"""
=======================================================================================================================
1) Даны три целых числа. Определите, сколько среди них совпадающих. 
Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
"""


# f_number = int(input("Input first number: "))
# s_number = int(input("Input second number: "))
# th_number = int(input("Input third number: "))
#
# if f_number == s_number == th_number:
#     print("The number are equal and value is", f_number)
# elif f_number == s_number or s_number == th_number or f_number == th_number:
#     print("2 equal numbers are available")
# else:
#     print("The numbers aren't equal")



#====================================================================================


"""
1) Дано несколько чисел. Вычислите их сумму. 
Сначала вводите количество чисел N, затем вводится ровно N целых чисел. 
Какое наименьшее число переменных нужно для решения этой задачи?
"""

n = int(input("Input the quantity of numbers: "))

a = 0
for i in range(int(input("Enter a number: "))):
    a += int(input("Add the number to iterator: "))
    print(i)

#не розумію



#====================================================================================

"""
2) Для настольной игры используются карточки с номерами от 1 до N. 
Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). 
Программа должна вывести номер потерянной карточки.

Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.
"""

n = int(input())
sum = 0

for i in range(1, n + 1):
    sum += i

for i in range(1, n):
    sum -= int(input())

print(sum)

