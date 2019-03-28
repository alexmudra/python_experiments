'''
  Напишите функцию с названием hello_world, которая будет выводить в консоль фразу - Hello, world!
'''

def hello_world():
    print("Hello, world!")

hello_world()
#///////////////////////////////////////////////

'''
   Напишите функцию с названием print_square, 
   которая будет принимать параметр num и выводить в консоль квадрат числа num. 
   Не используйте в теле функции дополнительные переменные
'''
#варіант 1
def print_square (num):
    num = num ** 2
    print(num)

print_square(10)
#100

#варіант 2
def print_square1 (num):
    print(num * num)

print_square1(3)
#9
#////////////////////////////////////////////

# Напишите функцию add_numbers, которая возвращает результат сложения двух своих
# параметров first и second.Дополнительные переменные не использовать.
#
# # ...
# # code
# # ...

def add_numbers(first, second):

    return first + second
result = add_numbers(2,4)
print(result)
#6

def print_square(num):
    return num * num
print(print_square(2))

#//////////////////////////////////////////////////

#приклад вложеної функції

def function (x):
    if x > 0:
        return x * 2
    else:
        return x * 3


def main_func():
    for i in range(-3, 4):
        y = function(i)
    print('function(', i,') = ',i, sep='')


main_func()

#function(3) = 3


'''
Приклад присвоювання номінальних і фактичних параметрів і ф-ій
'''

def table(width=1.5, legs=4, color="brown" ):
    print("Table width -", width)
    print("Table legs -", legs)
    print("Table color -", color)


table()
table(legs=2, color="black", width=2)
table(legs=2)
table(1.2, 2, "gray")
table(1.1, 3)
table(legs=4, width=2, color="white")
table(color="green", width=2, legs=2)

print("/////////////////////////////////////////////////////////")

def table(width=1.5, legs=4, color="brown" ):
    print("Table width -", width)
    print("Table legs -", legs)
    print("Table color -", color)


table()
table(width=2, color="black", legs=2)
table(legs=2)
table(1.2, 2, "gray")
table(1.1, 3)
table(width=2, legs=4, color="white")
table(color="green", width=2, legs=2)