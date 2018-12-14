
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

def function_if_else(x):
    if x > 0:
        return x * 5
    else:
        return x * 1


def function_range(): #ф-ія для виводу значень ф-ії function_if_else в проміжку значень
    for i in range (-3, 4):
        y = function_if_else(i)
        print('Value of function(',i,') = ', y, sep='')
function_range()
# output:
# Value of function(-3) = -3
# Value of function(-2) = -2
# Value of function(-1) = -1
# Value of function(0) = 0
# Value of function(1) = 5
# Value of function(2) = 10
# Value of function(3) = 15
