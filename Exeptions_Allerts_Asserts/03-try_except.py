try:
    x = 2 / 0
except ZeroDivisionError:
    print('Division by zero detected')

"""
Напишите код в соответствии с инструкциями в задании!
    При a < 0, функция генерирует исключение ValueError с текстом "Invalid argument"
"""
def Sum(a, b):

  if a < 0:
      raise ValueError("Invalid argument")

      return a + b
print("-------------------------------------------------------------------------------")

"""
  При b = 0, функция генерирует стандартное исключение с текстом - "Division by zero"
"""

def div(a, b):

    if b==0:

        raise ZeroDivisionError("Division by zero")
    return a / b

