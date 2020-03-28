
#======================================= Логические выражения ==================================================

# Логические выражения
# Во всех заданиях данной группы требуется вывести логическое значение
# TRUE, если приведенное высказывание для предложенных исходных данных
# является истинным, и значение FALSE в противном случае.
# Все числа, для которых указано количество цифр (двузначное число, трехзначное число и т. д.),
# считаются целыми положительными.

#======================================= boolean1 ==================================================

# Boolean1◦
# . Дано целое число A. Проверить истинность высказывания: «Число A является положительным».

def bool_1():
    a = int(input("input a: "))

    ok = a > 0

    print(ok)

#bool_1()

#======================================= boolean2 ==================================================
#
# Boolean2◦
# . Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».

def bool_2():
    a = int(input("input a: "))

    ok = a % 2 != 0

    print(ok)

#bool_2()

#======================================= boolean3 ==================================================

# Boolean3◦
# . Дано целое число A. Проверить истинность высказывания: «Число A является четным».


#======================================= boolean4 ==================================================
# Boolean4◦
# . Даны два целых числа: A, B. Проверить истинность высказывания:
# «Справедливы неравенства A > 2 и B ≤ 3»

def bool_4():
    a = int(input("input a: "))
    b = int(input("input b: "))

    ok = a > 2 and b <= 3

    print(ok)

#bool_4()

#======================================= boolean5 ==================================================
# Boolean5◦
# . Даны два целых числа: A, B. Проверить истинность высказывания:
# «Справедливы неравенства A ≥ 0 или B < −2».

def bool_5():
    a = int(input("input a: "))
    b = int(input("input b: "))

    ok = a >= 0 or b < -2

    print(ok)

#bool_5()

#======================================= boolean6 ==================================================
# Boolean6◦
# . Даны три целых числа: A, B, C. Проверить истинность высказывания: «Справедливо двойное неравенство A < B < C».

def bool_6():
    a = int(input("input a: "))
    b = int(input("input b: "))
    c = int(input("input c: "))

    ok = a < b < c # тільки на пайтоні можна так писати (в усіх інших мовах буде помилка н-д: c, c++, c-sharp)
    ok = a < b and b < c #рівнозначний

    print(ok)

#bool_6()


#======================================= boolean7 ==================================================
# Boolean7◦
# . Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B находится между числами A и C».
def bool_7():
    a = int(input("input a: "))
    b = int(input("input b: "))
    c = int(input("input c: "))

    ok = a < b < c

    print(ok)

#bool_7()

#======================================= boolean8 ==================================================
# /Boolean8◦
# . Даны два целых числа: A, B. Проверить истинность высказывания:
# «Каждое из чисел A и B нечетное»

def bool_8():
    a = int(input("input a: "))
    b = int(input("input b: "))

    oka = a % 2 != 0
    okb = b % 2 != 0
    ok = oka and okb

    print(ok)

#bool_8()



#======================================= boolean9 ==================================================

# Boolean9◦
# . Даны два целых числа: A, B. Проверить истинность высказывания:
# «Хотя бы одно из чисел A и B нечетное».

def bool_9():
    a = int(input("input a: "))
    b = int(input("input b: "))

    oka = a % 2 != 0
    okb = b % 2 != 0
    ok = oka or okb

    print(ok)

#bool_9()

#======================================= boolean10 ==================================================
# Boolean10◦
# . Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное».

def bool_10():
    a = int(input("input a: "))
    b = int(input("input b: "))

    ok  = a % 2 == 0 and b % 2 != 0 or a % 2 != 0 and b % 2 == 0 #такий синтаксис не варто використовувати
    #треба декомпозувати

    #спочатку виконаються %
    #плотім <,<=,>,>=,!=,==
    #потім and
    #потім or


    print(ok)

#bool_10()

# Boolean11◦
# . Даны два целых числа: A, B. Проверить истинность высказывания: «Числа A и B имеют одинаковую четность»

def bool_11():
    a = int(input("input a: "))
    b = int(input("input b: "))

    ok0 = a % 2 == 0 and b % 2 == 0
    ok1 = a % 2 != 0 and b % 2 != 0
    ok2 = ok0 or ok1
    print(ok2)


def bool_11a():
    a = int(input("input a: "))
    b = int(input("input b: "))

    ok = a % 2 == b % 2 #ми дивимось тотожність остач від ділення а і в
    print(ok)


#bool_11a()

# Boolean12◦
# . Даны три целых числа: A, B, C. Проверить истинность высказывания: «Каждое из чисел A, B, C положительное».

def bool_12():
    a = int(input("input a: "))
    b = int(input("input b: "))
    c = int(input("input c: "))


    #2 solution
    ok = a > 0
    оk1= b > 0
    ok2 =c > 0

    ok3 = ok and оk1 and ok2

    print(ok3)

#bool_12()

#Boolean13◦
#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Хотя бы одно из чисел A, B, C положительное».

def bool_13():
    a = int(input("input a: "))
    b = int(input("input b: "))
    c = int(input("input c: "))


    #2 solution
    ok = a > 0
    оk1= b > 0
    ok2 =c > 0

    ok3 = ok or оk1 or ok2

    print(ok3)

#bool_13()

# Boolean14◦
# . Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное».

def bool_14():
    a = int(input("input a: "))
    b = int(input("input b: "))
    c = int(input("input c: "))


    ok = a > 0 and b <= 0 and c <=0
    оk1= b > 0 and a <= 0 and c <= 0
    ok2 =c > 0 and a <= 0 and b <= 0

    ok3 = ok or оk1 or ok2

    print(ok3)

