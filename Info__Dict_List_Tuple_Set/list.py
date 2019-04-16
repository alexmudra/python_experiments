#ПРИКЛАД З ЛІСТ(МАСИВАМИ) LIST

char_list = ['a', 'b','c']
num_list = [1,2,3,4,5]
empty_list = []

a = "This is the"
print(a, "char list: ", char_list)
print(a, "int list: ", num_list)
print(a, "empty list: ", num_list)

# This is the char list:  ['a', 'b', 'c']
# This is the int list:  [1, 2, 3, 4, 5]
# This is the empty list:  [1, 2, 3, 4, 5]

list_from_range = list(range(5)) #надрукуємо ліст з числами від 0 до 4 за допомогою ф-ії list
print(list_from_range)
#[0, 1, 2, 3, 4]


print(list("To to to la la la")) #надрукуємо ліст із стрінги шляхом преобразування в ліст
#['T', 'o', ' ', 't', 'o', ' ', 't', 'o', ' ', 'l', 'a', ' ', 'l', 'a', ' ', 'l', 'a']


#Виведем суму 1 і останнього елементу списку

print(num_list[0] + num_list[-1])
#6


#Слайси в лістах

print(num_list[:3]) #виведем вміст ліста від 1 індексу до 3го
#[1, 2, 3]

print(num_list[1:-1]) #виведем вміст ліста від 2го індекса по передостанній
#[2, 3, 4]

print(num_list[0:-1:2])#отримаємо 1 елемент і останній із кроком в 2
#[1, 3]

print(num_list[::-2])#в зворотньому порядку з кроком в 3
#[5, 3, 1]


#Розпакувати ліст
num_list = [1,2]
x, y = num_list
print("Числа після розпакування:",x , y)


#РОЗГЛЯДАЄМО in в лістах (in перевіряє входження ОДНОГО елементу в лістах(не як в стрінгах)

my_list = [1,2,3,4,5,6,7,8,9,10]
'''
#user_input = int(input("Input the value: "))

if user_input in my_list:
        print("Your input correct!")
else:
    print("Your input incorrect!")
#Input the value: 2
#Your input correct!
'''
#-----------------------------------------------------------------------

#Розглядаємо функцію len для лістів

print("Number of elements for function len: ", len(my_list))
#Input the value: 3
#Your input correct!
#Number of elements for function len :  10


my_string = 'This is my string'

print(my_string)#This is my string

print(my_string[0]) #T
print(my_string[1]) #h
print(my_string[2]) #i
print(my_string[3]) #s
print(my_string[4]) #пробіл
print(len(my_string))# 17 елементів в стінг

print(my_string[2:5]) #is
print(my_string[::5]) #Ti n
print(my_string[::2]) #Ti sm tig (виборка із кроком 2)
print(my_string[::-2]) #git ms iT (виборка в зворотньому напрямку із кроком 2)


print(my_string[2] + my_string[-1]) #ig - конкатенація 2го і останнього символів в лісті
print(my_string[2:4] + " " + my_string[-4:]) #is ring - конкатенація is пробілу 4 символів в зворот.порядку

#------------------------------------------------------------------------


#ПЕРЕГЛЯНЕМО ЧИ ВХОДИТЬ ЕЛЕМЕНТ в СТРІНГУ ЗА ДОПОМОГОЮ (in)
'''
user_input = input("Enter some text: ")

if "sasha" in user_input:
    print("Cool. You guessed Sasha")
elif "anya" in user_input:
        print("You guessed Anya")
elif "girl" in user_input:
        print("You guessed Girl")
else:
    print("Try more")
'''


#РОЗГЛЯНЕМО ОПЕРАЦІЇ ІЗ СПИСКАМИ append, index, del value
#APPEND


some_list = []

some_list.append("sa") #додали 1й елемент в пустий список
some_list.append('sha')
print(some_list[0] + some_list[1]) #sasha


#DEL
some_list_for_del = [1,2,3,4,5]

print("Before del: ", some_list_for_del) #Before del:  [1, 2, 3, 4, 5]
del some_list_for_del[1]# видалили 2й елемент в ліст
print("After using del: ", some_list_for_del) #After using del:  [1, 3, 4, 5]


#Для проходження по спискам використовуємо цикл FOR

some_list_for_for = [3,4,5,6,7,8,9,-2]

print("List before FOR loop: ", some_list_for_for)

for x in some_list_for_for: #пройдемось циклом по лісту і знайдемо квадрат для кожного числа
    print("List after FOR loop: ","{} ^ 2 = {}".format(x, x ** 2))
