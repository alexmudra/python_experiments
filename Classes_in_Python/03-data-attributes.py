# Атрибуты-данные аналогичны полям в терминологии большинства
# распространённых языков программирования.
# Атрибуты-данные не нужно описывать: как и переменные,
# они создаются в момент первого присваивания.


# Класс, описывающий человека
class Person:
    pass


# Создание экземпляров класса

alex = Person()
alex.name = 'Alex'
alex.age = 36

john = Person()
john.name = 'Tania'
john.age = 33

# Атрибуты-данные относятся только к отдельным экземплярам класса
# и никак не влияют на значения соответствующих атрибутов-данных
# других экземпляров
print(alex.name, 'is', alex.age)
print(john.name, 'is', john.age)