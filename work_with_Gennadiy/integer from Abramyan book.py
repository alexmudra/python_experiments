
#======================================= Целые числа ===============================================
# Все входные и выходные данные в заданиях этой группы являются це-
# лыми числами. Все числа, для которых указано количество цифр (двузначное
# число, трехзначное число и т. д.), считаются положительными.

SEC_IN_MIN = 60
SEC_IN_HOUR = 3600
MINS_IN_HOUR = 60
MINS_IN_DAY = 24 * 60
HOURS_IN_DAY = 24

#======================================= Integer30 ==================================================
#
# Integer30◦
# . Дан номер некоторого года (целое положительное число). Определить соответствующий ему номер столетия, учитывая, что, к примеру,
# началом 20 столетия был 1901 год.

def integer_30():
    year = int(input("Initial year is: "))

    century = (year-1) // 100+1

    print(century)
#integer_30()
#======================================= Integer25 ==================================================

# Integer25◦
# . Дни недели пронумерованы следующим образом: 0 — воскресенье,
# 1 — понедельник, 2 — вторник, . . . , 6 — суббота. Дано целое число K,
# лежащее в диапазоне 1–365. Определить номер дня недели для K-го дня
# года, если известно, что в этом году 1 января было четвергом.

def integer_25():
    n = int(input("day = "))
    f_jan = int(input('Введите каким номером недели было 1 января = '))

    d = ((f_jan+n-2)%7)+1
    print(d)

integer_25()






#======================================= Integer24 ==================================================
# Integer24◦
# . Дни недели пронумерованы следующим образом: 0 — воскресенье,
# 1 — понедельник, 2 — вторник, . . . , 6 — суббота. Дано целое число K,
# лежащее в диапазоне 1–365. Определить номер дня недели для K-го дня
# года, если известно, что в этом году 1 января было понедельником.
def integer_24():
    n = int(input("day = "))
    f_jan = int(input('Введите каким номером недели было 1 января = '))

    d = ((f_jan+n-2)%7)+1
    print(d)

#integer_24()




#======================================= Integer23 ==================================================
# #Integer23◦
# . С начала суток прошло N секунд (N — целое). Найти количество
# полных минут, прошедших с начала последнего часа
def integer_23():
    n = int(input("n_seconds = "))

    sec = n % SEC_IN_HOUR
    sec_convert_to_min = sec // 60
    print(sec_convert_to_min)

#integer_23()
#======================================= Integer22 ==================================================
# Integer22◦
# . С начала суток прошло N секунд (N — целое). Найти количество
# секунд, прошедших с начала последнего часа.
def integer_22():
    n = int(input("n_seconds = "))

    sec = n % SEC_IN_HOUR

    print(sec)

#integer_22()

#======================================= Integer21 ==================================================
# Integer21◦
# . С начала суток прошло N секунд (N — целое). Найти количество
# секунд, прошедших с начала последней минуты

def integer_20():
    n = int(input("n_seconds = "))

    sec = n % SEC_IN_MIN

    print(sec)

#integer_20()


#======================================= Integer20 ==================================================
# Integer20◦
# . С начала суток прошло N секунд (N — целое). Найти количество
# полных часов, прошедших с начала суток.
def integer_20():
    n = int(input("n_seconds = "))

    hours = n // SEC_IN_HOUR

    print(hours)

#integer_20()

#======================================= Integer19 ==================================================
# Integer19◦
# . С начала суток прошло N секунд (N — целое). Найти количество
# полных минут, прошедших с начала суток


def integer_19():
    n = int(input("n = "))

    min = n // SEC_IN_MIN
    print(min)

#integer_19()




#======================================= time ==================================================
# Integer19◦
# . С начала суток прошло N секунд (N — целое). Найти количество
# полных минут, прошедших с начала суток.

def integer_time():
    n = int(input("n = "))

    hours = n // 3600
    rest = n % 3600

    minutes = rest//60
    sec = rest%60

    print(hours, minutes, sec)

#integer_time()


#======================================= Integer18 ==================================================
# Integer18◦
# . Дано целое число, большее 999. Используя одну операцию деления нацело и одну операцию
# взятия остатка от деления, найти цифру,
# соответствующую разряду тысяч в записи этого числа.

def integer_18():
    n = int(input("n = "))

    d3 = n // 1000 % 10

    print(d3)

#integer_18()



#======================================= Integer17 ==================================================
# Integer17◦
# . Дано целое число, большее 999. Используя одну операцию деления нацело и одну операцию
# взятия остатка от деления, найти цифру,# соответствующую разряду сотен в записи этого числа


def integer_17():
    n = int(input("n = "))

    d2=n // 100 %10
    print(d2)

#integer_17()


#======================================= Integer16 ==================================================

# Integer16◦
# . Дано трехзначное число. Вывести число, полученное при перестановке цифр десятков и единиц исходного числа (например,
# 123 перейдет
# в 132).

def integer_16():
    n = int(input("n = "))

    d0 = n // 1 % 10
    d1 = n // 10 % 10
    d2 = n // 100 % 10
    #d3 = n // 1000 % 10
    print(d2, d0, d1)

#integer_16()




#======================================= Integer15 ==================================================

# Integer15◦
# . Дано трехзначное число. Вывести число, полученное при перестановке цифр сотен и десятков исходного числа
# (например, 123 перейдет в
# 213).

def integer_15():
    n = int(input("n = "))

    d1 = n %10
    print(d1)

    d1 = n%100
    print(d1)

    y = d2*100 + d1*10 + d3*1 #
    print(y)


#integer_15()



#======================================= Integer14 ==================================================
# Integer14◦
# . Дано трехзначное число. В нем зачеркнули первую справа цифру
# и приписали ее слева. Вывести полученное число.

