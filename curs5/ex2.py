#4. Scrieti un program care sa afiseze toti divizorii unui numar intreg.

divizori = []
x = int(input("introduceti numarul intreg: "))

for i in range(1,x+1):
    if x % i == 0:
        divizori.append(i)

print(divizori)