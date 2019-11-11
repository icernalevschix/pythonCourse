def palindrom(str1):
    for i in range(len1):
        if str1[i] != str1[len1-1-i]:
            return False
    return True

while True:
    str1 = input("Introduceti cuvantul: ")
    len1 = len(str1)

    if palindrom(str1):
        print("Cuvantul introdus este palindrom! ")
    else:
        print("Cuvantul introdus nu este un palindrom! ")

    fwd = input("\nDoriti sa testati un alt cuvant(Yes/No): ")
    if fwd[0].lower() == 'n':
        break