#bool_14()


# Boolean15◦
# . Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно два из чисел A, B, C
# являются положительными».

def bool_15():
    a = int(input("input a: "))
    b = int(input("input b: "))
    c = int(input("input c: "))


    ok = a > 0 and b > 0 and c <=0
    оk1= b > 0 and a <= 0 and c > 0
    ok2 =c > 0 and a > 0 and b <= 0

    ok3 = ok or оk1 or ok2

    print(ok3)

#bool_15()

# Boolean16◦
# . Дано целое положительное число. Проверить истинность высказывания: «Данное число является четным двузначным»

def bool_16():
    a = int(input("input a: "))

    ok = a % 2 == 0 and a >= 10 and a <=99

    print(ok)

#bool_16()

# Boolean17◦
# . Дано целое положительное число. Проверить истинность высказывания: «Данное число является нечетным трехзначным».

def bool_17():
    a = int(input("input a: "))

    ok = a % 2 != 0 and a >= 100 and a <= 999

    print(ok)

#bool_17()

# Boolean18◦
# . Проверить истинность высказывания: «Среди трех данных целых
# чисел есть хотя бы одна пара совпадающих».

def bool_18():
    a = int(input("input a: "))
    b = int(input("input b: "))
    c = int(input("input c: "))

    ok = a == b or b == c or c == a

    print(ok)

#bool_18()

# Boolean19◦
# . Проверить истинность высказывания: «Среди трех данных целых
# чисел есть хотя бы одна пара взаимно противоположных».

def bool_19():
    a = int(input("input a: "))
    b = int(input("input b: "))
    c = int(input("input c: "))

    ok = a == -b or b == -c or c == -a

    print(ok)

#bool_19()

# Boolean20◦
# . Дано трехзначное число. Проверить истинность высказывания:
# «Все цифры данного числа различны».

def bool_20():
    n = int(input("input n: "))

    d0 = n // 1 % 10
    d1 = n // 10 % 10
    d2 = n // 100 % 10

    print("d0:",d0, "d1:", d1,"d2:", d2)

    x = d0 != d1 != d2

    print("x:", x)

#bool_20()

# Boolean21◦
# . Дано трехзначное число. Проверить истинность высказывания:
# «Цифры данного числа образуют возрастающую последовательность».

def bool_21():
    n = int(input("input n: "))

    d0 = n // 1 % 10
    d1 = n // 10 % 10
    d2 = n // 100 % 10

    print("d0:", d0, "d1:", d1, "d2:", d2)

    x = d0 > d1 and d1 > d2 and d2 < d0

    print("x:", x)


bool_21()

# Boolean22◦
# . Дано трехзначное число. Проверить истинность высказывания:
# «Цифры данного числа образуют возрастающую или убывающую последовательность».

def bool_22():
    a = int(input("input a: "))
    b = int(input("input b: "))
    c = int(input("input c: "))

    ok = a < b and b < c and c > a

#bool_22()

# Boolean23◦
# . Дано четырехзначное число. Проверить истинность высказывания:
# «Данное число читается одинаково слева направо и справа налево».

# Boolean23◦
# . Дано четырехзначное число. Проверить истинность высказывания: «Данное число читается одинаково
# слева направо и справа налево».

#d0 і д 3 буде одинакові І д1 і д2 теж буде одинакові одночасно


# Boolean24◦
# . Даны числа A, B, C (число A не равно 0). Рассмотрев дискриминант D = B
# 2 − 4·A·C, проверить истинность высказывания: «Квадратное
# уравнение A·x
# 2 + B·x + C = 0 имеет вещественные корни»

def bool_24():
    a = float(input("input a: "))
    b = float(input("input b: "))
    c = float(input("input c: "))

    d = b*b - 4*a*c
    print(d)

    ok = d >=0
    print("Зараз перевіряємо інфо чи у Д є у рівняння корені",ok)

#bool_24()


# Boolean25◦
# . Даны числа x, y. Проверить истинность высказывания: «Точка с
# координатами (x, y) лежит во второй координатной четверти».

def bool_25():
    x = float(input("x? = "))
    y = float(input("y? = "))

    ok = x < 0 and y > 0

    print(ok)

#bool_25()

# Boolean26◦
# . Даны числа x, y. Проверить истинность высказывания: «Точка с
# координатами (x, y) лежит в четвертой координатной четверти».



# Boolean26◦
# . Даны числа x, y. Проверить истинность высказывания: «Точка с
# координатами (x, y) лежит в четвертой координатной четверти».



# Boolean27◦
# . Даны числа x, y. Проверить истинность высказывания: «Точка с
# координатами (x, y) лежит во второй или третьей координатной четверти»

# Boolean28◦
# . Даны числа x, y. Проверить истинность высказывания: «Точка с
# координатами (x, y) лежит в первой или третьей координатной четверти».



#Boolean29◦
# . Даны числа x, y, x1, y1, x2, y2. Проверить истинность высказывания: «Точка с координатами (x, y) лежит
# внутри прямоугольника, левая
# верхняя вершина которого имеет координаты (x1, y1), правая нижняя —
# (x2, y2), а стороны параллельны координатным осям».




# Boolean30◦
# . Даны целые числа a, b, c, являющиеся сторонами некоторого треугольника. Проверить истинность высказывания: «Треугольник со сторо-
# Логические выражения 19
# нами a, b, c является равносторонним».

