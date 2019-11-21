import sys

a = [1,2,3,4,100,200,2,43,34,232,423,2143,53,43,43,4,2,3,0,254,1,765,7,5,3]
b = map(lambda x: x + 10, a)
print(b)
print(list(b))

b = map(lambda x: x + 10, a)
d = list(b)
print(sys.getsizeof(d))
print(d)

print(sys.getsizeof(b))
print(sys.getsizeof(list(b)))

c = [x + 10 for x in a]
print(sys.getsizeof(c))

# filter

a = [1,2,3,4]
b = filter(lambda x: x % 2 == 0, a)
print(b)
for i in b:
    print(i)