
#Програма яка рахує час перебування в Шенгенській зоні


residence_limit = 90
shengen_const = 180

your_visits = [[1, 10], [30, 54], [60, 89], [120, 150]] # двомірний список де 1 цифра це дата заїзду, а 2-га - виїзду

total_time_us = 0

for visit in your_visits:
    total_time_us += visit[1] - visit[0] + 1 #в першій ітерації від 10 відняли 1 (і додали 1) в лісті your_visits

overstay_days = total_time_us - residence_limit
print("Ви перевищили час перебування в шенгені на", overstay_days, "днів")

#assert (overstay_days == 10 + 25 + 30 + 40 - residence_limit)
