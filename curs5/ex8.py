# 4. Scrieti un program care sa elimine cuvinte duplicate dintr-o propozitie.

str1 = input("Introduceti propozitia: \n").split()

print(" ".join([i for n,i in enumerate(str1) if i not in str1[:n]]))
