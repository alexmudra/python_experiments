from math import pi
from math import sqrt

"Begin1 ◦ . Дана сторона квадрата a. Найти его периметр P = 4·a."

def begin_1():
    a = float(input("a = "))
    p = 4 * a
    print("p = %5.3f " % p)



"Begin2 ◦ . Дана сторона квадрата a. Найти его площадь S = a^2."

def begin_2():
    a = float(input("a = "))
    s = a*a # піднести до степеня...... альтернативна 1 a**2;    альтернатива 2: math.pow(a,2)
    print("s = %5.1f " % s)



# "Begin20 ◦ . Найти расстояние между двумя точками с заданными координатами
# (x 1 , y 1 ) и (x 2 , y 2 ) на плоскости.
# Расстояние вычисляется по формуле
# q
# (x 2 − x 1 ) 2 + (y 2 − y 1 ) 2"


def begin_20():
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))

    q = sqrt(pow(x2-x1,2)+ pow(y2-y1,2))
    print("q = ", q)

begin_20()

