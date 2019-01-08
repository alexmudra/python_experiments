

#Приклад використання лістів і дікшінарі + умова

# countries = [ #робимо ліст із дікшінарі всередині
#     #дікшінарі із key and value
#     {"name":'Thailand', 'sea': True, 'is_schengen':False},
#     {"name":'Germany', 'sea': True, 'is_schengen':True},
#     {"name": 'Ukraine', 'sea': True, 'is_schengen': False},
#     {"name": 'Japan', 'sea': True, 'is_schengen': True}
# ]
# #В циклі перебираємо значення із ліста
# for i in countries:
#     if i ['is_schengen'] and ['sea']:#умова де ми задаємо чи має країна море і шенгенську зону
#         print("Such country has sea and schengen zone:", i ['name'])
#
# '''
# вивід:
# Such country has sea and schengen zone: Germany
# Such country has sea and schengen zone: Japan
# '''
#-------------------------------------------------------


#Приклад використання лістів і дікшінарі + умова з температурою

# countries = [ #робимо ліст із dictionaries(словарями) всередині
#     #дікшінарі із key and value
#     {"name":'Thailand', 'sea': True, 'is_schengen':False, 'temperature': 30},
#     {"name":'Germany', 'sea': True, 'is_schengen':True, 'temperature': 22},
#     {"name": 'Ukraine', 'sea': True, 'is_schengen': False, 'temperature': 25},
#     {"name": 'Japan', 'sea': True, 'is_schengen': True, 'temperature': 34}
# ]
# #В циклі перебираємо значення із ліста
# for i in countries:
#     if i ['is_schengen']:
#         if i ['temperature'] >= 25:
#             print("Such country has over 25 degree and schengen zone:", i['name'])
#         elif i ['temperature'] <= 25:
#             print("Such country has less 25 degree and schengen zone:", i['name'])
#     else:
#         print("Country is not in schengen zone", i['name'])
'''
вивід:
Country is not in schengen zone Thailand
Such country has less 25 degree and schengen zone: Germany
Country is not in schengen zone Ukraine
Such country has over 25 degree and schengen zone: Japan
'''

#--------------------------------------------------------------

#Приклад коду із SET (множества)

countries = [ #робимо ліст із dictionaries(словарями) всередині
    #дікшінарі із key and value
    {"name":'Thailand', 'sea': True, 'is_schengen':False, 'temperature': 30, 'currency':1.8},
    {"name":'Germany', 'sea': True, 'is_schengen':True, 'temperature': 22, 'currency':2},
    {"name": 'Ukraine', 'sea': True, 'is_schengen': False, 'temperature': 25, 'currency':1.4},
    {"name": 'Japan', 'sea': True, 'is_schengen': True, 'temperature': 34, 'currency':2.5}]

schengen_countries = set() #ініціалізуємо set(множество) для країн в шенген зоні
sea_countries = set()#ініціалізуємо set(множество) для країн з морем

for i in countries:
    if i ['is_schengen']:
        schengen_countries.add(i["name"])
    if i ['sea']:
        sea_countries.add(i['name'])


print("Countries with sea", sea_countries)
print("Countries with schengen zone AND sea", schengen_countries & sea_countries) # використаємо AND
print("Countries with schengen zone OR sea", schengen_countries | sea_countries) # використаємо OR

'''
Countries with sea {'Thailand', 'Germany', 'Japan', 'Ukraine'}
Countries with schengen zone AND sea {'Germany', 'Japan'}
Countries with schengen zone OR sea {'Thailand', 'Germany', 'Ukraine', 'Japan'}
'''
#---------------------------------------------------------------------

#Приклад арифметичних(ділення) операцій із частиною дікшінарі. Конвертуємо наші гроші в місцеву валюту

our_money = 10000 #об'явим і ініціалізуєм перемінну

for country in countries:
    print("We have:",our_money,'.If we are going to exchange out money, we got', our_money/ country['currency'])
'''
We have: 10000 .If we are going to exchange out money, we got 5555.555555555556
We have: 10000 .If we are going to exchange out money, we got 5000.0
We have: 10000 .If we are going to exchange out money, we got 7142.857142857143
We have: 10000 .If we are going to exchange out money, we got 4000.0
'''







