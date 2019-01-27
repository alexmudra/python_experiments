# прилад дуже простої рекурсії
def recursia(a):
    if a == 0:
        return
    print("Result of recurs. func is:", a)
    recursia(a - 1)


recursia(5)

'''
Result of recurs. func is: 5
Result of recurs. func is: 4
Result of recurs. func is: 3
Result of recurs. func is: 2
Result of recurs. func is: 1
'''