# 2. Scrieti o functie care afiseaza o secventa de numere Fibonacci

# from functools import lru_cache
# @lru_cache(maxsize = 1000)

# def fibonacci(x):
#     if x == 0:
#         return 0
#     elif x == 1 or x == 2:
#         return 1
#     else:
#         return (fibonacci(x-2) + fibonacci(x-1))

# print(fibonacci(50))

#**************************************

# cache = {}
# def fibonacci_cache(x):

#     if x in cache:
#         return cache[x]

#     if x == 0:
#         result = 0
#     elif x == 1 or x == 2:
#         result = 1
#     else:
#         result = fibonacci_cache(x - 2) + fibonacci_cache(x - 1)

#     cache[x] = result
    
#     print(cache)
#     return result

# print(fibonacci_cache(50))

#****************************************

x = int(input("cate numere va avea sirul Fibonnaci ? "))
fibonacci = [0,1]

if x == 1:
    fibonacci = [0]

for i in range(x-2):
    nextF = fibonacci[i] + fibonacci[i+1]
    fibonacci.append(nextF)

print(fibonacci)