# -*- coding: utf-8 -*-

'''
Получить от пользователя текст, предоставив ему возможность многострочного ввода, окончить ввод по команде "/s";
Проверить являются ли первые буквы строк большими, если нет, заменить на большие;

Проверить являются ли первые буквы после символа точка "." в строках большими, если нет, заменить на большие;
Вывести получившийся результат на экран
'''

while True:
    a = input("Enter the word or /s: ")
    word = a.split()
    e = "/s"
    dot = "."

    if a == e:
        break

    elif word[0].isupper():  # isupper перевіряє і повертає (а метод upper тільки перевіряє)
        print ("word: ")

    else:
        print (a.title())

    if dot in word and word[0].isupper() == True:
        print ("dskfj")








