import math

def calcArea(raza):
    return raza*raza*math.pi

def main():
    area = calcArea(float(input("Introduceti raza cercului: ")))
    print("Area cercului = {} unitati".format(area))

main()