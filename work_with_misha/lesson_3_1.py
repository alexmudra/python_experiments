#перебрати 2вомірний масив

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
"""
1 2 3 4 
5 6 
7 8 9
"""


A = {'ab' : 'ba', 'aa' : 'aa', 'bb' : 'bb', 'ba' : 'ab'}

print(A['ab'])

for i in A:
    print(A[i])
#роздрукували значення


for i in A:
    print(i)
#роздрукували ключі




b = {'a' : 'ff', 'b' : 'tt', 'g' : 'ee', 'l' : 'oo'}

w = (list(b.keys()))
print("Друкуємо ключі в list",w)
#сортуємо ключі ліста
w.sort()
print(w)

for i in w:
    print(i, b[i])

try_items = b.items()
print(try_items)