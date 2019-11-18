# 1. Scrieti o functie care sa gaseasca maximum a 3 numere

def max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max(10,3,-100))