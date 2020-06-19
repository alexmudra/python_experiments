import math

# #For1. Даны целые числа K и N (N > 0). Вывести N раз число K.


def for_1():
    k = int(input("Input K: "))
    n = int(input("Input N: "))

    for i in range(n):
        print(k)


# Input K: 3
# Input N: 5
# 3
# 3
# 3
# 3
# 3


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
    while True:
        a = int(input("Input a: "))
        b = int(input("Input b: "))

        if a < b:
            for n in range(a, b + 1):
                print(n)
            break  # вихід із циклу while
        else:
            print("Enter a < b")


# For3. Даны два целых числа A и B (A < B). Вывести в порядке убывания все
# целые числа, расположенные между A и B (не включая числа A и B), а
# также количество N этих чисел.


def for_3():
    a = int(input("Input a: "))
    b = int(input("Input b: "))

    if a < b:
        for n in range(b - 1, a, -1):
            print("Numbers is:", n)
        print("Num. q-ty:", b - a - 1)

    else:
        print("Enter a < b")


# For4. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1,
# 2, . . . , 10 кг конфет.


def for_4():
    kandy_price = int(input("Input price: "))

    for i in range(1, 10 + 1):
        sum = kandy_price * i
        print("Total sum for kandy price", i, "is:", sum)


# For5◦. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1,
# 0.2, . . . , 1 кг конфет

def for_5():
    one_kg_price = float(input("Input price: "))
    weight = 0.1
    for i in range(100):
        cost = one_kg_price * weight
        print("%7.3f" % weight, ' кг. коштує - ', "%7.2f" % cost, "UAH")
        weight += 0.1


# or6. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1.2,
# 1.4, . . . , 2 кг конфет.


def for_6():
    one_kg_price = float(input("Input price: "))

    weight = 1.2
    for i in range(5):
        cost = one_kg_price * weight
        print("%7.3f" % weight, ' кг. коштує - ', "%7.2f" % cost, "UAH")
        weight += 0.2


# Input price: 2
#   1.200  кг. коштує -     2.40 UAH
#   1.400  кг. коштує -     2.80 UAH
#   1.600  кг. коштує -     3.20 UAH
#   1.800  кг. коштує -     3.60 UAH
#   2.000  кг. коштує -     4.00 UAH

# =================================================================================


# For7. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел
# от A до B включительно.

def for_7():
    a = int(input("Input a: "))
    b = int(input("Input b: "))

    sum = 0

    for i in range(a, b + 1):
        sum = sum + i;
    print(sum)


# Input a: 1
# Input b: 3
# 6

# =================================================================================

# For8. Даны два целых числа A и B (A < B). Найти произведение всех целых
# чисел от A до B включительно.

def for_8():
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    product = 1

    for i in range(a, b + 1):
        product = product * i
    print(product)


# =================================================================================


# For9. Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых
# чисел от A до B включительно.
def for_9():
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    sum = 0

    for i in range(a, b + 1):
        sum += i ** 2
    print(sum)


# =================================================================================


# For10. Дано целое число N (> 0). Найти сумму 1 + 1/2 + 1/3 + … + 1/N (вещественное число).

def for_10():
    n = int(input("Input n: "))
    result = 0

    for i in range(1, n + 1):
        result = result + 1 / i

    print(result)


# =================================================================================
# For11. Дано целое число N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 +…+ (2*N)2 (целое число).

def for_11():
    n = int(input("Input n: "))
    result = 0

    for i in range(n + 1):
        result = result + (n + i) ** 2
    print(result)


# =================================================================================

# For12 ◦ . Дано целое число N (> 0). Найти произведение
# 1.1 · 1.2 · 1.3 · . . .(N сомножителей).

def for_12():
    n = int(input("Input n: "))  # отримати вхідні дані

    product = 1  # розрахунки
    x = 1.1
    for i in range(n):
        product *= x
        x += 0.1

    print(product)  # виведення результатів


# =================================================================================

# For13 ◦ . Дано целое число N (> 0). Найти значение выражения
# 1.1 − 1.2 + 1.3 − . . .
# (N слагаемых, знаки чередуются). Условный оператор не использовать.

def for_13():
    n = int(input("Input n: "))  # отримати вхідні дані

    sum = 0  # розрахунки
    x = 1.1
    sign = 1
    for i in range(n):
        sum += x * sign
        sign = -sign  # так здобуваємо чергування + -
        x += 0.1

    print(sum)  # виведення результатів


# =================================================================================

# For14. Дано целое число N (> 0). Найти квадрат данного числа, используя для
# его вычисления следующую формулу:
# N^2= 1 + 3 + 5 + . . . + (2·N − 1).
# После добавления к сумме каждого слагаемого выводить текущее значе-
# ние суммы (в результате будут выведены квадраты всех целых чисел от 1
# до N).

def for_14():
    n = int(input("Input n: "))  # отримати вхідні дані

    result = 0
    x = 1
    for i in range (1, n+1):
        result = result +x
        x = x + 2
        print("i value is:", i,"and resalt is:", result)

#==========================================================================

# For15 ◦ . Дано вещественное число A и целое число N (> 0). Найти A в степе-
# ни N:
# A^N = A·A· . . . ·A
# (числа A перемножаются N раз).

def for_15():
    a = int(input("Input a: "))  # отримати вхідні дані
    n = int(input("Input n: "))  # степінь

    res = 1
    for i in range(n):
        res = res * a
    print(res)

#==========================================================================


# For16 ◦ . Дано вещественное число A и целое число N (> 0). Используя один
# цикл, вывести все целые степени числа A от 1 до N.

