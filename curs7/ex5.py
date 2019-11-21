z = zip([1,2,3], ["a", "b", "c"])
print(z)
print(next(z))
print(list(z))

z = zip([1,2,3,4], ["a", "b", "c"])
for i in z:
    print(i)

from functools import reduce
a = [1,2,3,4]
b = reduce(lambda x, y: x * y, a)
print(b)

a = [1,2,3,4,5,6,7,8]
b = reduce(lambda x, y: x * y, (
    map(lambda x: x + 10, (
        filter(lambda x: x % 2 == 0, a)))
        )
    )
print(b)