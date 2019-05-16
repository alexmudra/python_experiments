"""
написать клас который не возвращает ничего
"""

class MyClass:
    pass #пасс не возвращает ничего

#/////////////////////////////////
"""
Напишите класс MyObject, который содержит поля int_field и str_field со значениями 5 и
“simple string” соответственно. Создайте экземпляры класса MyObject, с названиями obj1 и obj2
"""

# class MyObject:
#     int_field = 5 #атрибути класа
#     str_field = "simple string" #атрибути класа
# obj1 = MyObject() # створили екземпляри класа MyObject
# obj2 = MyObject()

#////////////////////////////////////





"""
Создайте экземпляры класса MyObject с именем obj1 и obj2. Присвойте полю int_field объекта obj1 значение 10,
а полю str_field значение “string2”. Выведите в одной строке значение полей obj1, а во второй строке, значение полей obj2.

"""
#TODO зробити коректно

class MyObject:
    int_field = 5  # атрибути класа
    str_field = "simple string"  # атрибути класа


obj1 = MyObject()  # створили екземпляри класа MyObject
obj2 = MyObject()


obj1.int_field = 10
obj2.str_field = "string2"


print(obj1.int_field)
print(obj2.str_field)



"""
Передати довільні аргументи через args 
"""
def foo(*args, g):
    print(str(g))


foo(1,2,3,4, g = "Kontar")




'''
Опишите класс с именем Person, функция print_info которого выводит на консоль атрибуты name и age. 
Создайте экземпляр класса – john, присвойте атрибуту name значение “John”, а атрибуту age значение 22. 
Запустите функцию print_info() экземпляра john. Запустите функцию print_info() класса Person с параметром 
john.
'''


class Person:
    def print_info(self):#першим параметром будь-якого методу буде self
        print(self.name, self.age)


john = Person() #екземпляр класу Персон

john.name = "John" #переназначаємо значення нейм для об'єкту класу
john.age = 22


john.print_info() #звертаємось напряму до метода екземпляру класу

Person.print_info(john)

#John 22
#John 22

#/////////////////////////////////////////////////////

"""
Напишите метод конструктор класса Person, который будет устанавливать параметры name и age для экземпляров класса Person.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, "is", self.age)


john = Person("John", 22)
lucy = Person("Lucy", 21)

john.print_info()
lucy.print_info()

#John is 22
#Lucy is 21

#//////////////////////////////////////////

"""
Найдите и исправьте ошибку в коде
"""
class MyObject:

    class_attribute = 8

    def __init__(self): # метод в констркторе для создавания атрибута данних
        self.data_attribute = 42 # атрибут данних

    def instance_method(self):# звичайний метод який повертає атрибут данних
        print(self.data_attribute) # повертає дані об'єкта екземпляра self

    @staticmethod # об'являємо статичний метод через декоратор staticmethod
    def static_method():# об'являєм статичний метод без параметра
        print(MyObject.class_attribute)


if __name__ == "__main__": # умова якщо наш метод був запущений як виконуваний файл...
    MyObject.static_method() # визиваємо статичний метод на класі
    obj = MyObject() # створимо екземпляр класу
    obj.instance_method() # визвемо його метод екземпляра класа
    obj.static_method() # визвемо статичний метод

# 8 вивелось значення визову статичного методу на самому класі (вивелось на екран значення атрибуту класу)
# 42 результат визову instance_method ( obj.instance_method()), 42 це результат визову атрибуту даних
# 8 результат визову статичного методу на самому об'єкті


#////////////////////////////////////////////////
"""
Напишете метод класса Triangle, с названием from_rectangle(), 
который будет возвращать равносторонний треугольник со стороной side, равной side_a четырехугольника Rectangle.
"""

# class Rectangle:
#
#     def __init__(self, side_a, side_b): # метод конструктор який приймає 2 параменти: 2 сторони
#         self.side_a = side_a # атрибут данних
#         self.side_b = side_b
#
#     def __repr__(self): # метод __repr__ повертає строкове значення об'єкта. Метод конвертує об'єкт в строку
#         # яке тільки для внутрішнього користування
#         return "Rectangle(%.1f, %.1f)" % (self.side_a, self.side_b)
#
# class Triangle:
#
#     def __init__(self, side):
#         self.side = side
#
#     def __repr__(self):
#         return "Triangle(%.f)" % self.side
#
#     @classmethod
#     def from_rectangle(cls, rectangle):
#         side = rectangle.side_a
#         return cls(side)



"""
Задание
Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.
"""


class Car:
    def __init__(self, type=None, model=None, color=None, prod_year=0, price=0, currency=None):
        self.type = type
        self.model = model
        self.color = color
        self.prod_year = prod_year
        self.price = price
        self.currency = currency

    def print_info(self):
        print("The car has following parameters:", self.type, self.model, self.color, self.prod_year, self.price,
              self.currency)


Mazda = Car("Hechbeck", "CX-7", "Red", 1998, 2000, "USD")
Mazda.print_info()
# The car has following parameters: Hechbeck CX-7 Red 1998 2000 USD


class CarDealerShip:

    car_list = ["car_one", "car_two", "car_three"]

    def __init__(self):
        self.car_list = ["car_one", "car_two", "car_three"]

    @staticmethod
    def show_cars():
        for i in CarDealerShip.car_list:
            print("This is the list of cars in dealership",i)

    def sale_car(self):
        print("The car", + self.show_cars() + "is for sale!")


if __name__ == "__main__":

    CarDealerShip.show_cars()


"""
This is the list of cars in Dealership car_one
This is the list of cars in Dealership car_two
This is the list of cars in Dealership car_three
"""

#Приклади ІНКАПСУЛЯЦІЯ

"""
    Атрибуты, имена которых начинаются, но не заканчиваются, двумя символами
    подчёркивания, считаются приватными. К ним применяется механизм
    «name mangling», суть которого заключается в том, что изнутри класса
    и его экземпляров к этим атрибутам можно обращаться по тому имени,
     было задано при объявлении, однако на самом деле к именам слева добавляется
    подчёркивание и имя класса. Этот механизм не предполагает защиты данных от
    изменения извне, так как к ним всё равно можно обратиться, зная имя класса
    и то, как Python изменяет имена приватных атрибутов, однако позволяет
    защитить их от случайного переопределения в классах-потомках.
"""

#     class MyClass:
#         def __init__(self):
#             self.__private_attribute = 42
#
#         def get_private(self):
#             return self.__private_attribute
#
# obj = MyClass()
# print(obj.get_private())  # 42
# print(obj.__private_attribute)  # ошибка
# # print(obj._MyClass__private_attribute)  # 42



"""
 Создайте класс с именем MyObject и атрибутами с именами: простой - attribute, внутренний - inner_attribute, 
 защищенный - private_attribute и значениями соответственно 2, 3, 4. 
Создайте объект класса c именем obj
Выведите на печать атрибут private_attribute объекта obj
"""


class MyObject:
    def __init__(self):
        self.attribute = 2
        self._inner_attribute = 3
        self.__private_attribute = 4


obj = MyObject()

print(obj._MyObject__private_attribute)


"""
 Используя функции. Напишите геттер с названием get_attribute, 
 для приватного поля   __private_attribute. И сеттер для этого поля с названием set_attribute, который бы устанавливал 
 только положительные значения value переменной. 
"""
class MyObject:
    def __init__(self):
        self.__private_attribute = 0

    def get_attribute(self):
        return self.__private_attribute

    def set_attribute(self, value):
        if value < 100:
            self.__private_attribute = value


obj3 = MyObject()
print(obj3.get_attribute())



