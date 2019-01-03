

#Приклад використання лістів і дікшінарі + умова

countries = [ #робимо ліст із дікшінарі всередині
    #дікшінарі із key and value
    {"name":'Thailand', 'sea': True, 'is_schengen':False},
    {"name":'Germany', 'sea': True, 'is_schengen':True},
    {"name": 'Ukraine', 'sea': True, 'is_schengen': False},
    {"name": 'Japan', 'sea': True, 'is_schengen': True}
]
#В циклі перебираємо значення із ліста
for i in countries:
    if i ['is_schengen'] and ['sea']:#умова де ми задаємо чи має країна море і шенгенську зону
        print("Such country has sea and schengen zone:", i ['name'])

'''
вивід:
Such country has sea and schengen zone: Germany
Such country has sea and schengen zone: Japan
'''
#-------------------------------------------------------


#Приклад використання лістів і дікшінарі + умова з температурою

countries = [ #робимо ліст із дікшінарі всередині
    #дікшінарі із key and value
    {"name":'Thailand', 'sea': True, 'is_schengen':False, 'temperature': 30},
    {"name":'Germany', 'sea': True, 'is_schengen':True, 'temperature': 22},
    {"name": 'Ukraine', 'sea': True, 'is_schengen': False, 'temperature': 25},
    {"name": 'Japan', 'sea': True, 'is_schengen': True, 'temperature': 34}
]
#В циклі перебираємо значення із ліста
for i in countries:
    if i ['is_schengen']:
        if i ['temperature'] >= 25:
            print("Such country has over 25 degree and schengen zone:", i['name'])
        elif i ['temperature'] <= 25:
            print("Such country has less 25 degree and schengen zone:", i['name'])
    else:
        print("Country is not in schengen zone", i['name'])




'''
вивід:

'''

