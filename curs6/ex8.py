
def convertStrToInt(str1):
    try:
        x = float(str1)
    except ValueError:
        print("valoarea introdusa nu este valida")
        return False
    return x

while True:
    convertStrToInt(input("introduceti un numar: ")) 
