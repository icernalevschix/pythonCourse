"""1. Scrieti un program care sa calculeze suma numerelor pare dintr-o lista, folositi
functiile reduce / filter"""

from functools import reduce

a = input("introduceti elementele listei (separate prin spatiu): ").split()
suma = reduce(lambda x,y: int(x) + int(y), filter(lambda x: int(x)%2==0, a))

print("Suma elementelor pare din lista =", suma)