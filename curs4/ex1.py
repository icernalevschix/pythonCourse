a = 1
b = a

print(id(a))
print(id(b))


a = [1, 2, 3, 4]
b = a
b[0] = 5
print(a) # [5, 2, 3, 4]
print(b) # [5, 2, 3, 4]
print(id(a)) # 140459448017288
print(id(b)) # 140459448017288

a = [[1, 2], 2, 3, 4]
b = a.copy()
# b[0][0] = 10
print(a) # [[10, 2], 2, 3, 4]
print(b) # [[10, 2], 2, 3, 4]
print(id(a)) # 140123304644680
print(id(b)) # 140123304644808

print(1 == "1")