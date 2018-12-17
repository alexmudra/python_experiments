# -*- coding: utf-8 -*-
'''
Организовать пользовательский ввод и, если пользователь вводит слово ping, выводить ему в ответ pong. Если вводит pong, выводить ping.
Если вводит что-то другое, ничего не выводить.
Все это делаем циклично, что значит, сколько бы раз пользователь не ввел что-то, приложение не должно прекращать свою работу.
'''

# while True:
#     a = raw_input("Введите pong or ping: ")
#     b = "ping"
#     c = "pong"
#
#     if a == b:
#         print ("pong")
#     elif a == c:
#         print ("ping")


#Хороше рішення від Сані:

while True:
    people = raw_input('enter ping')
    x=''
    y='ping'
    z='pong'
    if people == y:
            x+=z
    elif people == z:
            x+=y
    print(x)

