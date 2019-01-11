#Приклад перебору значень в dict через цикл for

countries_population = {} #ініціалізували новий дікшінарі

countries_population = {
    'Ukraine': 52000000,
    'France': 62000000,
    'Japan': 126693000
}

#Отримати значення із словаря countries_population

population_in_ukraine = countries_population['Ukraine']
print("Ukraine has:", population_in_ukraine)
'''
Ukraine has:  52000000
'''

#обійти всі елементи словаря в циклі

for i in countries_population:
    print(i, countries_population[i])
'''
Ukraine 52000000
Japan 126693000
France 62000000
'''