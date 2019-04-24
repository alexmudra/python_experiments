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

    @staticmethod # об'являємо статичний метод
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
