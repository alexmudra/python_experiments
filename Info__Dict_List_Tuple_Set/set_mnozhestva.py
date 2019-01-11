
#ініціалізуємо сет. Тобто невпорядковане множество унікальних об'єктів або записів
friends = set()

#заповнимо set значеннями list
classmates = set(['Kolya', 'Sasha', "Masha", 'Kvitka', 'Nizinka'])
print(classmates)
'''
{'Masha', 'Kolya', 'Sasha', 'Kvitka', 'Nizinka'}
'''

#додамо значення в SET
friends.add('Nikaragua')
friends.add('Galina')
print(friends)
'''
{'Nikaragua', 'Galina'}
'''

#додамо значення в уже заповнений SET
classmates.add('Gorliy')
classmates.add('Opps')
print(classmates)
'''
{'Kolya', 'Masha', 'Sasha', 'Kvitka', 'Nizinka', 'Gorliy', 'Opps'}
'''

#Перевірити наявність значення/елементу в SET

if 'Doodle' in friends:
    print("YES")
else:
    print("NO")
'''
NO
'''

#Знайти суму множеств
friends_or_classmates = friends | classmates
print("Ось сума множеств з сета friends і classmates", friends_or_classmates)
'''
Ось сума множеств з сета friends і classmates {'Nikaragua', 'Kvitka', 'Masha', 'Galina', 'Kolya', 'Nizinka', 'Gorliy', 'Sasha', 'Opps'}
'''

#Знайти відмінні елементи у множеств(пересєчєніє)
friends_and_classmates = friends & classmates
print("Ось унікальні елементи із сетів friends і classmates", friends_and_classmates)
'''
Ось унікальні елементи із сетів friends і classmates set()
'''

#Пройтись по всим елементам 2х SETів через цикл FOR

for elements in friends and classmates:
    print("Ось всі елементи 2х сетів:", elements)
'''
Ось всі елементи 2х сетів: Nizinka
Ось всі елементи 2х сетів: Kvitka
Ось всі елементи 2х сетів: Kolya
Ось всі елементи 2х сетів: Gorliy
Ось всі елементи 2х сетів: Masha
Ось всі елементи 2х сетів: Opps
Ось всі елементи 2х сетів: Sasha
'''

#Перетворити SET в LIST

friends_list = list(friends)
print(type(friends_list))
'''
<class 'list'>
'''

