# 3. Scrieti o functie care sa calculeze numarul de litere majuscule si minuscule dintr-un text

def fn1(str1):
    majuscule,minuscule = 0, 0

    for i in str1:
        if i.isupper():
            majuscule+=1
        elif i.islower():
            minuscule+=1
        
    print("\nNumarul de majuscule: {} \nNumarul de minuscule: {}".format(majuscule,minuscule))

fn1(input("Introduceti textul: "))
