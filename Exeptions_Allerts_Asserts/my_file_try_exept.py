"""
 При a < 0, функция генерирует исключение ValueError с текстом "Invalid argument"
"""
def Sum(a, b):

   try:
       a < 0:
   except ValueError:
       print("Invalid argument")

       return a + b
