import math


#  Дано целое число. Если оно является положительным, то прибавить к
# нему 1; в противном случае не изменять его. Вывести полученное число.
from typing import Any, Union


def if_1():
    x = int(input("x1? = "))

    if x > 0:
        x = x+1

    print(x)


#if_1()

#If2. Дано целое число. Если оно является положительным, то прибавить к
#нему 1; в противном случае вычесть из него 2. Вывести полученное число.

def if_2():
    x = int(input("x? = "))

    if x > 0:
        x = x + 1
    else:
        x = x - 2

    print(x)

#if_2()

# If3. Дано целое число. Если оно является положительным, то прибавить к
# нему 1; если отрицательным, то вычесть из него 2; если нулевым, то
# заменить его на 10. Вывести полученное число.


def if_3():
    x = int(input("x? = "))

    if x > 0:
        x = x + 1
    elif x < 0:
        x = x - 2
    else:
        x = 10

    print("x =", x)

#if_3()


# If4◦
# . Даны три целых числа. Найти количество положительных чисел в исходном наборе.

def if_4():
    x_1 = int(input("x1? = "))
    x_2 = int(input("x2? = "))
    x_3 = int(input("x?3 = "))

    cnt = 0

    if x_1 > 0: cnt += 1 #коли багато if і в кожному із них лище одна команда можна робити таким чином:
    if x_2 > 0: cnt += 1
    if x_3 > 0: cnt += 1

    print(cnt)

#if_4()


# If5. Даны три целых числа. Найти количество положительных и количество
# отрицательных чисел в исходном наборе.

def if_5():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    cnt = 0
    cnt_1 = 0

    if a > 0:
        cnt +=1
    else:
        cnt_1 =cnt_1+1
    if b > 0:
        cnt +=1
    else:
        cnt_1 =cnt_1+1
    if c > 0:
        cnt +=1
    else:
        cnt_1 =cnt_1+1


    print("positive numbers:", cnt, "negative n.:", cnt_1)

#if_5()



# If6◦
# . Даны два числа. Вывести большее из них.
def if_6():
    a = int(input("a? = "))
    b = int(input("b? = "))

    max_x = a # це гіпотеза
    if b > max_x: #а тепер перевірка гіпотези
        max_x = b

    print(max_x)

def if_6a(): #ще одне рішення
    a = int(input("a? = "))
    b = int(input("b? = "))

    if a > b:
        max_x = a
    else:
        max_x = b

    print(max_x)

# If7. Даны два числа. Вывести порядковый номер меньшего из них.

def if_7():
    a = int(input("a? = "))
    b = int(input("b? = "))

    number = 1
    if b < a:
        number = 2

    print(number)
#if_7()


# If8◦
# . Даны два числа. Вывести вначале большее, а затем меньшее из них.

def if_8():
    a = int(input("a? = "))
    b = int(input("b? = "))

    maxx = a
    minx = b
    if a < b:
        minx = a
        maxx = b

    print(maxx, minx)

#if_8 ()


def if_8a():
    a = int(input("a? = "))
    b = int(input("b? = "))


    if a < b:
        minx = a
        maxx = b
    else:
        minx = b
        maxx = a

    print(maxx, minx)

#if_8a ()



# If9. Даны две переменные вещественного типа: A, B. Перераспределить значения данных переменных так,
# чтобы в A оказалось меньшее из значений,
# а в B — большее. Вывести новые значения переменных A и B.

def if_9():
    a = int(input("a? = "))
    b = int(input("b? = "))

    if a > b:
        a,b = b, a
    print(a, b)

#if_9()


# If10. Даны две переменные целого типа: A и B. Если их значения не равны,
# то присвоить каждой переменной сумму этих значений, а если равны,
# то присвоить переменным нулевые значения. Вывести новые значения
# переменных A и B.

def if_10():
    a = int(input("a? = "))
    b = int(input("b? = "))

    if a != b:
        summ = a + b
        a = summ
        b = summ
    else:
        a = b = 0 #так писати присвоєння багатьом перемінним

    print(a, b)

#if_10()


# If11. Даны две переменные целого типа: A и B. Если их значения не равны, то
# присвоить каждой переменной большее из этих значений, а если равны,
# то присвоить переменным нулевые значения. Вывести новые значения
# переменных A и B


def if_11():
    a = int(input("a? = "))
    b = int(input("b? = "))

    if a != b:
        if a > b:
            b = a
        else:
            a = b
    else:
        a = b = 0

    print(a, b)

#if_11()


#If12◦
# . Даны три числа. Найти наименьшее из них.

def if_12():
    a = int(input("a? = "))
    b = int(input("b? = "))
    c = int(input("c? = "))

    # if a < b and a < c:
    #     print(a)
    # if b < a and b < c:
    #     print(b)
    # if c < a and c < a:
    #     print(c)

    minn = a
    if b < minn:
        minn = b
    if c < minn:
        minn = c

    print(minn)


#if_12()


# If13. Даны три числа. Найти среднее из них (то есть число, расположенное
# между наименьшим и наибольшим).

