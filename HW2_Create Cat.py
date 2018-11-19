"""

Создадим кота, но дадим возможность пользователю определить некоторые его параметры следующим образом:
Предлогаем пользователю ввести четырехзначное число; Затем разбираем пользовательский ввод следующим образом:
Первая цифра отвечает за цвет кота. От 0 до 2 - белый. От 3 до 4 - рыжий. От 5 до 7 - серый. От 8 до 9 - черный.
Вторая цифра отвечает за размер кота. От 0 до 2 - маленький. От 3 до 5 - небольшой. от 6 до 7 - большой. От 8 до 9 - очень большой.
Третья цифра отвечает за характер кота. От 0 до 1 - ленивый. От 2 до 4 - спокойный. от 5 до 7 - подвижный. от 8 до 9 - гиперактивный.
Четвертая цифра отвечает за "пушистость". От 0 до 2 - короткошерстный. От 3 до 5 - гладкошерстный. От 6 до 7 - пушистый. От 8 до 9 - очень пушистый.
После того, как пользователь ввел число, кнему должна вернуться информация примерно следующего вида: "Это пушистый белый кот, он крупный и ленивый.".

"""

a = input("Input 4digits number: ")
b = []
for i in range(len(a)):
    b.append(int(a[i]))

print("---Start. System information.---")
print(b)
print(type(b))
print(len(b))
print("---end---")


if len(a) == 4:
    print("Success. Your imput has 4digits")
else:
    print("Invalid number! Please enter 4 digits number")


if b[1] >= 0 and b[1] <= 2:
    print("This is little")
elif b[1] == 3 or b[1] == 4:
    print("This is tiny")
elif b[1] >= 5 and b[1] <= 7:
    print("This is big")
else:
    print("This is enormous")



if b[0] >= 0 and b[0] <= 2:
    print("white cat.")
elif b[0] == 3 or b[0] == 4:
    print("orange cat.")
elif b[0] >= 5 and b[0] <= 7:
    print("grey cat.")
else:
    print("black cat.")


if b[2] >= 0 and b[2] <= 2:
    print("He is lazy")
elif b[2] == 3 or b[2] == 4:
    print("He is calm")
elif b[2] >= 5 and b[2] <= 7:
    print("He is energetic")
else:
    print("He is hiperactive")


if b[3] >= 0 and b[3] <= 2:
    print("and has short fur.")
elif b[3] == 3 or b[3] == 4:
    print("and has smooth fur.")
elif b[3] >= 5 and b[3] <= 7:
    print("and has a lot of fur.")
else:
    print("and ahs fur fur fur.")













