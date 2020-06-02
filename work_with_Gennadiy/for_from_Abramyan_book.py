import math
from math import pi



# #For1. Даны целые числа K и N (N > 0). Вывести N раз число K.


def for_1 ():
    k = int(input("Input K: "))
    n = int(input("Input N: "))

    for k in range(1,n):
        print(k)




# прискоїти для color по черзі різні значення-кольори
def coror():
    i = 1
    for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
        print(i, '-th color of rainbow is ', color, sep='')
        i += 1


# For2. Даны два целых числа A и B (A < B). Вывести в порядке возрастания все
# целые числа, расположенные между A и B (включая сами числа A и B), а
# также количество N этих чисел.


def for_2():
    a = int(input("Input a: "))
    b = int(input("Input b: "))

    if a < b:
        for n in range (a,b+1):
            print(n)
    else:
        print("Enter a < b")



# For3. Даны два целых числа A и B (A < B). Вывести в порядке убывания все
# целые числа, расположенные между A и B (не включая числа A и B), а
# также количество N этих чисел.


def for_3():
    a = int(input("Input a: "))
    b = int(input("Input b: "))

    if a < b:
        for n in range (b-1, a,-1):
            print("Numbers is:",n)
        print("Num. q-ty:", b-a-1)

    else:
         print("Enter a < b")




# For4. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1,
# 2, . . . , 10 кг конфет.


def for_4():
    kandy_price = int(input("Input price: "))

    for i in range(10):
        sum = kandy_price * i
        print("Total sum for kandy price", i,"is:", sum)


# For5◦. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1,
# 0.2, . . . , 1 кг конфет

def for_5():
    one_kg_price = float(input("Input price: "))

    for i in range (1, 10, 1):
        print(i / 10, ' кг. коштує - ', one_kg_price * (i / 10), "UAH")


#or6. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1.2,
#1.4, . . . , 2 кг конфет.



def for_6():
    one_kg_price = float(input("Input price: "))

    for i in range (1,20,1):
        print(1+i/10, ' кг. коштує - ', one_kg_price * 1+i /10, "UAH")

#Input price: 200
# 1.1  кг. коштує -  200.1 UAH
# 1.2  кг. коштує -  200.2 UAH
# 1.3  кг. коштує -  200.3 UAH
# 1.4  кг. коштує -  200.4 UAH
# 1.5  кг. коштує -  200.5 UAH
# 1.6  кг. коштує -  200.6 UAH




# For7. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел
# от A до B включительно.

def for_7():
    a = int(input("Input a: "))
    b = int(input("Input b: "))

    sum = 0

    if a < b:
        for i in range(a,b+1):
            sum = sum + i;
        print(sum)
# Input a: 1
# Input b: 3
# 6

#=================================================================================

# For8. Даны два целых числа A и B (A < B). Найти произведение всех целых
# чисел от A до B включительно.

def for_8():
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    sum = 1

    for i in range(a,b+1):
        sum = sum*i
    print(sum)

#=================================================================================


# For9. Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых
# чисел от A до B включительно.
def for_9():
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    sum = 1

    for i in range(a,b+1):
        sum = i ** 2
    print(sum)



for_9()

