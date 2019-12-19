raise Exception('some error occurred')


try:
    raise ValueError
except ZeroDivisionError:
    print("division by zero is prohibited")

