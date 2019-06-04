"""
 При a < 0, функция генерирует исключение ValueError с текстом "Invalid argument"
"""
def Sum(a, b):

    if a < 0:

        raise ValueError ("Invalid argument")

    return a + b


"""
Напишите код в соответствии с инструкциями в задании!
    При a < 0, функция генерирует исключение ValueError с текстом "Invalid argument"
"""
def Sum(a, b):

  if a < 0:
      raise ValueError("Invalid argument")

      return a + b
print("-------------------------------1------------------------------------------------")

"""
  При b = 0, функция генерирует стандартное исключение с текстом - "Division by zero"
"""

def div(a, b):

    if b==0:

        raise ZeroDivisionError("Division by zero")
    return a / b

print("--------------------------------2-----------------------------------------------")

"""
 При type(arg) == type('str'), функция генерирует стандартное исключение с текстом "unsupported operand type"
"""
# def Exp(arg):
#
#     if type(arg) == type('str'):
#         raise TypeError("unsupported operand type")
#     return arg ** 2
#
# print(Exp("skdjfkjsd"))

"""
    raise TypeError ("unsupported operand type")
TypeError: unsupported operand type
"""

print("--------------------------------3-----------------------------------------------")


# try:
#     raise  ValueError
# except ZeroDivisionError:
#     print("division by zero is prohibited")

print("--------------------------------4-----------------------------------------------")


"""
 Обработайте ошибку деления на ноль. В случае деления на ноль, функция выдает на консоль слово “Infinity”
"""


def Div(a, b):
    a = 5
    b = 0

    try:
        result = a / b

    except ZeroDivisionError:
        return print("Infinity")

#TODO доробити код


print("--------------------------------5-----------------------------------------------")



try:
    pass
except:
    pass
except Exception1:
    pass
except Exception2, Exception3, Exception4:
    pass
except Exception5 as exception:
    pass
finally:
    pass
else:
    pass