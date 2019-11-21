#2. Scrieti o functie generator care sa lucreze ca functia enumerate (yield)
import random

def fn1():
    for i in range(100):
        yield i, random.randrange(555)

x = fn1()
print(x)
print(next(x))
print(list(x))