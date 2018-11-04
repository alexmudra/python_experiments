# -*- coding: utf-8 -*-
'''
Напишите программу которая в цикле ожидает последовательного ввода 10 чисел по отдельности
добавляет из в список а после єтого сортирует данний список и печатает его умножив каждое число на 10
'''

a = int(raw_input("Enter the 10 words: "))
b = []
e = "exit"
for i in range(len(a)):
    b.append(a[i])
print("List contains such elements: ", b)
b.sort()
print("Sorted list:", b)

prod = [i * 10 for i in b]

print(prod)