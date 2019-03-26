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

