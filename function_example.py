
# #Зробимо функцію яка буде друкувати всі числа які входять в інпут від юзера (від 0 до числа в інпуті)
#
# def print_numbers(limit): #об'явим ф-ію із формальним параметром(параметром ф-ії)
#     for i in range(limit): #в циклі перебираємо параметр limit
#         print(i) #друкуємо її
#
#
# n = int(input("Input any number: ")) #об'являємо перемінну n з фактичним параметром(аргументом)
# print_numbers(n) #передаємо у ф-ію аргумент n
#
# # формальник параметр limit перетворюється на фактичний параметр n



# # Приклад функції для підрахування суми чисел
#
# def add_numbers(a,b):
#      return a+b
# print(add_numbers(10,50))
#
# output:
# 60


#Приклад суміщення в одну глобальну ф-ію декількох локальних

# def print_numbers(limit):
#     for i in range(limit):
#         print(i)
#
# def main(): #Приклад суміщення в одну глобальну ф-ію декількох локальних
#
#     print_numbers(3)
#     print("************************")
#     print_numbers(4)
#     print("************************")
#     print_numbers(5)
#
#
# #Приклад запуску глобальної ф-ії через модуль name. Іншими словами запускаємо даний файл як программу
# if __name__ == "__main__":
#     main()#наша ф-ія
# output:
# 0
# 1
# 2
# ************************
# 0
# 1
# 2
# 3
# ************************
# 0
# 1
# 2
# 3
# 4



# #Приклад використання ф-ії в тілі іншої функції
#
# def add_numbers(first, second):
#     print("Результат ф-ії: ", first, second)
#     return first * second
#
# inside_fuction_result = add_numbers(2, add_numbers(5,10))
# inside_function_result = add_numbers(2, 5) + add_numbers(5,4)
# inside_function_result = add_numbers(5, 5) / add_numbers(5,4)
#
# print(inside_function_result)
# # output:
# Результат ф-ії:  5 10
# Результат ф-ії:  2 50
# Результат ф-ії:  2 5
# Результат ф-ії:  5 4
# Результат ф-ії:  5 5
# Результат ф-ії:  5 4
# 1.25



#Функція з умовою if ... else

# def function_if_else(x):
#     if x > 0:
#         return x * 5
#     else:
#         return x * 1
#
#
# def function_range(): #ф-ія для виводу значень ф-ії function_if_else в проміжку значень
#     for i in range (-3, 4):
#         y = function_if_else(i)
#         print('Value of function(',i,') = ', y, sep='')
# function_range()
# output:
# Value of function(-3) = -3
# Value of function(-2) = -2
# Value of function(-1) = -1
# Value of function(0) = 0
# Value of function(1) = 5
# Value of function(2) = 10
# Value of function(3) = 15


#--------------------------------------------------------

#Ф-ія з іменованими параметрами. Ф-ія повертає інфо про об'єкт

def print_info(object_name, color, price):
    print("Oblect name is: ", object_name, sep="\t")
    print("Object colour: ", color, sep="\t")
    print("Object price: ", price, sep="\t")
    print()

print_info("skdfj", "red", 3223)
# output:
# Oblect name is: 	skdfj
# Object colour: 	red
# Object price: 	3223

#Заміним параметри функції напряму.
print_info(object_name="cool", color="purpe", price=1000)
# Oblect name is: 	cool
# Object colour: 	purpe
# Object price: 	1000


#Заміним рандомно параметри функції
print_info(price=2349, color="purpe", object_name="super",)
# Oblect name is: 	super
# Object colour: 	purpe
# Object price: 	2349

#Передамо одночасно позиційний параметр(Coffee) і іменовані аргументи(з =)
#Завжди треба передавати першим позиційний аргумент, а вже потів іменовані аргументи
print_info("Coffee", price=3000, color="orange")
# Oblect name is: 	Coffee
# Object colour: 	orange
# Object price: 	3000


#-----------------------------------------------------


#Ф-ія для показу як працюють в ф-ії значення по замовчуванню

def hello_you(name="Alex"): #у ф-ії параметр по замовчуванню це Alex
    print('Hello ', name, sep='')
# hello_you("Igor")
# Hello Igor

#------------------------------------------------------------------------

#Приклад функції (на прикладі Факторіалу) без рекурсії

def no_factorial(n):
    result = 1
    for multiplier in range(2, n + 1):
        result *=multiplier
    return result

print("The", no_factorial(5),"is the factorial")

#The 120 is the factorial

#Переробимо ф-ію no_factorial на рекурсію

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)
print("Recursion resulr is:", recursive_factorial(5))



