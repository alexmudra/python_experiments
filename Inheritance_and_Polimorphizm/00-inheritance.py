# -*- coding: utf-8 -*-

"""
Пример наследования классов
"""

class Figure(object):
    def __init__(self, side):
        self.side = side


class Square(Figure):
    def draw(self):
        for i in range(self.side):
            print('*' * self.side)


class Triangle(Figure):
    def draw(self):
        for i in range(self.side):
            print('*' * i)


def main():
    square = Square(10)
    square.draw()

    print()

    triangle = Triangle(5)
    triangle.draw()


if __name__ == '__main__':
    main()


"""
  Опишите два класса Base и его наследника Child с методами method(), который выводит на консоль фразы соответственно
    "Hello from Base" и "Hello from Child"  

"""
class Base:
    def method(self):
        print("Hello from Base")

class Child(Base):
    def method(self):
        print("Hello from Child")

base_inst = Base()
base_inst.method()

child_inst = Child()
child_inst.method()

#Hello from Base
#Hello from Child



"""
  Создайте класс Child, наследник класса Base, который содержит метод child_method(), выводящий на консоль
   фразу "Hello from child method!" и переопределяющий метод базового класса выводящий на консоль фразу 
   "Hello from redefined method!"
"""

class Base:
    def method(self):
        print("Hello!")


class Child(Base):
    def child_method(self):
        print("Hello from child method!")

    def method(self):
        print("Hello from redefined method!")

base_instance = Base()
base_instance.method()

child_instance = Child()
child_instance.child_method()
child_instance.method()

#Hello from child method!
#Hello from redefined method!


"""
 Дан базовый класс Figure, опишите два класса наследника Square и Triangle, методы draw() 
 которых будут выводит side знаков ‘* ‘  в side строках, рисуя при этом квадрат  и соответственно  треугольник. 
 Используйте последовательности для вывода знаков ‘* ‘ и переменную-счётчик ‘i‘.
 """

class Figure:
    def __init__(self, side=0.0):
        self.side = side


class Square(Figure):
    def draw(self):
        for i in range(self.side): # передаємо сюди конструктор классу Figure
            print('* ' * self.side)

class Triangle(Figure):
    def draw(self):
        for i in range(1, self.side + 1):# передаємо сюди конструктор классу Firure
            print('* ' * i)

def main(): #створимо екземпляри класу в головній функції, щоб код був чистішим
    square = Square(10)
    square.draw()

    print("==============separator====================")

    triangle = Triangle(5)
    triangle.draw()


if __name__ == '__main__':
    main()
"""
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
==============separator====================
* 
* * 
* * * 
* * * * 
* * * * * 
"""



"""
  Опишите класс Pegasus, который является наследником классов Horse и Bird и умеет, и бегать и летать.
"""

class Horse:
    def run(self):
        print("I'm running.")

class Bird:
    def fly(self):
        print("I'm flying.")

class Pegasus(Horse,Bird):#приклад множественного наследования
    pass

def main():
    pegasus = Pegasus()
    pegasus.fly()
    pegasus.run()

if __name__ == main():
    main()