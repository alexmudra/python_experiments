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