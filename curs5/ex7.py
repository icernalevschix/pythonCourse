#3. Scrieti un program care calculeaza frecventa cu care apare un cuvint intr-o propozitie.

import re

str1 = input("Introduceti propozitia: \n")
x = input("Introduceti cuvantul cautat: ")

print("Frecventa : {}".format(len(re.findall(x, str1))))