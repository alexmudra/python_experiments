import re

q = "misha sasha masha kolya masha"


print("Довжина стрінги: ",len(q))

print("Результат frfind: ", q.rfind("kolya", 0,28))

print("Результат index: ", q.index("masha", 0,28))

print("Результат rindex: ", q.rindex("masha", 0,28))


'''
# Состоит ли ВСЯ строка из символов в верхнем регистре
'''
a = q
print("Результат replace: ", a.replace("masha", "gosha"))


'''
# Состоит ли строка из неотображаемых символов (пробел, символ перевода страницы ('\f'),
"новая строка" ('\n'), "перевод  каретки" ('\r'), "горизонтальная табуляция" ('\t') и вертикальная табуляция ('\v'))
'''
a = "\f\n\r\t\v"
print(a.isspace())


'''
# Начинаются ли слова в строке с заглавной буквы
'''
a = "DSFSDFSD"
print(a.istitle())


b = "sdfkjskjfnskf"
print(a.upper())

print("SFDSFSDF".lower())


# Начинается ли строка S с шаблона str
a = "DSFSDFSD"
print(a.startswith("DSF"))

# Заканчивается ли строка S шаблоном str
a = "DSFSDFSD"
print(a.endswith("SD"))

# Сборка строки из списка с разделителем S
print("-".join(["a", "l", "e", "x"]),'a-n-d-r')


s = "55 ящик"

result = re.findall(r'\w+$', "55 ящик")
print("This is the last word: ", (result)[0])


result = re.findall(r'\w+$', s)