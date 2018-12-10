
#Цикл for з кінцевим значенням

# for i in range(5):
#     print("i has value: ", i)
#
# #Вивід:
# i has value:  0
# i has value:  1
# i has value:  2
# i has value:  3
# i has value:  4


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


# #Цикл for...continue
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


#Цикл while...else можна легко замінити на for...else

for attems_left in range (3, 0, -1):
    attems_left -= 1
    password = input("Enter your password ("
                     "you have {} attems_left):".format(attems_left))
    if password == "9348sdfkj":
        print("Access granted")
        break #нестандартне завершення цикла і секція else не буде виконуватися
else:
    print("Access denided")