#123
# де 3 це нульовий розряд (самий молодший розряд)
# де 2 це перший розряд
# де 1 це другий розряд

def integer_14():
    n = int(input("n = "))

    d0 = n // 1 % 10
    d1 = n // 10 % 10
    d2 = n // 100 % 10
    d3 = n // 1000 % 10
    print(d0, d1, d2, d3)

    y = d1*100 + d0*10 + d2*1

    print("виводим цифри:", y)

def integer_14a(): #присвоювання через стрінг в ліст потім в стрінг і інт
    n = int(input("n = "))

    s = str(n)
    l = list(s)
    t = l[0]
    l[0] = l[1]
    l[1] = l[2]
    l[2] = t

    s1 = "".join(l)
    n = int(s1)

    print(n)

#integer_14a()

#======================================= Integer13 ==================================================

# Integer13◦
# . Дано трехзначное число. В нем зачеркнули первую слева цифру и
# приписали ее справа. Вывести полученное число

def integer_13():
    n = int(input("n = "))


    d1 = n % 10
    n = n // 10
    d2 = n % 10
    n = n // 10
    d3 = n % 10

    print("Сумма цифр числа:", d2, d3, d1)

#integer_13()




#======================================= Integer12 ==================================================

# Integer12◦
# . Дано трехзначное число. Вывести число, полученное при прочтении исходного числа справа налево

def integer_12():
    n = int(input("n = "))


    d1 = n % 10
    n = n // 10
    d2 = n % 10
    n = n // 10
    d3 = n % 10

    print("Сумма цифр числа:", d1, d2, d3)

#integer_12()




#======================================= Integer11 ==================================================
#Integer11 ◦ . Дано трехзначное число. Найти сумму и произведение его цифр.

def integer_11():
    n = int(input("n = "))

#Алгоритм нахождения суммы цифр трехзначного числа abc (где a - сотни, b - десятки и c - единицы) можно описать так:

    d1 = n % 10 #Найти остаток от деления abc на 10, записать его в переменную d1. Это будет цифра c.

    n = n // 10 #Избавиться от цифры c в числе abc, разделив его нацело на 10.
    d2 = n % 10 #Найти остаток от деления ab на 10, записать его в переменную d2. Это будет цифра b.

    n = n // 10 #Избавиться от цифры b в числе ab, разделив его нацело на 10.
    d3 = n % 10 #Найти остаток от деления a на 10, записать его в переменную d3. Это будет цифра a.




    print("Сумма цифр числа:", d1 + d2 + d3) #Сложить цифры a, b и c.



#integer_11()




#======================================= Integer8 ==================================================
#
# Integer8 ◦ . Дано двузначное число. Вывести число, полученное при переста-
# новке цифр исходного числа.

def integer_8():
    n = int(input("n = "))

    find_10 = n % 10
    find_1 = n // 10

    print(find_10, find_1)

#integer_8()


#======================================= Integer7 ==================================================

#Integer7 ◦ . Дано двузначное число. Найти сумму и произведение его цифр.

def integer_7():
    n = int(input("n = "))

    find_10 = n % 10
    find_1 = n // 10

    sum = find_1 + find_10
    print(sum)

#integer_7()



#======================================= Integer6 ==================================================
#
# Integer6 ◦ . Дано двузначное число. Вывести вначале его левую цифру (десят-
# ки), а затем — его правую цифру (единицы). Для нахождения десятков
# использовать операцию деления нацело, для нахождения единиц — опе-
# рацию взятия остатка от деления.

def integer_6():
    n = int(input("n = "))

    find_10 = n % 10
    find_1 = n // 10

    print(find_1, find_10)

#integer_6()

#======================================= Integer5 ==================================================
#
# Integer5 ◦ . Даны целые положительные числа A и B (A > B). На отрезке длины A
# размещено максимально возможное количество отрезков длины B (без
# наложений). Используя операцию взятия остатка от деления нацело, найти
# длину незанятой части отрезка A.

def integer_5():
    a = int(input("a = "))
    b = int(input("b = "))


    how_many_last_b = a % b
    print("last part of b is ", how_many_last_b)

#integer_5()



#======================================= Integer4 ==================================================

# Integer4 ◦ . Даны целые положительные числа A и B (A > B). На отрезке дли-
# ны A размещено максимально возможное количество отрезков длины B
# (без наложений). Используя операцию деления нацело, найти количество
# отрезков B, размещенных на отрезке A.

def integer_4():
    a = int(input("a = "))
    b = int(input("b = "))

    if a >= b:
        how_many_b = a // b
        print("b is ", how_many_b)
    else:
        print("Are you sure a > b?")

#integer_4()







#======================================= Integer3 ==================================================

# Integer3 ◦ . Дан размер файла в байтах. Используя операцию деления нацело,
# найти количество полных килобайтов, которые занимает данный файл
# (1 килобайт = 1024 байта).

def integer_3():
    byte = int(input("byte = "))
    f_byte = byte//1024
    print(f_byte)

#integer_3()



#======================================= Integer2 ==================================================
# Integer2 ◦ . Дана масса M в килограммах. Используя операцию деления нацело,
# найти количество полных тонн в ней (1 тонна = 1000 кг).

def integer_2():
    m = int(input("m = "))

    while m >= 1000:
        t = m // 1000  # отримуємо цілу частину
        print(t)
        break
    else:
        print("Number should be over 1000")

#integer_2()


#======================================= Integer1 ==================================================


# Integer1 ◦ . Дано расстояние L в сантиметрах. Используя операцию деления
# нацело, найти количество полных метров в нем (1 метр = 100 см).


def integer_1():
    l = int(input("l = "))

    m = l//100 #отримуємо цілу частину

    print(m)

#integer_1()
