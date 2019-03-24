
#Цикл for з кінцевим значенням.Вивести числа починаючи з 0

# for i in range(5):
#     print("i has value: ", i)
#
# #Вивід:
# i has value:  0
# i has value:  1
# i has value:  2
# i has value:  3
# i has value:  4


#Цикл for з кінцевим значенням. Вивести числа починаючи з 1

# for i in range(5):
#     print("i has value: ", i+1)
#
# i has value:  1
# i has value:  2
# i has value:  3
# i has value:  4
# i has value:  5


#Виведем елементи в інтервалі між 2 і 5

# for i in range(2, 5):
#      print("i has value: ", i+1)
#
#
# i has value:  3
# i has value:  4
# i has value:  5


# #Цикл із початковим значенням(1), максимальним значенням(20) і кроком в (3)

# for i in range (1, 20, 3):
#     print(i)
#
# #Вивід:
# 1
# 4
# 7
# 10
# 13
# 16
# 19



#Цикл із початковим(10), макимальним(0), і кроком в -1 який буде віднімати одиницю від 10ти
# for i in range(10, 0, -1):
#     print(i)
#
# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1


# #Цикл for...break (після break цикл виконуватися не буде)
# for i in range(10):
#     print(i)
#     if i == 8:
#         break
# #Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8


# #Цикл for...continue(інструція continue пропускає все що нижче неї(ітерацію)
#
# for i in range(10):
#     if i == 8:
#         continue
#     print(i)
#
# #Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 9


# # Цикл while...else можна легко замінити на for...else
#
# for attems_left in range (3, 0, -1):
#     attems_left -= 1
#     password = input("Enter your password ("
#                      "you have {} attems_left):".format(attems_left))
#     if password == "9348sdfkj":
#         print("Access granted")
#         break #нестандартне завершення цикла і секція else не буде виконуватися
# else:
#     print("Access denided")









#В циклі можна використовувати замість "і" просто знак "_"

# def print_numbers(limit): #
#     for _ in range(limit):
#         print(_)

#print_numbers(10)

# output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
#
#---------------------------------------------------------------

#Підрахунок чисел Фібоначі за допомогою FOR

# numbers_for_fib = 100 #будем проходитись по цим числам
# fibs = [1 , 2]
#
# for i in range (numbers_for_fib - 2):#проходимось циклом і з кожною ітерацією мінусюємо 2
#     fibs.append(fibs[i] + fibs[i + 1])
#
# print("Fibonnachi's numbers: ", fibs)
#
# #---------------------------------------------------------------
#
# #Приклад перебору значень в dict через цикл for
#
# countries_population = {} #ініціалізували новий дікшінарі
#
# countries_population = {
#     'Ukraine': 52000000,
#     'France': 62000000,
#     'Japan': 126693000
# }
#
# #Отримати значення із словаря countries_population
#
# population_in_ukraine = countries_population['Ukraine']
# print("Ukraine has: ", population_in_ukraine)
# '''
# Ukraine has:  52000000
# '''
#
# #обійти всі елементи словаря в циклі
#
# for i in countries_population:
#     print(i, countries_population[i])
'''
Ukraine 52000000
Japan 126693000
France 62000000
'''


'''
 Используя цикл for выведите все чётные числа в диапазоне от 1 до 10 включительно. 
 Переменная number – счетчик цикла. Использовать оператор continue.

# ...
# code
# ...

    print("Current number is", number)
'''

"""
Виведем через цикл всі нечотні числа(використаємо ділення по модулю)

"""

number = None

for number in range(10):
    if number % 2 != 0:
        print("Current number is", number)
    number += 1
"""
Current number is 1
Current number is 3
Current number is 5
Current number is 7
Current number is 9
"""

