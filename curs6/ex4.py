"""4. Scrieti o functie care sa intoarca elementele distincte dintr-o lista
Ex ([1,2,3,3,3,3,4,5] - > [1, 2, 3, 4, 5]) """

def fn1(l1):
    return set(l1)

print(fn1((input("introduceti o lista ( elementele separate prin spatiu): ").split())))

