"""6. Scrieti un program care sa primeasca la input un numar N intreg si sa creeze
un dictionar care contine numer mai mici sau egale decit N si N*2. Ex(4 - > {1:
1, 2: 4, 3: 9, 4: 16})"""

x = int(input("introduceti numarul: "))
dictionar = {}

for i in range(1,x+1):
    dictionar[i] = i*i

print(dictionar)