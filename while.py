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

attems_left = 3
while attems_left > 0:
    attems_left -= 1
    password = input("Enter your password ("
                     "you have {} attems_left):".format(attems_left +1 )) #додали 1 щоб відображати коректну к-сть спроб
    if password == "9348sdfkj":
        print("Access granted")
        break #нестандартне завершення цикла і секція else не буде виконуватися
else:
    print("Access denided")



