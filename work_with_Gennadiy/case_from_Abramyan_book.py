import math
from math import pi

#Case1. Дано целое число в диапазоне 1–7. Вывести строку — название дня
# недели, соответствующее данному числу (1 — «понедельник», 2 — «вторник» и т. д.).

def case1():
    day = int(input("day(1-7) = "))

    day_name = "unknown day"
    if day == 1:
        day_name = "mon"
    elif day == 2:      #elif спрацює тільки якщо всі вищі не спрацювали. ELIF добре працює замість CASE
        day_name = "tue"
    elif day == 3:
        day_name = "wed"
    elif day == 4:
        day_name = "thur"
    elif day == 5:
        day_name = "friday"
    elif day == 6:
        day_name = "sutur"
    elif day == 7:
        day_name = "sund"

    print(day_name)

#case1()

# # . Дано целое число K. Вывести строку-описание оценки, соответствующей числу K (1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»). Если K не лежит в диапазоне 1–5,
# # то вывести строку «ошибка».

def case2():
    day = int(input("input day(1-5) = "))

    day_name = "error"

    if day == 1:
        day_name = "ploho"
    elif day == 2:
        day_name = "neud"
    elif day == 3:
        day_name = "udovlet"
    elif day == 4:
        day_name = "horosho"
    elif day == 5:
        day_name = "otlichno"

    print(day_name)

#case2()




# # Case3. Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.). Вывести название соответствующего времени года («зима»,
# # «весна», «лето», «осень»).
# # Case4◦


def case_3():
    month = int(input("input month(1-12) = "))
    season = "error"
    if month in [2,3,4]:
        season = "spring"
    elif month in [5,6,7]:
        season = "summer"
    elif month in [8,9,10]:
        season = "outhem"
    elif month in [11,12,1]:
        season = "winter"

    print(season)

#case_3()

# # Case4◦
# # . Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 —
# # февраль и т. д.). Определить количество дней в этом месяце для невисокосного года.


def is_year_leap(year):
    days = 365
    if year % 4 == 0:
        days = 366
        if year % 100 == 0 and year % 400 != 0:
            days = 365
    return days == 366

def get_month_days(month, year):
    if month == 1:
        return 31
    if month == 2:
        if is_year_leap(year): #передаємо функцію яка визначає високосний рік
            return 29
        else:
            return 28
    if month == 3:
        return 31
    if month == 4:
        return 30
    if month == 5:
        return 31
    if month == 6:
        return 30
    if month == 7:
        return 31
    if month == 8:
        return 31
    if month == 9:
        return 30
    if month == 10:
        return 31
    if month == 11:
        return 30
    if month == 12:
        return 31


#робимо цю саму задачку із масивом
def get_month_days_1(month, year):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]

    if is_year_leap(year):
        days[1] = 29
    return days[month-1]

def case_4():
    year = int(input("enter year: "))
    month = int(input("enter month 1-12: "))

    month_days = get_month_days(month, year)

    print("days = ", month_days)

#case_4()


#
# Case5. Арифметические действия над числами пронумерованы следующим
# образом: 1 — сложение, 2 — вычитание, 3 — умножение, 4 — деление. Дан
# номер действия N (целое число в диапазоне 1–4) и вещественные числа A
# и B (B не равно 0). Выполнить над числами указанное действие и вывести
# результат


def case_5():
    a = int(input("input A = "))
    while True:
        b = int(input("input B = "))
        if b != 0:
            break
    operations = input("operation (+ - * /)= ")

    if operations == "+":
        answer = a + b
    elif operations == "-":
        answer = a - b
    elif operations == "*":
        answer = a * b
    elif operations == "/":
        answer = a / b
    else:
        answer = "unknown operation"

    print(answer)

#case_5()


def test():
    a = int(input("input A = "))
    b = int(input("input B = "))
    try:
        z = a / b
    except:
        print("error.Divisin by ZERO is not alloved")


#test()

