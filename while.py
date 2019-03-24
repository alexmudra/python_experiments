# response = "exit"
#
# input_info = input("Please input info: ")
#
# while input_info != response:
#     print("Your input incorrect")



#Простий счьотчик з while

#
# n = 1
# while n <= 10:
#     print("The value of n is", n)
#     n = n+1;
#     if n == 10:
#         print("The end")



#Проста перевірка чисел на натуральність через цикл while

# number = 0
#
# while number <= 0:
#     print("Enter only positive number")




# Подимимось на конструкцію while...else(без break)

# counter = 5
# while counter:
#     print(counter)
#     counter -= 1
# else:
#     print("Loop is done")
#     print("counter is", counter)
#
# #Система поверне наступне:
#
# 5
# 4
# 3
# 2
# 1
# Loop is done
# counter is 0



# Подимимось на конструкцію while...else(з break)

# attems_left = 3
# while attems_left > 0:
#     attems_left -= 1
#     password = input("Enter your password ("
#                      "you have {} attems_left):".format(attems_left +1 )) #додали 1 щоб відображати коректну к-сть спроб
#     if password == "9348sdfkj":
#         print("Access granted")
#         break #нестандартне завершення цикла і секція else не буде виконуватися
# else:
#     print("Access denided")

'''
Присвойте переменной, счетчику цикла “x” значение 1
Выведите на консоль, с помощью цикла с предусловием, цифры от 1 до 5, каждую в отдельной строке
'''

# x = 1
#
# while x <= 5:
#     print(x)
#     x = x+1



'''
Напишите цикл while, который бы использовал переменную number, 
и в теле цикла предлагал ввести число использую переменную str_. 
И завершал бы работу при вводе любого отрицательного числа.
number = 0
str_ = "Enter a positive integer: "

# ...
# code
# ...

print("You have entered", number)

!!!hint    telo cikla: number = int(input(str))
'''
#
# number = 0
# str_ = ("Enter a positive integer: ")
#
# while number <=0 :
#     number = int(input(str_))
#
# print("You have entered", number)


'''
Напишите бесконечный цикл, который бы завершался вводом в консоли слова exit. 
Используйте переменную response.

response = ""

# ...
# code
# ...
'''

# #Варіант 1
# response = ""
#
# while True:
#     response = input("Введите команду")
#     if response == "exit":
#         break

#Варіант 2

while True:
    print("Enter exit to extit from loop")
    response = input("> ")
    if response == "exit":
        break

