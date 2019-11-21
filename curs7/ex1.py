res1 = [x + y for x in 'abc' for y in 'lmn']
print(res1)

res2 = []
for x in 'abc':
    for y in 'lmn':
        res2.append(x + y)
print(res2)

d = {k:v for k,v in enumerate(range(3))}
print(d)

a = {i for i in range(5)}
print(a)

a = (i for i in range(3))
print(a) # generator object
print(next(a)) # 0
print(next(a)) # 1
print(next(a)) # 2

import sys
g = (i for i in range(100000))
l = list(range(100000))
print(sys.getsizeof(g)) # 88
print(sys.getsizeof(l)) # 900112