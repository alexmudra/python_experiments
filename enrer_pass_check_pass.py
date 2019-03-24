#Приклад простого коду який перевіряє 3 рази ввід коректного паролю


attempts_left = 3
while attempts_left > 0:
    attempts_left -= 1
    password = input("Enter your password: ")
    if password == "98abc":
        print("Access granted")
        break
else:
    print("Access denied")

"""
Enter your password: dfdf
Enter your password: df
Enter your password: dsf
Access denied
"""