import math
from math import pi
from math import sqrt
from math import radians
from math import degrees



#"Begin1 ◦ . Дана сторона квадрата a. Найти его периметр P = 4·a."

def begin_1():
    a = float(input("a = "))
    p = 4 * a
    print("p = %5.3f " % p)


#======================================= 2 ==================================================
#"Begin2 ◦ . Дана сторона квадрата a. Найти его площадь S = a^2."

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

    a = sqrt(pow(x2-x1,2)+pow(y2-y1,2)) #взнаємо відстань від вершини до вершини, що і є сторона трикутника
    b = sqrt(pow(x3-x2,2)+pow(y3-y2,2))
    c = sqrt(pow(x1-x3,2)+pow(y1-y3,2))

    p = (a+b+c)/2 #взнаємо полупериметрт
    s = sqrt(p*(p-a)*(p-b)*(p-c)) #знахоимо плошу за формулою Герона


    print("a is: ", a)
    print("b is: ", b)
    print("c is: ", c)
    print("p is: ", p)
    print("s is: ", s)

#begin_21()


#======================================= 22 ==================================================
# Begin22 ◦ . Поменять местами содержимое переменных A и B и вывести новые
# значения A и B


def begin_22():
    a = float(input("a = "))
    b = float(input("b = "))

    a = b

    print("a is b", a)

#begin_22()

#======================================= 23 ==================================================

# Begin23 ◦ . Даны переменные A, B, C. Изменить их значения, переместив содер-
# жимое A в B, B — в C, C — в A, и вывести новые значения переменных A,
# B, C.


def begin_23():

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    tmp = a

    a = b
    b = c
    c = tmp

    print("a is b", a)
    print("b is c", b)
    print("c is a", c)



#begin_23()


#======================================= 24 ==================================================

# Begin24 ◦ . Даны переменные A, B, C. Изменить их значения, переместив содер-
# жимое A в C, C — в B, B — в A, и вывести новые значения переменных A,
# B, C.

def begin_24():

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    tmpA = a
    tmpB = b
    tmpC = c

    c = a
    b = tmpC
    a = tmpB


    print("a to c",c)
    print("c to b",b)
    print("b to a",a)



#begin_24()




#======================================= 25 ==================================================


#Найти значение функции y = 3x 6 − 6x 2 − 7 при данном значении x.

def begin_25():

    x = float(input("x = "))

    y = 3*x**6 - 6*x**2 - 7

    print("res is: ", y)


#begin_25()

#======================================= 26 ==================================================
# Begin26 ◦ . Найти значение функции y = 4(x−3) 6 − 7(x−3) 3 + 2 при данном
# значении x


def begin_26():

    x = float(input("x = "))

    y = 4*(x-3)**6 - 7*(x-3)**3+2
    z = 4*pow(x-3,6)- 7*pow(x-3,3)+2


    print("res of task 26 is: ", y)
    print("res of task 26 is: ", z)

#begin_26()


#======================================= 27 ==================================================
# Begin27 ◦ . Дано число A. Вычислить A 8 , используя вспомогательную перемен-
# ную и три операции умножения. Для этого последовательно находить A 2 ,
# A 4 , A 8 . Вывести все найденные степени числа A.

def begin_27():

    a = float(input("a = "))

    b = a * a
    print("a ^ 2 ", b)
    b = b * b
    print("a ^ 4 ", b)
    b = b * b
    print("a ^ 8 ", b)

#begin_27()


#======================================= 28 ==================================================
# Begin28 ◦ . Дано число A. Вычислить A 15 , используя две вспомогательные пере-Ввод и вывод данных, оператор присваивания
# 13
# менные и пять операций умножения. Для этого последовательно находить
# A 2 , A 3 , A 5 , A 10 , A 15 . Вывести все найденные степени числа A.

def begin_28():

    a = float(input("a = "))

    b = a * a
    print("a ^ 2: ", b)

    c = b * a
    print("a ^ 3:", c)

    b = c * b
    print("a ^ 5:", b)

    c = b * b
    print("c ^ 10:", c)

    c = b * c
    print("a ^ 15", c)