def for_16():
    a = int(input("Input a: "))  # отримати вхідні дані
    n = int(input("Input n: "))  # отримати вхідні дані

    res = 1
    for i in range(n+1):
        print(a, "в степені", i, "дорівнює", res)
        res *= a

# Input a: 2
# Input n: 5
# 2 в степені 0 дорівнює 1
# 2 в степені 1 дорівнює 2
# 2 в степені 2 дорівнює 4
# 2 в степені 3 дорівнює 8
# 2 в степені 4 дорівнює 16
# 2 в степені 5 дорівнює 32

#==========================================================================

# For17. Дано вещественное число A и целое число N (> 0). Используя один
# цикл, найти сумму
# 1 + A + A 2 + A 3 + . . . + A N .

def for_17():
    a = int(input("Input a: "))  # отримати вхідні дані
    n = int(input("Input n: "))  # отримати вхідні дані

    summ = 0
    for i in range(n+1):
        summ += a**i

    print(summ)

#for_17()

# #Input a: 2
# Input n: 3
# 15

def for_17a():
    a = int(input("Input a: "))  # отримати вхідні дані
    n = int(input("Input n: "))  # отримати вхідні дані

    summ = 0
    a_in_pow = 1 #для того щоб перезаписувати сюди степінь
    for i in range(n+1):
        summ += a_in_pow
        a_in_pow *=a #наступний степіль а

    print(summ)

#for_17a()


# Input a: 2
# Input n: 3
# 15

#==========================================================================

# For18. Дано вещественное число A и целое число N (> 0). Используя один
# цикл, найти значение выражения
# 1 − A + A 2 − A 3 + . . . + (−1) N ·A N .
# Условный оператор не использовать.


def for_18():
    a = int(input("Input a: "))  # отримати вхідні дані
    n = int(input("Input n: "))  # отримати вхідні дані

    summ = 0
    sign = 1

    a_in_pow = 1 #для того щоб перезаписувати сюди степінь
    for i in range(n+1):
        summ += a_in_pow*sign
        a_in_pow *=a #наступний степіль а
        sign = -sign

    print(summ)

#for_18()

# #Input a: 2
# Input n: 3
# -5


#==========================================================================
# For19 ◦ . Дано целое число N (> 0). Найти произведение
# N! = 1·2·. . .·N
# (N–факториал). Чтобы избежать целочисленного переполнения, вычис-
# лять это произведение с помощью вещественной переменной и вывести
# его как вещественное число


def for_19():
    n = int(input("Input n: "))  # отримати вхідні дані
    fact = 1
    for i in range(1,n+1):
        fact *=i
    print(fact)

#for_19()


#==========================================================================
 
# For20 ◦ . Дано целое число N (> 0). Используя один цикл, найти сумму
# 1! + 2! + 3! + . . . + N!
# (выражение N! — N–факториал — обозначает произведение всех целых
# чисел от 1 до N: N! = 1·2·. . .·N). Чтобы избежать целочисленного пере-
# полнения, проводить вычисления с помощью вещественных переменных
# и вывести результат как вещественное число.


def for_20():
    n = int(input("Input n: "))  # отримати вхідні дані
    fact = 1
    summ = 0

    for i in range(1, n + 1):
        fact *= i
        summ +=fact
    print(summ)
#Input n: 5
#153

#==========================================================================
# For21. Дано целое число N (> 0). Используя один цикл, найти сумму
# 1/(0!) + 1/(1!) + 1/(2!) + 1/(3!) + . . . + 1/(N!)
# (выражение N! — N–факториал — обозначает произведение всех целых
# чисел от 1 до N: N! = 1·2·. . .·N). Полученное число является прибли-
# женным значением константы e = exp(1).

def for_21():

    n = int(input("Input n: "))  # отримати вхідні дані
    fact = 1
    summ = 0

    for i in range(1,n + 1):
        summ +=1/fact
        fact *= i
    print(summ)
    print(math.exp(1))#перевірка значення константи експоненти


#for_21()
#Input n: 50
#2.7182818284590455
#2.718281828459045

#==========================================================================

# For22. Дано вещественное число X и целое число N (> 0). Найти значение
# выражения
# 1 + X + X 2 /(2!) + . . . + X N /(N!)
# (N! = 1·2·. . .·N). Полученное число является приближенным значением
# функции exp в точке X.

def for_22():

    x = float(input("Input x: "))  # отримати вхідні дані f
    n = int(input("Input n: "))  # отримати вхідні дані n

    summ = 0
    fact = 1
    x_val = 1


    for i in range(1, n + 1):
        n_fact = i*n
        summ = (x_val +(x**x))/(2/fact)
    print(n_fact)
    print(summ)

for_22()































# For23. Дано вещественное число X и целое число N (> 0). Найти значение
# выражения
# X − X 3 /(3!) + X 5 /(5!) − . . . + (−1) N ·X 2·N +1 /((2·N+1)!)
# (N! = 1·2·. . .·N). Полученное число является приближенным значением
# функции sin в точке X.
# For24. Дано вещественное число X и целое число N (> 0). Найти значение
# выражения
# 1 − X 2 /(2!) + X 4 /(4!) − . . . + (−1) N ·X 2·N /((2·N)!)
# (N! = 1·2·. . .·N). Полученное число является приближенным значением
# функции cos в точке X.
# For25. Дано вещественное число X (|X | < 1) и целое число N (> 0). Найти
# значение выражения
# X − X 2 /2 + X 3 /3 − . . . + (−1) N −1 ·X N /N.
# Полученное число является приближенным значением функции ln в точ-
# ке 1 + X.