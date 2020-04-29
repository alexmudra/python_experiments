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

case_6()

# Case7. Единицы массы пронумерованы следующим образом: 1 — килограмм,
# 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах
# (вещественное число). Найти массу тела в килограммах.



# Case8. Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года. Вывести значения D и M для даты,
# предшествующей указанной.
# Case9◦
# . Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года. Вывести значения D и M для даты,
# следующей за указанной.