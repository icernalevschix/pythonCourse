"""4. Scrieti o functie care primeste 2 parametri, 1 functie si o lista, rezultatul
returnat trebuie sa fie lista modificata de fuctie:
In: def my_fync(lambda x: x*x, [1, 2, [3, 4, [5]]])
Out: [1, 4, [9, 16, [25]]]"""

def fn1(l1, f = lambda x: x*x):
    return map(f,l1)

a = [1, 2, 3, 4, 5]

print(list(fn1(a)))
print(list(fn1(a, lambda x: x + x)))
