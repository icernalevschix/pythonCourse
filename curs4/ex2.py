a = [1,2,4]

print((1 + 2 == 3) or (10 < 20) and (77 + 8) and 7 in a)

import copy
a = [1, 2, [2, 3]]
b = copy.copy(a)
print("***")
print(a[2] is b[2])
print(a is b)
print("***")
b = a
print(a[2] is b[2])
print(a is b)
print("***")
c = copy.deepcopy(a)
print(a[2] is c[2])

a = {"name": "Alice", "age": 44, "profile":
{"occupation": "student"}}
b = copy.copy(a)
c = copy.deepcopy(a)
print(a is b)
print(a["profile"] is b["profile"])
print(a["profile"] is c["profile"])