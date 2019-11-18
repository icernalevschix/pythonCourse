# 2. Scrieti o functie care sa calculeze produsul elementelor unei liste.

def fn2(l1):
    produs = l1[0]
    for i in l1[1:]:
        produs*=i
    return produs

print(fn2([1,5,-10]))