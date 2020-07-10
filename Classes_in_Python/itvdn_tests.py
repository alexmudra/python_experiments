# Создайте экземпляры класса MyObject с именем obj1 и obj2. Присвойте полю int_field объекта obj1 значение 10,
# а полю str_field значение “string2”.
# Выведите в одной строке значение полей obj1,
# а во второй строке, значение полей obj2.

class MyObject:
    pass

obj1 = MyObject()
obj2 = MyObject()


obj1.int_field = 10
obj2.str_field = "string2"


print(obj1.int_field)
print(obj2.str_field)


# Опишите класс с именем Person, функция print_info которого выводит на консоль атрибуты name и age.
# Создайте экземпляр класса – john, присвойте атрибуту name значение “John”,
# а атрибуту age значение 22. Запустите функцию print_info() экземпляра john.
# Запустите функцию print_info() класса Person с параметром john.

class Person:
    def print_info:
        print(name, age)

john = Person ()
name = "John"
age = 22

print_info(john.name)
print_info(Person.john)

#https://itvdn.com/ru/video/python-essential 48 minutes



