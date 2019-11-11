
fileName = input("Introduceti numele fisierul: ")

print("Extensia: ", fileName[fileName.rfind('.'):])
print("Extensia: ", fileName.split('.')[-1])