#begin_28()

#======================================= 29 ==================================================
# Begin29 ◦ . Дано значение угла α в градусах (0 < α < 360). Определить значение
# этого же угла в радианах, учитывая, что 180 ◦ = π радианов. В качестве
# значения π использовать 3.14.


def begin_29():

    a = float(input("a = "))
    print(radians(a)) #використали інбілдмодуль

#begin_29()

#======================================= 30 ==================================================
# Begin30 ◦ . Дано значение угла α в радианах (0 < α < 2·π). Определить значение
# этого же угла в градусах, учитывая, что 180 ◦ = π радианов. В качестве
# значения π использовать 3.14.

def begin_30():

    a_radian = float(input("a = "))

    conv = a_radian*180/pi
    print(degrees(a_radian))
    print(conv)

#begin_30()


#======================================= 31 ==================================================
# Begin31 ◦ . Дано значение температуры T в градусах Фаренгейта. Определить
# значение этой же температуры в градусах Цельсия. Температура по Цель-
# сию T C и температура по Фаренгейту T F связаны следующим соотношением:
# T C = (T F − 32)·5/9.

def begin_31():

    t_far = float(input("a = "))

    t_cels_is = (t_far-32)*(5/9)
    print(t_cels_is)

#begin_31()

#======================================= 32 ==================================================

# Begin32 . Дано значение температуры T в градусах Цельсия. Определить зна-
# чение этой же температуры в градусах Фаренгейта. Температура по Цель-
# сию T C и температура по Фаренгейту T F связаны следующим соотноше-
# нием:
# T C = (T F − 32)·5/9.

def begin_32():

    cels = float(input("a = "))

    t_far_is=9/5*cels+32 # треба пояснення стосовно цього
    print(t_far_is)

#begin_32()

#======================================= 33 ==================================================

# Begin33 . Известно, что X кг конфет стоит A рублей. Определить, сколько
# стоит 1 кг и Y кг этих же конфет.

def begin_33():

    candies_kg = float(input("candies kg = "))
    cost = float(input("cost = "))


    one_kg_price = cost/ candies_kg


    print(one_kg_price)

    next_kg = float(input("next kg = "))

    next_cost = next_kg * one_kg_price
    print("next cost is: ", next_cost)

#begin_33()

#======================================= 34 ==================================================
# Begin34 ◦ . Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ири-
# сок стоит B рублей. Определить, сколько стоит 1 кг шоколадных конфет,
# 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок.

def begin_34():

    x = float(input("x is: ")) # Известно, что X кг
    x_cost = float(input("x_cost is: ")) #шоколадных конфет стоит A рублей,
    y = float(input("y is: ")) # а Y кг ириcjr
    y_cost = float(input("y_cost is: "))  # стоит B рублей.


    one_kg_x_prince = x_cost/x
    print(one_kg_x_prince)

    one_kg_y_price = y_cost/y
    print(one_kg_y_price)

    differ_price = int((x_cost/y_cost*0.01)*100) #визначаємо різницю в разах
    print(differ_price)

#begin_34()

#======================================= 35 ==================================================

# Begin35 ◦ . Скорость лодки в стоячей воде V км/ч, скорость течения реки U км/ч
# (U < V ). Время движения лодки по озеру T 1 ч, а по реке (против течения)
# — T 2 ч. Определить путь S, пройденный лодкой (путь = время · скорость).
# Учесть, что при движении против течения скорость лодки уменьшается
# на величину скорости течения.

def begin_35():

    v = float(input("boat speed in no flow is: "))
    u = float(input("river flow speed is: "))

    time_one_speed_lake = float(input("time lake speed is: "))
    time_two_speed_river = float(input("time river speed is: "))

    s_in_lake = time_one_speed_lake * v
    s_in_river = time_two_speed_river * u

    s = v * time_one_speed_lake+(v-u)*time_two_speed_river



    print("s in lake", s_in_lake, "km")
    print("s in river", s_in_river, "km")
    print("s difference", s,"km")

