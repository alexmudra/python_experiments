def div (a, b):
    if b == 0:
        raise Exception ("Division by zero is prohibited")
    return a / b


def division (a,b):
    return div (a,b)

def test_try ():
    while True:
        a = float(input("enter a: "))
        b = float(input("enter b: "))

        try:
            x = division(a,b)
            print(x)
        except Exception as ex:
            print(ex)

#test_try()