# Case6. Единицы длины пронумерованы следующим образом: 1 — дециметр,
# 2 — километр, 3 — метр, 4 — миллиметр, 5 — сантиметр. Дан номер
# единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих
# единицах (вещественное число). Найти длину отрезка в метрах.


def case_6():
    print("1 - decimetr")
    print("2 - km")
    print("3 - metr")
    print("4 - milimetr")
    print("5 - santimert")
    n = int(input("input n(1 2 3 4 5) = "))
    lenghth = int(input("input length = "))

    if n == 1:
        answer = lenghth / 10
    elif n == 2:
        answer = lenghth * 1000
    elif n == 3:
        answer = lenghth
    elif n == 4:
        answer = lenghth / 1000
    elif n == 5:
        answer = lenghth / 100
    else:
        answer = "error"

    print(answer)

#case_6()

# Case7. Единицы массы пронумерованы следующим образом: 1 — килограмм,
# 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах
# (вещественное число). Найти массу тела в килограммах.

def case_7():
    print("1 - kilogram")
    print("2 - miligramm")
    print("3 - gramm")
    print("4 - tonna")
    print("5 - centner")
    n = int(input("input № mass value: 1, 2, 3, 4, 5) = "))
    mass = float(input("input mass = "))

    if n == 1:
        answer = mass
    elif n == 2:
        answer = mass * 1000
    elif n == 3:
        answer = mass * 1000
    elif n == 4:
        answer = mass / 1000
    elif n == 5:
        answer = mass * 100
    else:
        answer = "input other value"

    print(answer)

#case_7()

# Case8. Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года. Вывести значения D и M для даты,
# предшествующей указанной.

def case_8():
    d = int(input("input day: 1-31) = "))
    m = int(input("input month: 1-12) = "))
    y = int(input("input year: ) = "))

    if d > 1:
        d -= 1
    else: #тут ми розглядаємо 1 число місяця
        m -= 1
        if m == 0: # внутрішня умова, якщо т == 0 (наприклад 1-1), то буде 12
            m = 12
            y -= 1
        d = get_month_days(m,y)

    print(d,m,y)

#case_8()


# Case9◦
# . Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года. Вывести значения D и M для даты,
# следующей за указанной.

#дз
def case_9():
    d = int(input("input day: (1-31) = "))
    m = int(input("input month: (1-12) = "))
    y = int(input("input year: ) = "))


    last_day = get_month_days(m,y) #взнаємо останній день місяці

    if d < last_day:
        d += 1
    else: #тут ми розглядаємо останній день місяця
        m += 1
        if m == 13: # внутрішня умова, якщо т == 0 (наприклад 1-1), то буде 12
            m = 1
            y += 1
        d = 1


    print(d,m,y)

#case_9()



# Case10◦. Робот может перемещаться в четырех направлениях («С» — север,
# «З» — запад, «Ю» — юг, «В» — восток) и принимать три цифровые ко-
# манды: 0 — продолжать движение, 1 — поворот налево, −1 — поворот
# направо. Дан символ C — исходное направление робота и целое число N
# — посланная ему команда. Вывести направление робота после выполне-
# ния полученной команды.


def case_10():
    x = 0 #початкова точка у робота
    y = 0
    direction = "north"

    while True:
        print(x,y,direction) # робот показує свій поточний стан
        command = input("command (right, left, go, exit)= ")
        if command == "right":
            if direction == "north":
                direction = "east"
            elif direction == "east":
                direction = "south"
            elif direction == "south":
                direction = "west"
            elif direction == "west":
                direction = "north"
        if command == "left":
            if direction == "north":
                direction = "west"
            elif direction == "east":
                direction = "north"
            elif direction == "south":
                direction = "east"
            elif direction == "west":
                direction = "south"
        if command == "go":
            if direction == "north":
                y = y + 1
            elif direction == "east":
                x = x + 1
            elif direction == "south":
                y = y - 1
            elif direction == "west":
                x = x - 1
        if command == "exit":
            break

#case_10()


