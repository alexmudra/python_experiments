
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
    avg.write(str(avg_temperature))


