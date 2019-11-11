def convert(scara,temp):
    if scara == 'c':
        print("Temeratura dupa conversie (in grade Fahrenheit) = {}".format((temp*1.8)+32))
    elif scara == 'f':
        print("Temeratura dupa conversie (in grade Celsius) = {}".format((temp - 32)/1.8))

def main():

    while True:

        conv = input("\nUnitatea de masura initiala(Celsius/Fahrenheit): ")

        if conv[0].lower() == 'c':
            x = float(input("Introduceti temperatura: "))
            convert('c', x)
        elif conv[0].lower() == 'f':
            x = float(input("Introduceti temperatura: "))
            convert('f', x)

        fwd = input("\nDoriti sa efectuati o alta conversie(Yes/No): ")
        if fwd[0].lower() == 'n':
            break

main()