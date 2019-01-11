
#Програма яка рахує час перебування в Шенгенській зоні


residence_limit = 90
shengen_const = 180

your_visits = [[1, 10], [30, 54], [60, 89], [120, 150]] # двомірний список де 1 цифра це дата заїзду, а 2-га - виїзду

total_time_us = 0

for visit in your_visits:

#проходимося по списку і віднімаємо від дати виїзду(10, 54, 89, 150) дату заїзду
    total_time_us += visit[1] - visit[0] + 1 #в першій ітерації від 10 відняли 1 (і додали 1) в лісті your_visits

overstay_days = total_time_us - residence_limit #віднімаємо від к-сті днів які ми вже пробули дні які перевищили

print("Ви перевищили час перебування в шенгені на", overstay_days, "днів")

#assert (overstay_days == 10 + 25 + 30 + 40 - residence_limit)



#----------------------------------------------------------------
# Новий варіант коду по підрахунку перебування в Шенгенській зоні


residence_limit = 90  # 45, 60
schengen_constraint = 180

# Мы тратим в день
cost_per_day = 15

first_of_january = 1  # первое января текущего года

first_time_arriving = 1
first_time_leave = 11

second_time_arriving = 16
second_time_leave = 27

third_time_arriving = 45
third_time_leave = 46

total_time_in_es = (first_time_leave - first_time_arriving)
total_time_in_es = total_time_in_es + (second_time_leave - second_time_arriving)
total_time_in_es = total_time_in_es + (third_time_leave - third_time_arriving)

if total_time_in_es > residence_limit:
    print('Вы не можете прибывать в ЕС так долго')

print('Вы пробудете в ЕС дней:', total_time_in_es)