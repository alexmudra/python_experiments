# прилад дуже простої рекурсії
def recursia(a):
    if a == 0:
        return
    print("Result of recurs. func is:", a)
    recursia(a - 1)


recursia(5)