# Case11. Локатор ориентирован на одну из сторон света («С» — север, «З» —
# запад, «Ю» — юг, «В» — восток) и может принимать три цифровые коман-
# ды поворота: 1 — поворот налево, −1 — поворот направо, 2 — поворот на
# 180◦. Дан символ C — исходная ориентация локатора и целые числа N1
# и N2 — две посланные команды. Вывести ориентацию локатора после
# выполнения этих команд.


def case_11():
    direction = "south"

    while True:
        print(direction) # робот показує свій поточний стан
        command = input("command (left, right, turn 180, exit)= ")

        if command == "left":
            if direction == "south":
                direction = "east"
            elif direction == "north":
                direction = "west"
            elif direction == "west":
                direction = "south"
            elif direction == "east":
                direction = "north"

        if command == "right":
            if direction == "south":
                direction = "west"
            elif direction == "north":
                direction = "east"
            elif direction == "west":
                direction = "north"
            elif direction == "east":
                direction = "south"

        if command == "turn 180":
            if direction == "south":
                direction = "north"
            elif direction == "north":
                direction = "south"
            elif direction == "west":
                direction = "east"
            elif direction == "east":
                direction = "west"

        if command == "exit":
            break

#case_11()





# Case12. Элементы окружности пронумерованы следующим образом: 1 — ра-
# диус R, 2 — диаметр D = 2·R, 3 — длина L = 2·π·R, 4 — площадь кру-
# га S = π·R2. Дан номер одного из этих элементов и его значение. Вывести
# значения остальных элементов данной окружности (в том же порядке). В
# качестве значения π использовать 3.14.
def case_12():
    value = float(input("enter value: "))
    tr_element = input("element (r, d , l , s): ")


    if tr_element == "r":
        r = value
        d = 2 * r
        l = 2*pi*r
        s = pi * r*math.sqrt(2)
    if tr_element == "d":
        d = value
        r = d / 2
        l = 2*pi*r
        s = pi*r*math.sqrt(2)
    if tr_element == "l":
        l = value
        r = l / 2 * pi
        d = r * 2
        s = pi*r*math.sqrt(2)
    if tr_element == "s":
        s = value
        r = s / pi * math.sqrt(2)
        d = r * 2
        l = 2*pi *r

    print(r, d , l , s)

#case_12()



# Case13. Элементы равнобедренного прямоугольного треугольника пронуме-
# рованы следующим образом: 1 — катет a, 2 — гипотенуза c = a·
# √
# 2, 3 —
# высота h, опущенная на гипотенузу (h = c/2), 4 — площадь S = c·h/2.
# Дан номер одного из этих элементов и его значение. Вывести значения
# остальных элементов данного треугольника (в том же порядке)

def case_13():
    value = float(input("enter value: "))
    tr_element = input("element (a, c , h , s): ")

    if tr_element == "a":
        a = value
        c = a * math.sqrt(2)
        h = c / 2
        s = c * h / 2
    if tr_element == "c":
        c = value
        a = c / math.sqrt(2)
        h = c / 2
        s = c * h / 2
    if tr_element == "h":
        h = value
        c = 2 * h
        a = c / math.sqrt(2)
        s = c * h / 2
    if tr_element == "s":
        s = value
        h = math.sqrt(s)
        c = 2 * h
        a = c / math.sqrt(2)

    print(a , c , h , s)


#case_13()


# Case14. Элементы равностороннего треугольника пронумерованы следую-
# щим образом: 1 — сторона a, 2 — радиус R1 вписанной окружности
# (R1 = a·
# √
# 3/6), 3 — радиус R2 описанной окружности (R2 = 2·R1), 4 —
# площадь S = a2·
# √
# 3/4. Дан номер одного из этих элементов и его значение.
# Вывести значения остальных элементов данного треугольника (в том же
# порядке).

#dz

