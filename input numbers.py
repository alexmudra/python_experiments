# -*- coding: utf-8 -*-

# a = int(input("Input quantity: "))
# b = int(input("Input price: "))
# c = int(input("Input discount: "))
# d = a * b
# print ("Final sum", d )
#
# if c >= b:
#     print ("Error")
# else:
#     a

quantity_of_goods = int(input("Количество товара: "))
p = int(input("цена : "))
d = int(input("скидка : "))
s = p * quantity_of_goods
pd = s * d // 100
if d > s and d > 0:
    print('error')
else:
    print(s - pd)

# Використання методу формат для запису характеристик кота в один рядок
# present = 'Ur cat was be {0}, and {1}, and {2}, and {3}'.format(q, w, e, r)
# print(present)

