'''
1Предложить пользовательский ввод, где пользователь должен написать любой текст;
Предложить пользовательский ввод, где пользователь может выбрать один из предложенных пунктов:
1 - Вывести текст большими буквами ( метод upper() )
2 - Вывести текст маленькими буквами ( метод lower() )
3 - Вывести количество символов в тексте ( функция len() )
4 - Вывести количество слов в тексте ( метод split() и потом функция len() для получившегося списка )

Пользователь выбирает пункт, вводя 1, 2, 3 или 4.
Взависимости, что ввел пользователь, вывести указанную информацию.
3 -
'''


someText = input("Please input any text: ")
someNumber = int(input("Enter 1 or 2 or 3 or 4: "))

if someNumber == 1:
    print (someText.upper())
elif someNumber == 2:
    print (someText.lower())
elif someNumber == 3:
    print (len(someText))
elif someNumber == 4:
    print (someText.split())
    print(len(someText))
else:
    print("Error occured!. Please enter valid number.")