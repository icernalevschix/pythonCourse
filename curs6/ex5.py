# 1. Scrieti o functie care calculeaza daca un numar este prim.

def prim(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

while True:
    x = prim(int(input("introduceti numarul: ")))

    if x:
        print("numarul este prim")
        break





