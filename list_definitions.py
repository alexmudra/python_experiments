#ПРИКЛАД З ЛІСТ(МАСИВАМИ) LIST

char_list = ['a', 'b','c']
num_list = [1,2,3,4,5]
empty_list = []

a = "This is the"
print(a, "char list: ", char_list)
print(a, "int list: ", num_list)
print(a, "empty list: ", num_list)

# This is the char list:  ['a', 'b', 'c']
# This is the int list:  [1, 2, 3, 4, 5]
# This is the empty list:  [1, 2, 3, 4, 5]

list_from_range = list(range(5)) #надрукуємо ліст з числами від 0 до 4 за допомогою ф-ії list
print(list_from_range)
#[0, 1, 2, 3, 4]


print(list("To to to la la la")) #надрукуємо ліст із стрінги шляхом преобразування в ліст
#['T', 'o', ' ', 't', 'o', ' ', 't', 'o', ' ', 'l', 'a', ' ', 'l', 'a', ' ', 'l', 'a']


#Виведем суму 1 і останнього елементу списку

print(num_list[0] + num_list[-1])
#6


#Слайси в лістах

print(num_list[:3]) #виведем вміст ліста від 1 індексу до 3го
#[1, 2, 3]

print(num_list[1:-1]) #виведем вміст ліста від 2го індекса по передостанній
#[2, 3, 4]

print(num_list[0:-1:2])#отримаємо 1 елемент і останній із кроком в 2
#[1, 3]

print(num_list[::-2])#в зворотньому порядку з кроком в 3
#[5, 3, 1]


#РОЗГЛЯДАЄМО in в лістах (in перевіряє входження ОДНОГО елементу в лістах(не як в стрінгах)

my_list = [1,2,3,4,5,6,7,8,9,10]
'''
#user_input = int(input("Input the value: "))

if user_input in my_list:
        print("Your input correct!")
else:
    print("Your input incorrect!")
#Input the value: 2
#Your input correct!
'''
#-----------------------------------------------------------------------

#Розглядаємо функцію len для лістів

print("Number of elements for function len: ", len(my_list))
#Input the value: 3
#Your input correct!
#Number of elements for function len :  10


my_string = 'This is my string'

print(my_string)#This is my string

print(my_string[0]) #T
print(my_string[1]) #h
print(my_string[2]) #i
print(my_string[3]) #s
print(my_string[4]) #пробіл
print(len(my_string))# 17 елементів в стінг

print(my_string[2:5]) #is
print(my_string[::5]) #Ti n
print(my_string[::2]) #Ti sm tig (виборка із кроком 2)
print(my_string[::-2]) #git ms iT (виборка в зворотньому напрямку із кроком 2)


print(my_string[2] + my_string[-1]) #ig - конкатенація 2го і останнього символів в лісті
print(my_string[2:4] + " " + my_string[-4:]) #is ring - конкатенація is пробілу 4 символів в зворот.порядку

#------------------------------------------------------------------------


#ПЕРЕГЛЯНЕМО ЧИ ВХОДИТЬ ЕЛЕМЕНТ в СТРІНГУ ЗА ДОПОМОГОЮ (in)

user_input = input("Enter some text: ")

if "sasha" in user_input:
    print("Cool. You guessed Sasha")
elif "anya" in user_input:
        print("You guessed Anya")
elif "girl" in user_input:
        print("You guessed Girl")
else:
    print("Try more")
