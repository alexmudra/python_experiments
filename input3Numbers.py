'''
Программа должна принимать через пользовательский ввод несколько чисел через пробел. Соблюдаем следующие условия:
Чисел должно быть не менее трех;
Последнее число должно быть ровно в два раза больше чем первое;
Если условия не соблюдены, вывести на экран "Error".
Если условия соблюдены:
Если чисел парное количество, вывести на экран 2 средних числа, Т.Е. Если числа "10 15 3 20" - вывести на экран "15 3);
Если непарное, вывести на экран одно среднее число - "12 22 8 32 24" - вывести на экран "8";
'''

a = input("Enter more than 3digits number via space: ").split()
b = []
for i in range(len(a)):
    b.append(int(a[i]))
print("The list value: ",b)
print("List lenght: ",len(b), end='\n\n')

if len(b) <= 2:
    print("Error! Enter more than 3 digits.")
elif (b[2] * 2) < b[0]:
    print("Error! Please, enter vadid number")
else:
    print("You entered valid number")

if len(b) % 2 == 0:
    print("Я не знаю як виконати умову")

else:
    print("Я не знаю як виконати умову")

#print(len(b[1] and len(b[2])))