def if_13():
    a = int(input("a? = "))
    b = int(input("b? = "))
    c = int(input("c? = "))

    # if a < b and a < c and b < c:
    #     print(b)
    # if b < a and b < c and a < c:
    #     print(c)
    # if c < a and c < b and a < b:
    #     print(a)

    middle = a
    if a < b and b < c or c < b and b < a:
        middle = b
    if a < c and c < b or b < c and c < a:
        middle = c

    print(middle)

#if_13()


def if_13_a():
    a = int(input("a? = "))
    b = int(input("b? = "))
    c = int(input("c? = "))

    #спробуємо виконати задачу через пошук мінімального і макс. елементу

    min_el = a
    if b < min_el:
        min_el = b
    if c < min_el:
        min_el = c

    max_el = a
    if b > max_el:
        max_el = b
    if c > max_el:
        max_el = c

    middle = a + b + c - min_el - max_el
    print(middle)

#if_13_a()



# If14. Даны три числа. Вывести вначале наименьшее, а затем наибольшее из
# данных чисел.
def if_14():
    a = int(input("a? = "))
    b = int(input("b? = "))
    c = int(input("c? = "))

    min_el = a
    if b < min_el:
        min_el = b
    if c < min_el:
        min_el = c

    max_el = a
    if b > max_el:
        max_el = b
    if c > max_el:
        max_el = c

    print(min_el, max_el)

#if_14()


# If15. Даны три числа. Найти сумму двух наибольших из них.

def if_15():
    a = int(input("a? = "))
    b = int(input("b? = "))
    c = int(input("c? = "))

    min_el = a
    if b < min_el:
        min_el = b
    if c < min_el:
        min_el = c

    max_el = a
    if b > max_el:
        max_el = b
    if c > max_el:
        max_el = c

    middle = a + b + c - min_el - max_el
    summ = max_el+middle

    print(summ)

#if_15()

def if_15a():
    a = int(input("a? = "))
    b = int(input("b? = "))
    c = int(input("c? = "))

    middle = a
    if b > middle and middle < c:
        middle = b
    if c < middle and c > b:
        middle = c

    max_el = a
    if b > max_el:
        max_el = b
    if c > max_el:
        max_el = c

    summ = max_el + middle

    print(summ)

#if_15a()

# If16. Даны три переменные вещественного типа: A, B, C. Если их значения
# упорядочены по возрастанию, то удвоить их; в противном случае заменить значение каждой переменной на противоположное.
# Вывести новые значения переменных A, B, C.

def if_16():
    a = int(input("a? = "))
    b = int(input("b? = "))
    c = int(input("c? = "))

    if a < b and b < c:
        a += a
        b += b
        c += c
    else:
        a = -a
        b = -b
        c = -c

    print(a , b, c)

#if_16()


# If17. Даны три переменные вещественного типа: A, B, C. Если их значения
# упорядочены по возрастанию или убыванию, то удвоить их; в противном случае заменить значение каждой переменной на противоположное.
# Вывести новые значения переменных A, B, C.

def if_17():
    a = float(input("a? = "))
    b = float(input("b? = "))
    c = float(input("c? = "))

    if a < b and b < c:
        a += a
        c += c
        b += b
    else:
        a = -a
        b = -b
        c = -c

    print(a , b, c)

# If18. Даны три целых числа, одно из которых отлично от двух других, равных между собой. Определить порядковый номер числа, отличного от
# остальных.

def if_18():
    a = int(input("a? = "))
    b = int(input("b? = "))
    c = int(input("c? = "))

    number = 1 #припускаємо що a це є відмінне число і порівнюємо з ним

    if a == c:
        number = 2
    if a == b:
        number = 3

    print(number)

#if_18()



# If19. Даны четыре целых числа, одно из которых отлично от трех других,
# равных между собой. Определить порядковый номер числа, отличного от
# остальных.

def if_19():
    a = float(input("a? = "))
    b = float(input("b? = "))
    c = float(input("c? = "))
    d = float(input("d? = "))

    number = 1

    if a == b:
        number = 2
    if a == c:
        number = 3
    if a == d:
        number = 4

    print(number)

#if_19()


# If20. На числовой оси расположены три точки: A, B, C. Определить, какая из
# двух последних точек (B или C) расположена ближе к A, и вывести эту
# точку и ее расстояние от точки A.

def if_20():
    a = float(input("a? = "))
    b = float(input("b? = "))
    c = float(input("c? = "))

    ab = abs(b - a) # беремо за модулем бо точно не знаємо яке число буде з мінусом
    ac = abs(c - a)

    if ab < ac:
        print("b is closer than a/c")
        print("distance is ab", ab)
    else:
        print("c is closer than a/b")
        print("distance is ac", ac)

#if_20()


# If21. Даны целочисленные координаты точки на плоскости. Если точка совпадает с началом координат, то вывести 0.
# Если точка не совпадает с началом координат, но лежит на оси OX или OY, то вывести соответственно 1
# или 2. Если точка не лежит на координатных осях, то вывести 3.


