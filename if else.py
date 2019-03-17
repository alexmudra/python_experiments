# a = input("Enter number: ")
# if int(a) >= 1 and  int(a) <=10:
#     print('This is correct number')
# else:
#     print('This is incorrect number')

#  Напишите код который бы в зависимости от выбранного пункта меню сохраненного в переменной choice,
#  выводил бы на консоль соответственно слова “File”, “View”, “Exit”. Иначе – “Incorrect choice”
# print("""Menu:
# 1. File
# 2. View
# 3. Exit""")
# choice = input("Enter your choice: ")
#
# # ...
# # cod
# # ...

# print("""Menu:
# 1. File
# 2. View
# 3. Exit
# """)
#
# choice = input("Enter your choice:")
# if choice == "1":
#     print("File")
# elif choice == "2":
#     print("View")
# elif choice == "3":
#     print("Exit")
# else:
#     print("Incorrect choice")
#
# #########################################
#
# print("""Menu:
# 1. File
# 2. View
# 3. Exit
# """)
#
# choice = int(input("Enter your choice:"))
#
# if choice == 1:
#     print("File")
# elif choice == 2:
#     print("View")
# elif choice == 3:
#     print("Exit")
# else:
#     print("Incorrect choice")
#
# ###############################################
#
#
# print("""Menu:
# 1. File
# 2. View
# 3. Exit
# """)
#
# choice = input("Enter your choice:")
#
# if choice == "1":
#     print("'File'")
# elif choice == "2":
#     print("'View'")
# elif choice == "3":
#     print("'Exit'")
# else:
#     print("'Incorrect choice'")
# ###############################################
#
# print("""Menu:
# 1. File
# 2. View
# 3. Exit
# """)
#
# choice = input("Enter your choice:")
#
# if choice == "1":
#     print("“File”")
# elif choice == "2":
#     print("“View”")
# elif choice == "3":
#     print("“Exit”")
# else:
#     print("“Incorrect choice”")

###########################################

# Напишите код в соответствии с инструкциями в задании
# 10
#     Присвойте переменной state_msg значение “Ready” либо “Not ready yet”
#     в зависимости от состояния логической переменной is_ready. Используйте тернарный оператор.
# is_ready = False
#
# # ...
# # code
# # ...
#
# print(state_msg)

#Перший варіант вирішення
is_ready = True

if is_ready:
    state_msg = "Ready"
else:
    state_msg = "Not ready yet"

print(state_msg)

is_ready and "Ready" or "Not ready yet"

#Другий варіант вирішення

is_ready = False


state_msg = is_ready and "Ready" or "Not ready yet"

print(state_msg)

#Вирішення через ТЕРНАРНИЙ ОПЕРАТОР

is_ready = False

state_msg = "Ready" if is_ready else "Not ready yet"
print(state_msg)

