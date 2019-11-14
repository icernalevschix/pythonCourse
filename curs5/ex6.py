"""2. Scrieti un program care verifica daca o parola introdusa de utilizator este
securizata
● Lungimea minima 6 caractere
● Cotine cel putin 1 litera in intervalul [a-z]
● Cotine cel putin 1 litera in intervalul [A-Z]
● Cotine cel putin 1 cifra
● Contine cel putin un caracter special [!, /, #]
● Nu contine caractere interzire [@, ‘, {, }]"""

def secure(str1):
    if len(str1)<6:
        return False

    upper,lower,integer,special = 0, 0, 0, 0

    for i in range(len(str1)):
        if str1[i] in ["@", "‘", "{", "}"]:
            return False        
        elif str1[i].islower():
            lower = 1
        elif str1[i].isupper():
            upper = 1
        elif str1[i].isdigit():
            integer = 1
        elif str1[i] in ["!", "/", "#"]:
            special = 1

    if upper and lower and integer and special:
        return True

str1 = input("introduceti parola: ")

if secure(str1):
    print("parola introdusa este securizata !")
else:
    print("parola nu este securizata !")