def if_21():
    x = float(input("x? = "))
    y = float(input("y? = "))

    answer = 3
    if x == 0 and y == 0:
        answer = 0
    if x == 0 and y != 0:
        answer = 1
    if x !=0 and y == 0:
        answer = 2

    print(answer)

#if_21()


# If22◦
# . Даны координаты точки, не лежащей на координатных осях OX и OY.
# Определить номер координатной четверти, в которой находится данная
# точка.

def if_22():
    x = float(input("x? = "))
    y = float(input("y? = "))

    answer = 0
    if x > 0 and y > 0:
        answer = 1
    if x < 0 and y > 0:
        answer = 2
    if x < 0 and y < 0:
        answer = 3
    if x > 0 and y < 0:
        answer = 4

    print(answer)

#if_22()



# If23. Даны целочисленные координаты трех вершин прямоугольника, стороны
# которого параллельны координатным осям. Найти координаты его четвертой вершины.

def if_23():
    x1 = float(input("x1? = "))
    y1 = float(input("y1? = "))
    x2 = float(input("x2? = "))
    y2 = float(input("y2? = "))
    x3 = float(input("x3? = "))
    y3 = float(input("y3? = "))

    x4 = x1 #припущення/гіпотеза
    #а далі перевірки чи є пара у х
    if x1 == x3:
        x4 = x2
    if x1 == x2:
        x4 = x3

    y4 = y1
    if y1 == y3:
        y4 = y2
    if y1 == y2:
        y4 = y3

    print("x4, y4 coordinates is:", x4,y4)

#if_23()


# If24. Для данного вещественного x найти значение следующей функции f,
# принимающей вещественные значения:
# f (x) = 2·sin(x), если x > 0,
# 6 − x, если x ≤ 0

def if_24():
    x = float(input("x? = "))

    fx = 6-x
    if x > 0:
        fx = math.sin(x) * 2


    print("function f is:", fx)

#if_24()


# If25. Для данного целого x найти значение следующей функции f, принимающей значения целого типа:
# f (x) = 2·x, если x < −2 или x > 2,
# −3·x, в противном случае.

def if_25():
    x = int(input("x? = "))

    fx = -3 * x
    if x < -2 or x > 2:
        fx = 2 * x

    print("25 fx is:", fx)

#if_25()

# Для данного вещественного x найти значение следующей функции f,
# принимающей вещественные значения:
# −x, если x ≤ 0,
# f (x) = x
# 2
# , если 0 < x < 2,
# 4, если x ≥ 2.

def if_26():
    x = float(input("x? = "))

    fx = x*x
    if x <= 0:
        fx = -x
    if x >= 2:
        fx = 4

    print("26 ex is:", fx)

#if_26()


# If27. Для данного вещественного x найти значение следующей функции f,
# принимающей значения целого типа:
# 0, если x < 0,
# f (x) = 1, если x принадлежит [0, 1), [2, 3), . . . ,
# −1, если x принадлежит [1, 2), [3, 4), . . .

def if_27():
    x = float(input("x? = "))

    fx = 0
    if x >= 0:
        y = int(x)
        fx = 1
        if y % 2 != 0:
            fx = -1

    print('Значение функции f= ', fx)

#if_27()

#===============[0, 1), [2, 3), . . . ,  хочу знати детальніше?

# If28. Дан номер года (положительное целое число). Определить количество
# дней в этом году, учитывая, что обычный год насчитывает 365 дней, а
# високосный — 366 дней. Високосным считается год, делящийся на 4, за
# исключением тех годов, которые делятся на 100 и не делятся на 400
# (например, годы 300, 1300 и 1900 не являются високосными, а 1200 и 2000
# — являются).

def if_28():
    year = int(input("Year = "))

    days = 365
    if year % 4 == 0:
        days = 366
        if year % 100 == 0 and year % 400 != 0:
            days = 365

    print(days)

#if_28()



# If29. Дано целое число. Вывести его строку-описание вида «отрицательное
# четное число», «нулевое число», «положительное нечетное число» и т. д.

def if_29():
    x = int(input("x? = "))

    answer = "нульове "
    if x < 0:
        answer = "videmne "
    if x > 0:
        answer = "dodatne "

    if x % 2 == 0:
        answer += "parne "
    else:
        answer += "ne parne "

    answer += "chislo"

    print(answer)

#if_29()



# f30. Дано целое число, лежащее в диапазоне 1–999.
# Вывести его строкуописание вида «четное двузначное число», «нечетное трехзначное число»
# и т. д.


def if_30():
    x = int(input("x in range 1-1999? = "))

    if x % 2 == 0:
        answer = " parne"
    else:
        answer = "ne parne"

    if x > 1 and x <= 99:
        answer += " dvoznachne"
    if x >=100 and x <= 999:
        answer += " trohznachne"
    if x >= 1000 and x <=1999:
        answer += " chotiriohnachne"

    answer += " chislo"



    print(answer)

if_30()








