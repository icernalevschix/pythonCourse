def my_generator(n):
    while n < 10:
        yield n
        n += 1

# for i in my_generator(0):
#     print(i)

g = my_generator(8)
print(g)
print(next(g))

# iterators

import sys
a = list(range(100000))
i = iter(range(100000))
print(sys.getsizeof(a)) # 900112
print(sys.getsizeof(i))

a = iter([1, 2, 3])

for i in a:
    print(i)

a = iter([1, 2, 3])

while True:
    try:
        print(next(a))
    except StopIteration:
        break

l = iter([1, 2, 3])
d = iter({"name": "Alice", "age": 32})
s = iter({1, 2, 3})
t = iter((1,2,3,3))
st = iter("spam")