import math
from math import pi
from math import sqrt

"Begin1 ◦ . Дана сторона квадрата a. Найти его периметр P = 4·a."

def begin_1():
    a = float(input("a = "))
    p = 4 * a
    print("p = %5.3f " % p)


#======================================= 2 ==================================================
"Begin2 ◦ . Дана сторона квадрата a. Найти его площадь S = a^2."

def begin_2():
    a = float(input("a = "))
    s = a*a # піднести до степеня...... альтернативна 1 a**2;    альтернатива 2: math.pow(a,2)
    print("s = %5.1f " % s)

#======================================= 3 ==================================================

# Begin3 ◦ . Даны стороны прямоугольника a и b. Найти его площадь S = a·b и
# периметр P = 2·(a + b).

def begin_3 ():

    a = float(input("a = "))
    b = float(input("b = "))
    figure_square = a * b
    perimetr = 2*(a + b)
    print("Find Square", figure_square)
    print("Perimetr of square", perimetr)


#begin_3()

#======================================= 4 ==================================================


# Begin4 ◦ . Дан диаметр окружности d. Найти ее длину L = π·d. В качестве
# значения π использовать 3.14.

def begin_3_or_pi ():

    d = float(input("d = "))
    cirkle_lenth = pi * d #використали модуль math
    print(cirkle_lenth)
    print("Резалт при використанніокругление до ближайшего большего числа.", math.ceil(cirkle_lenth))

#begin_3_or_pi()



#======================================= 5 ==================================================


# Begin5 ◦ . Дана длина ребра куба a. Найти объем куба V = a 3 и площадь его
# поверхности S = 6·a 2 .

def begin_5_rebro_kuba():


    a_rebro= float(input("rebro_kuba="))
    v_cube = a_rebro ** 3 #введення в степінь **
    s_cube = 6 *(a_rebro ** 2)
    print(a_rebro)
    print("v_cub is = ", v_cube)
    print("s_cube is", s_cube)

#begin_5_rebro_kuba()



#======================================= 6 ==================================================


# Begin6 ◦ . Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти
# его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c).

def begin_6_square_side():

    a_side = float(input("a_side is? = "))
    b_side = float(input("b_side is? = "))
    c_side = float(input("c_side is? = "))

    v_square = a_side*b_side*c_side
    s_square = 2 * (a_side*b_side+b_side*c_side+a_side*c_side)

    print("The volme of square is: ",v_square)
    print("The square of square is: ",s_square)


#begin_6_square_side()


#======================================= 7 ==================================================

# Begin7 ◦ . Найти длину окружности L и площадь круга S заданного радиуса R:
# L = 2·π·R,
# S = π·R 2 .

def begin_7_lenth_square_sircle():


    r_radius = float(input("input r_radius= "))
    l_circle = 2 * pi * r_radius
    s_circle = pi * (r_radius ** 2)

    print("initial radius is: ", r_radius)
    print("circle length is: ", l_circle)
    print("square of cirlce is: ", s_circle)

#begin_7_lenth_square_sircle()

#======================================= 8 ==================================================

#Begin8 ◦ . Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2.

def average_arithmetic ():

    a_number = float(input("a number? = "))
    b_number = float(input("b number? = "))

    average_betuw_numbers = (a_number+b_number)/2

    print("average value a, b is: ", average_betuw_numbers)

#average_arithmetic()


#======================================= 9 ==================================================
# Begin9◦
#
# . Даны два неотрицательных числа a и b. Найти их среднее геометри-
# ческое, то есть квадратный корень из их произведения: √
#
# a·b.
# зробити

def begin_9 ():
    a = float(input("a number? = "))
    b = float(input("b number? = "))

    average = sqrt(a*b)
    print(average)

#begin_9()





#======================================= 13 ==================================================


# Begin16◦
# . Найти расстояние между двумя точками с заданными координатами x1 и x2 на числовой оси: |x2 − x1|.
# Begin17◦
# . Даны три точки A, B, C на числовой оси. Найти длины отрезков AC
# и BC и их сумму

def begin_13():
    r1 = float(input("r1? = "))
    r2 = float(input("r2? = "))

    s1 = pi*r1*r1
    s2 = pi*r2*r2
    s3 = abs(s1-s2)

    print("s1 = %5.3f " % s1)
    print("s2 = %5.3f " % s2)
    print("s3 = %5.3f " % s3)

#begin_13()

#======================================= 14 ==================================================

#тут буде задача



#======================================= 18 ==================================================

# Begin18 ◦ . Даны три точки A, B, C на числовой оси. Точка C расположена
# между точками A и B. Найти произведение длин отрезков AC и BC.


def begin_18():
    a = float(input("a? = "))
    b = float(input("b? = "))
    c = float(input("c? = "))

    ac = abs(a-c)
    bc = abs(c-b)
    result_ab_bc = ac * bc

    print("result ab*bc is: ", result_ab_bc)

#begin_18()

#не дуже зрозумів цю задачу

#======================================= 19 ==================================================
# Begin19 ◦ . Даны координаты двух противоположных вершин прямоугольника:
# (x 1 , y 1 ), (x 2 , y 2 ). Стороны прямоугольника параллельны осям координат.
# Найти периметр и площадь данного прямоугольника.

def begin_19():
    x1 = float(input("x1? = "))
    y1 = float(input("y2? = "))
    x2 = float(input("x2? = "))
    y2 = float(input("y2? = "))

    p = abs((x2-x1)+abs(y2-y1))*2
    s = abs((x2-x1)*abs(y2-y1))*2

    print("Peirmetr is:", p)
    print("Square is:", s)

#begin_19()

#нагуглив і адаптував з паскаля


#======================================= 20 ==================================================

# "Begin20 ◦ . Найти расстояние между двумя точками с заданными координатами
# (x 1 , y 1 ) и (x 2 , y 2 ) на плоскости.
# Расстояние вычисляется по формуле
# q
# (x 2 − x 1 ) 2 + (y 2 − y 1 ) 2"

#abs по модулю


def begin_20():
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))

    q = sqrt(pow(x2-x1,2)+ pow(y2-y1,2))
    print("q = ", q)

#begin_20()


#======================================= 21 ==================================================
# Begin21 ◦ . Даны координаты трех вершин треугольника: (x 1 , y 1 ), (x 2 , y 2 ), (x 3 , y 3 ).
# Найти его периметр и площадь, используя формулу для расстояния меж-
# ду двумя точками на плоскости (см. задание Begin20). Для нахождения
# площади треугольника со сторонами a, b, c использовать формулу Герона:
# √
# S = p·(p − a)·(p − b)·(p − c),
#где p = (a + b + c)/2 — полупериметр.

def begin_21():
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    x3 = float(input("x3 = "))
    y3 = float(input("y3 = "))

    q = sqrt(pow(x2-x1,2)+pow(y2-y1,2))+pow(y3-y2,2)+pow(x3-x2,2)
    ab = sqrt(sqrt(x2 - x1) + sqrt(y2 - y1))

    print(ab)
begin_21()