#begin_35()

# Begin36◦
# . Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние между ними S км. Определить расстояние между ними через T часов,
# если автомобили удаляются друг от друга. Данное расстояние равно сумме начального расстояния и общего пути, проделанного автомобилями;
# общий путь = время · суммарная скорость.


#======================================= 36 ==================================================
def begin_36():
    v1_speed = float(input("v1_speed = "))
    v2_speed = float(input("v2_speed = "))
    t = float(input("t = "))

    distance = 5
    s1 = v1_speed * t
    s2 = v2_speed * t

    s = distance + s1 +s2

    print(s)

#begin_36()


#======================================= 37 ==================================================


# Begin37 ◦ . Скорость первого автомобиля V 1 км/ч, второго — V 2 км/ч, расстоя-
# ние между ними S км. Определить расстояние между ними через T часов,

# если автомобили первоначально движутся навстречу друг другу. Данное14
# расстояние равно модулю разности начального расстояния и общего пути,
# проделанного автомобилями; общий путь = время · суммарная скорость.


def begin_37():
    v1_speed = float(input("v1_speed = "))
    v2_speed = float(input("v2_speed = "))
    t = float(input("t = "))

    distance = 5
    s1 = v1_speed * t
    s2 = v2_speed * t

    s = abs(distance - s1 - s2)


    print(s)

#begin_37()

#======================================= 38 ==================================================


# Begin38 ◦ . Решить линейное уравнение A·x + B = 0, заданное своими коэффи-
# циентами A и B (коэффициент A не равен 0)


def begin_38 ():
    a = float(input("a = "))
    b = float(input("b = "))

    #A·x + B -b  = 0 - b знищуємо б
    #ax = -b знищуємо а
    #ax/a = -b/a додаємо а для знишення(ділимо на а обидві половини...)

    x = -b/a

    print(x)

#begin_38()


#======================================= 39 ==================================================

# Begin39 ◦ . Найти корни квадратного уравнения A·x 2 + B·x + C = 0, задан-
# ного своими коэффициентами A, B, C (коэффициент A не равен 0), ес-
# ли известно, что дискриминант уравнения положителен. Вывести внача-
# ле меньший, а затем больший из найденных корней. Корни квадратного
# уравнения находятся по формуле
# √
# x 1, 2 = (−B ± D)/(2·A),
# где D — дискриминант, равный B 2 − 4·A·C.


def begin_39 ():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    d = b*b - 4 *a*c

    x1 = (-b+sqrt(d))/(2*a)
    x2 = (-b-sqrt(d))/(2*a)

    print(d, x1, x2)

#begin_39()


#======================================= 40 ==================================================


# Begin40 ◦ . Найти решение системы линейных уравнений вида
# A 1 ·x + B 1 ·y = C 1 ,
# A 2 ·x + B 2 ·y = C 2 ,
# заданной своими коэффициентами A 1 , B 1 , C 1 , A 2 , B 2 , C 2 , если известно,
# что данная система имеет единственное решение. Воспользоваться фор-
# мулами
# x = (C 1 ·B 2 − C 2 ·B 1 )/D,
# y = (A 1 ·C 2 − A 2 ·C 1 )/D,
# где D = A 1 ·B 2 − A 2 ·B 1 .


def begin_40 ():
    a1 = float(input("a1 = "))
    b1 = float(input("b1 = "))
    c1 = float(input("c1 = "))
    a2 = float(input("a2 = "))
    b2 = float(input("b2 = "))
    c2 = float(input("c2 = "))

    d = a1*b2 - a2*b1
    x = (c1*b2 - c2*b1)/d
    y = (a1*c2 - a2*c1)/d

    z = a1*x+b1*y
    g = a2*x+b2*y

    print(d)
    print(x)
    print(y)
    print(z)
    print(g)


#begin_40()
