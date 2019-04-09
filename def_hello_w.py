'''
  Напишите функцию с названием hello_world, которая будет выводить в консоль фразу - Hello, world!
'''

# def hello_world():
#     print("Hello, world!")
#
# hello_world()
# #///////////////////////////////////////////////
#
# '''
#    Напишите функцию с названием print_square,
#    которая будет принимать параметр num и выводить в консоль квадрат числа num.
#    Не используйте в теле функции дополнительные переменные
# '''
# #варіант 1
# def print_square (num):
#     num = num ** 2
#     print(num)
#
# print_square(10)
# #100
#
# #варіант 2
# def print_square1 (num):
#     print(num * num)
#
# print_square1(3)
# #9
# #////////////////////////////////////////////
#
# # Напишите функцию add_numbers, которая возвращает результат сложения двух своих
# # параметров first и second.Дополнительные переменные не использовать.
# #
# # # ...
# # # code
# # # ...
#
# def add_numbers(first, second):
#
#     return first + second
# result = add_numbers(2,4)
# print(result)
# #6
#
# def print_square(num):
#     return num * num
# print(print_square(2))
#
# #//////////////////////////////////////////////////
#
# #приклад вложеної функції
#
# def function (x):
#     if x > 0:
#         return x * 2
#     else:
#         return x * 3
#
#
# def main_func():
#     for i in range(-3, 4):
#         y = function(i)
#     print('function(', i,') = ',i, sep='')
#
#
# main_func()
#
# #function(3) = 3
#
#
# '''
# Приклад присвоювання номінальних і фактичних параметрів і ф-ій
# '''
#
# def table(width=1.5, legs=4, color="brown" ):
#     print("Table width -", width)
#     print("Table legs -", legs)
#     print("Table color -", color)
#
#
# table()
# table(legs=2, color="black", width=2)
# table(legs=2)
# table(1.2, 2, "gray")
# table(1.1, 3)
# table(legs=4, width=2, color="white")
# table(color="green", width=2, legs=2)
#
# print("/////////////////////////////////////////////////////////")
#
# def table(width=1.5, legs=4, color="brown" ):
#     print("Table width -", width)
#     print("Table legs -", legs)
#     print("Table color -", color)
#
#
# table()
# # table(width=2, color="black", legs=2)
# # table(legs=2)
# # table(1.2, 2, "gray")
# table(1.1, 3)
# # table(width=2, legs=4, color="white")
# # table(color="green", width=2, legs=2)
#
#
# #//////////////////////////////////////////
#
# # Напишите функцию sum_ принимает три
# # параметра a, b, c.Параметр “c” равен нулю по умолчанию.Функция должна возвращать
# # сумму всех трех аргументов.Не использовать дополнительные переменные.
#
#
# def sum_ (a,b,c = 0):
#     return a+b+c
#
# print (sum_(100,1))
# #101

#//////////////////////////////////////

# Напишите функцию с именем func которая будет выводить в консоль числа от 0 до 4,
# каждое в новой строке если ее запустить без параметров.
# Либо числа от 0 до n-1, где n – параметр функции. Используйте цикл for и переменную итератор i.
#

# def func (n):
#     if n == 0 and n <=4:
#         return n
#     else:
#         return n - 1
#
# def func1():
#     for i in range (0, 6):
#         y = func(i)
#         print('function(',i, ') = ', y, sep='')
#
# func1()

'''
function(0) = 0
function(1) = 0
function(2) = 1
function(3) = 2
function(4) = 3
'''


#TODO знайти коректне рішення для функції func



#////////////////////////////////////////////////////

#  Напишите функцию с именем func которая будет выводить в консоль числа от 0 до 4,
#  каждое в новой строке если ее запустить без параметров. Либо числа от 0 до n-1, где n – параметр функции.
#  Используйте цикл while и переменную итератор i. Цикл while должен проверять условие (i != n).
#
# # ...
# # code
# # ...
#
# func()

# def func (n = 5):
#     for i in range(n):
#         while i != n:
#             i +=1
#             if i == 0 and i <= 4:
#                 print(i)
#             else:
#                 n -= i
#                 print(n)

#func()
# #TODO знайти коректне рішення для функції func2


"""
  Напишите функцию с названием function и параметрами a и b, которая возвращает сумму этих параметров. 
  Напишите документационную строку к функции содержащую текст - This function adds two arguments.
"""


# def function_(a, b):
#     """- This function adds two arguments."""
#
#     return a + b
#
#
# print(function_(4, 6))
# #10
#
# #////////////////////////////////////
# # Вывести содержание документационной строки функции the_func() на консоль.
# print(function_.__doc__)
# #- This function adds two arguments.
#
# #/////////////////////////////////
#
# """
#  Напишите функцию с именем func, которая принимает три параметра a, b, c, значения по умолчанию которых 4, 10, -1 соотве
#  тственно.
#  Функция выводит в консоль максимальное значение, минимальное значение, и модуль параметра “c”.
#  Для решения задачи используйте встроенные функции Python. Порядок следования переменных не изменять.
# """
#
# def func(a = 4, b = 10, c = -1):
#
#
#     print(max(a, b, c))
#     print(min(a, b, c))
#     print(abs(c))
#
#
# func()
# """
# 10
# -1
# 1
# """
#
# #///////////////////////////////////////////////////////////////////////////////
# """
# Напишите функцию с названием str_revers,
# которая принимает параметр str_ строку, и выводит в консоль перевернутую строку,
# все символы которой идут в обратном порядке.
# Используйте цикл for, переменную итератор i
# """
#
# def str_revers(str_ = "строку"):
#     for i in reversed(str_):
#         print(i, end='')
#
# str_revers()
#
#
# #////////////////////////////////////////////
#
# """
#    Напишите функцию с названием function, которая присваивает глобальной переменной var значение "new variable"
#
# var = "variable"
#
# # ...
# # code
# # ...
#
# function()
# print(var)
# """
#
#
# var = "variable"
#
# def function():
#     global var
#     var = "new variable"
#
# function()
# print(var)

#глобальна перемінна буде мати значення new variable

#////////////////////////////////////////////////

"""
    Создайте функцию с именем function(), без параметров. Объявите в ней переменную var и присвойте ей значение “variable”. 
    Создайте встроенную функцию inner() тоже без параметров, которая меняет значение ранее созданной переменной var на новое “new variable” 
"""

# def function():
#     var = "variable"
#
#
#     def inner():
#         nonlocal var
#         var = "new variable"
#//////////////////////////////////////////////

"""
Напишите функцию с сигнатурой factorial(n) которая возвращает факториал числа n. Используйте рекурсию.
"""



"""
Простенька рекурсія для циклічного підрахунку на 1"""

def rec (a):
    print("res of recursion", a)
    while a == 20:
        continue

    rec(a+1)

rec(10)
"""
res of recursion 10
res of recursion 11
res of recursion 12
res of recursion 13
res of recursion 14
res of recursion 15
res of recursion 16
res of recursion 17
res of recursion 18
res of recursion 19
res of recursion 20
"""