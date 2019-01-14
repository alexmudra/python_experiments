'''
Добавьте в программу ещё 5 стран (любых, по вашему
усмотрению, достоверность данных большой роли не играет)
• Добавьте новое свойство «стоимость проживания в сутки в
валюте страны»
• Пользуясь множествами, найдите список стран, которые:
тёплые и есть море или находятся в шенгене, и нам хватит
денег прожить там месяц.
'''

countries = [ #робимо ліст із dictionaries(словарями) всередині
    #дікшінарі із key and value

    {"name":'Thailand', 'sea': True, 'is_schengen':False, 'temperature': 30, 'currency':1.8, 'live_rate_24': 20},
    {"name":'Germany', 'sea': True, 'is_schengen':True, 'temperature': 22, 'currency':2, 'live_rate_24': 80},
    {"name": 'Ukraine', 'sea': True, 'is_schengen': False, 'temperature': 25, 'currency':1.4, 'live_rate_24': 30},
    {"name": 'Japan', 'sea': True, 'is_schengen': True, 'temperature': 30, 'currency':2.5, 'live_rate_24': 40},
    {"name": 'Moldova', 'sea': False, 'is_schengen': True, 'temperature': 22, 'currency': 1.2, 'live_rate_24': 55},
    {"name": 'Dubai', 'sea': True, 'is_schengen': False, 'temperature': 50, 'currency': 2.9, 'live_rate_24': 60}

]

schengen_countries = set() #ініціалізуємо set(множество) для країн в шенген зоні
sea_countries = set()#ініціалізуємо set(множество) для країн з морем
worm_countries = set()
we_can_live_countries = set()



for i in countries:
    if i ['is_schengen']:
        schengen_countries.add(i["name"])
    if i ['sea']:
        sea_countries.add(i['name'])
    if i ['temperature']:
        if i['temperature'] > 22:
            worm_countries.add(i['name'])
    if i ['live_rate_24']:
        we_can_live_countries.add(i['name'])



print("Countries with sea", sea_countries)
print("Countries with schengen zone AND sea", schengen_countries & sea_countries) # використаємо AND
print("Countries with schengen zone OR sea", schengen_countries | sea_countries) # використаємо OR
print("Worm countries", worm_countries)
print("Sea and worm countries", worm_countries & sea_countries)
print("Worm and schengen countries", worm_countries & schengen_countries)




#Приклад арифметичних(ділення) операцій із частиною дікшінарі. Конвертуємо наші гроші в місцеву валюту

our_money = 1200

for country in countries:
        if (our_money/country['currency'])/31 >= country['live_rate_24']:
                print("We can live in", country['name'])
        else:
            print("We can't live")





#
#         converted_money = our_money / country['currency']
#         live_24 = converted_money/31
#
# for s in countries:
#     if live_24 >= s['live_rate_24']:
#         print("We can live in country")
#     else:
#         print("We can't live in such counry becouse we have only,", live_24)
#




