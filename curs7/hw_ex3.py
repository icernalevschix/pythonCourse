"""3. Scrieti un program care transforma o lista cu elemente compuse intr-o lista
simpla ( [1, [2, 3, [4, 5]]] -> [1,2,3,4,5] )"""

from functools import reduce

a = [1, [2, 3, [4, [5, 6]]]]

print(type(a[1]))
print(type(a[1]) == list)

l2 = []

def fn1(l1):
    for i in l1:
        if isinstance(i,list):
            fn1(i)            
        else:
            l2.append(i)

fn1(a)
print(l2)

# print(reduce(lambda x, y: list(x) + list(y) , a))
