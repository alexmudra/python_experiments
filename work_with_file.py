
# Приклад як можна прочитати картинку
# a = "pict.jpg"
# with open(a, 'wb') as Pictures:
#     Pictures.a

# # Прочитає інфо із файлу построково. Щоб пройтися по файлу використали цикл FOR
# with open('my_file.txt', 'rt') as Documents:
#     for line in Documents:
#          print(line)
#
# '''
# Koba
# great programmer
# super puper
# ))
# '''
#-----------------------------------------------------------
#Порахуємо середню температуру. Дані прочитаємо із файла temperature.txt

temperature = []

with open('temperature.txt') as doc:
    for line in doc:
        temperature.append(int(line))

print("Info from txt file", temperature)
avg_temperature = sum(temperature) / len(temperature)

#використаємо ф-ію round щоб округлити флоат число
print("Average winter temper.in Kyiv:", round(avg_temperature, 4))

'''
Info from txt file [-8, -2, -10, -5, 6, 12, -20]
Average winter temper.in Kyiv: -3.8571
'''

#-----------------------------------------------------------------------------------------
# Приклад як ,через ф-ію .strip видалимо лишню табуляцію, перенос каретки, пробіл

with open('temperature.txt') as doc:
    for line in doc:
# приклад як ,через ф-ію .strip видалимо лишню табуляцію, перенос каретки, пробіл
        temperature.append(line.strip())

print("Info from txt file and .strip", temperature)
'''
Info from txt file and .strip [-8, -2, -10, -5, 6, 12, -20, '-8', '-2', '-10', '-5', '6', '12', '-20']
<<<<<<< Updated upstream


'''
#----------------------------------------------------------Прочитаєм і запишем файл температуру
temperature = []

with open('temperature.txt') as doc:
    for line in doc:
        temperature.append(int(line))

print("Info from txt file", temperature)
avg_temperature = sum(temperature) / len(temperature)

#використаємо ф-ію round щоб округлити флоат число
print("Average winter temper.in Kyiv:", round(avg_temperature, 4))

#створимо файл і запишем в файл середню температуру(із флагом w)
with open('average_temp_file.txt', 'w') as avg:
    avg.write(str("%2.f" %avg_temperature))

#------------------------------------------------Запишем дані в ліст

#запишемо температуру в список
temperature_deviation = [] #об'явимо список
for i in temperature: # цикл з ітератором
    temperature_deviation.append(i - avg_temperature) #вичисляємо різницю температур

with open('average_temperature.txt', 'w') as t_average_file:
    t_average_file.write('%.2f' % avg_temperature)

with open('temperature_deviation.txt', 'w') as t_deviation_file:
    for t in temperature_deviation:
        t_deviation_file("%.2f\n" % t)
=======
'''
#-----------------------------------------------------------------
# Запишем результати в файл

with open (avg_temperature.txt, 'w') as write_doc:
    a

>>>>>>> Stashed changes
