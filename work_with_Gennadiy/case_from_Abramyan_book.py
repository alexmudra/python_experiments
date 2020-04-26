#Case1. Дано целое число в диапазоне 1–7. Вывести строку — название дня
# недели, соответствующее данному числу (1 — «понедельник», 2 — «вторник» и т. д.).
# # Case2◦
# # . Дано целое число K. Вывести строку-описание оценки, соответствующей числу K (1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»). Если K не лежит в диапазоне 1–5,
# # то вывести строку «ошибка».
# # Case3. Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.). Вывести название соответствующего времени года («зима»,
# # «весна», «лето», «осень»).
# # Case4◦
# # . Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 —
# # февраль и т. д.). Определить количество дней в этом месяце для невисокосного года.

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

#zd


# # Case3. Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.). Вывести название соответствующего времени года («зима»,
# # «весна», «лето», «осень»).
# # Case4◦

#dz

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

case_4()
