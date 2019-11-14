# 1. Scrieti un program care sa calculeze numarul de litere si cifre din un text.

str1 = input("introduceti textul: ")
litere,cifre = 0, 0

for i in enumerate(str1):
    if i[1].isdigit():
        cifre+=1
    elif i[1].isalpha():
        litere+=1
    
print("\nNumarul de litere: {} \nNumarul de cifre: {}".format(litere,cifre))
