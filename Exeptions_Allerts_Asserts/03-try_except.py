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
