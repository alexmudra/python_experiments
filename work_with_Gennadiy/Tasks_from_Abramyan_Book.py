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

#======================================= 35 ==================================================

# Begin35◦
# . Скорость лодки в стоячей воде V км/ч, скорость течения реки U км/ч
# (U < V). Время движения лодки по озеру T1 ч, а по реке (против течения)
# — T2 ч. Определить путь S, пройденный лодкой (путь = время · скорость).
# Учесть, что при движении против течения скорость лодки уменьшается
# на величину скорости течения


#======================================= 36 ==================================================
# Begin36◦
# . Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние между ними S км. Определить расстояние между ними через T часов,
# если автомобили удаляются друг от друга. Данное расстояние равно сумме начального расстояния и общего пути, проделанного автомобилями;
# общий путь = время · суммарная скорость.

def begin_36():
    v1_speed = float(input("v1_speed = "))
    v2_speed = float(input("v2_speed = "))

    distance = 5

    all_distance = 60 *(v1_speed+v2_speed)
    print("all_distance", int(all_distance))
    t_hours = distance + all_distance
    print("distance via t hours is:", t_hours)

#begin_36()

#======================================= 9 ==================================================
# Integer9◦
# . Дано трехзначное число. Используя одну операцию деления нацело,
# вывести первую цифру данного числа (сотни).

def integer_9 ():
    int_1 = int(input("our number is = "))
    res = int_1//100
    print("the first numb. is ",res )

#integer_9()

#======================================= 10 ==================================================
# Integer10◦
# . Дано трехзначное число. Вывести вначале его последнюю цифру
# (единицы), а затем — его среднюю цифру (десятки).

def integer_10 ():
    int_1 = int(input("our number is = "))
    res = int_1%10
    res2 = int_1//10
    res3 = res2%10
    print("the last numb. is ",res)
    print("the second numb. is ",res3)

integer_10()