def case_14():
    value = float(input("enter value: "))
    tr_element = input("element (a, r1, r2, s): ")

    if tr_element == "a":
        a = value
        r1 = a*math.sqrt(3/6) #радіус вписаної окружності
        r2 = 2 * r1
        s = pow(a,2)*math.sqrt(3/4)
    if tr_element == "r1":
        r1 = value
        a = r1 / math.sqrt(3/6)
        r2 = 2 * r1
        s = pow(a,2)*math.sqrt(3/4)
    if tr_element == "r2":
        r2 = value
        r1 = r2 / 2
        a = r1 / math.sqrt(3/6)
        s = pow(a,2)*math.sqrt(3/4)
    if tr_element == "s":
        s = value
        a = s / a * math.sqrt(3/4)
        r1 = a * math.sqrt(3 / 6)
        r2 = 2 * r1
    print("(a, r1, r2, s", a, r1, r2, s)

#case_14()





# Case15. Мастям игральных карт присвоены порядковые номера: 1 — пики,
# 2 — трефы, 3 — бубны, 4 — червы. Достоинству карт, старших десятки,
# присвоены номера: 11 — валет, 12 — дама, 13 — король, 14 — туз. Даны
# два целых числа: N — достоинство (6 ≤ N ≤ 14) и M — масть карты
# (1 ≤ M ≤ 4). Вывести название соответствующей карты вида «шестерка
# бубен», «дама червей», «туз треф» и т. п.


def case_15():

    while True:
        n = input("enter karti(6,7,8,9,T,J,Q,K,A): ")
        m_suit = input("suit ((s)pade, (c)lubs, (h)arts, (d)iamants) = ")

        result = ""

        if n == "6":
            result = "six "
        elif n == "7":
            result = "seven "
        else:
            result += "error "
        #etc


        if m_suit == "s":
            result += "spade"
        elif m_suit == "c":
            result += "clubs"
        elif m_suit == "h":
            result += "harts"
        elif m_suit == "d":
            result += "diamonds"
        else:
            result += "error "

        print(result)

#case_15()

# Case20. Даны два целых числа: D (день) и M (месяц), определяющие пра-
# вильную дату. Вывести знак Зодиака, соответствующий этой дате: «Водо-
# лей» (20.1–18.2), «Рыбы» (19.2–20.3), «Овен» (21.3–19.4), «Телец» (20.4–
# 20.5), «Близнецы» (21.5–21.6), «Рак» (22.6–22.7), «Лев» (23.7–22.8), «Де-
# ва» (23.8–22.9), «Весы» (23.9–22.10), «Скорпион» (23.10–22.11), «Стре-
# лец» (23.11–21.12), «Козерог» (22.12–19.1).


def is_month (m , month):
    month = 12
    if month > 12:
        raise Exception ("You input over 12 month. Try again, pls")


def case_20():
    d = int(input("enter day (1-31): "))
    m = int(input("enter month (1-12): "))
    result = "Input correct value"

    # while True:
    if (d >= 18 and m >= 1) or (d <= 20 and m <= 2):
        result = "Vodoley"
    if (d >= 19 and m >=2) or (d <= 20 and m <=3):
        result = "Fish"
    if (d >= 21 and m >=3) or (d <= 19 and m <=4):
        result = "Oven"
    if (d >= 20 and m >=4) or (d <= 20 and m <= 5):
        result = "Telec"
    if (d >= 21 and m >=5) or (d <=21 and m <= 6):
        result = "Bliznetci"
    if (d >= 22 and m >=6) or (d <= 22 and m <=7):
        result = "Rack"
    if (d >= 23 and m >=7) or (d <= 22 and m <=23):
        result = "Lev"
    if (d >= 23 and m >=8) or (d <=22 and m <= 9):
        result = "Deva"
    if (d >= 23 and m >=9) or (d <= 22 and m <= 10):
        result = "Vesi"
    if (d >= 23 and m >= 10) or (d <= 22 and m <= 11):
        result = "Scorpion"
    if (d >= 23 and m >= 11) or ( d <= 21 and m <= 12):
        result = "Streletc"
    if (d >= 22 and m == 12) or (d <= 19 and m == 1):
        result = "Kozerog"

    print(result)

        # try:
        #     x = is_month(m,12)
        #     print(x)
        # except Exception as f:
        #     print(f)


case_20()




