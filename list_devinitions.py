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