'''
List before FOR loop:  [3, 4, 5, 6, 7, 8, 9, -2]
List after FOR loop:  3 ^ 2 = 9
List after FOR loop:  4 ^ 2 = 16
List after FOR loop:  5 ^ 2 = 25
List after FOR loop:  6 ^ 2 = 36
List after FOR loop:  7 ^ 2 = 49
List after FOR loop:  8 ^ 2 = 64
List after FOR loop:  9 ^ 2 = 81
List after FOR loop:  -2 ^ 2 = 4
'''
#-----------------------------------------------------------

'''
Аналогично, может возникнуть задача проверки, что все элементы удовлетворяют условию. Без Python 2.5 придется писать так:
'''
numbers = [1,2,3,4,5,6,7,8,9]
if len(numbers) == len([number for number in numbers if number < 10]):
    print('Success!')
# Результат: "Success!"

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

"""
Создайте список list_r содержащий числа (0, 1, 2, 3, 4) с использование встроенной функции list().
Создайте список list_str, основанный на строке "Simple string"
"""

list_r = list(range(5))
list_str = list("Simple string")


print(list_r)
print(list_str)
"""
[0, 1, 2, 3, 4]
['S', 'i', 'm', 'p', 'l', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g']
"""

#/////////////////////////////////////////////////////

"""
 Создайте список list_str на основе фразы "Hello, world!" Далее, 
 последовательно выведите на консоль первый элемент списка, пятый и последний.
"""

list_str = list("Hello, world!")
print(list_str[0])
print(list_str[4])
print(list_str[-1])



#//////////////////////////////////////////////////

"""
приклад використання оператора in (який перевіряє входження підстроки в строку)
"""

# if list_str[0] == "H" in list_str:
#     print("The H is available")
#
# else:
#     print("The H isn't available")

#/////////////////////////////////////////////////

#TODO застряв на ub_list содержит последние три элемента my_list в обратном порядке

"""
  Дан список my_list. Создайте срез этого списка с названием sub_list
1)	sub_list содержит 3 и 4 элемент списка my_list
2)	sub_list содержит элементы my_list начиная с первого, через один
3)	sub_list содержит список my_list в обратном порядке
4)	sub_list содержит последние три элемента my_list в обратном порядке
5)	sub_list содержит копию списка my_list

my_list = [1, 10, 22, 43, 11, -2, 7]

# ...
# code
# ...

"""

my_list = [1, 10, 22, 43, 11, -2, 7]

print("Initial list", my_list)

# sub_list = my_list[2:4]
# print(sub_list)
#
# sub_list = my_list[:: 2]
# print(sub_list)
#
# sub_list = my_list[:: -1]
# print(sub_list)

# sub_list = my_list[-1],my_list[-2], my_list[-3]
# print("sub_list содержит последние три элемента my_list в обратном порядке", sub_list)

sub_list = my_list[::]
print("sub_list содержит последние три элемента my_list в обратном порядке", sub_list)


# sub_list = my_list[::]
# print(sub_list)

#////////////////////////////////////////

"""
Задайте список my_list который будет содержать числа от 0 до 9. Используя функцию list(). 
Создайте функцию func, которая принимает два параметра list_ и num. Если число num входит в список list_, 
функция должна выводить на консоль фразу "This number is in list" в противном случае, 
фразу - "This number is out of list"
"""


# my_list = list(range(10))
# print(my_list)
#
#
# def func(list_, num):
#     list_ = my_list[::]
#
#     for num in list_:
#
#         if num in list_:
#             print("This number is in list")
#         else:
#             print("This number is out of list")
#
#
#
# func()
#TODO доробити цю функцію

#///////////////////////////////////////////

"""
Создайте переменную my_str, которая будет содержать текст - "This is simple text" 
Напишите проверку вхождения подстроки “imp” в my_str. Если данная подстрока присутствует, 
на консоль выдается фраза - "This text is in string"
"""


my_str = "This is simple text"
if "imp" in my_str:
    print("This text is in string")

#///////////////////////////////////////

"""
  Дан список my_list. Выведите на консоль длину этого списка
my_list = [4, 6, 0, 9, 11, 23, 1, 10]

# ...
# code
# ...
"""

my_list = [4, 6, 0, 9, 11, 23, 1, 10]
print(len(my_list))

#8

#////////////////////////////////////////

"""
Задайте список my_list с элементами от 0 до 9.
1)	Добавьте 11 элемент равный 100
2)	Удалите третий элемент списка
3)	Измените 10й элемент списка на 99
"""


my_list = list(range(10))
print("Initial list  0 - 9", my_list)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list.append(100)
print("Added 100 via append", my_list)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

del my_list[2]
print("Delete 2-d element", my_list, sep=" ")
#[0, 1, 3, 4, 5, 6, 7, 8, 9, 100]

my_list[9] = 99
print("Replace 9th element(it's == 100) to 99", my_list, sep=" ")




