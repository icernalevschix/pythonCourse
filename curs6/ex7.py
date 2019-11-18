
def validate(str1):
    if '@' not in str1:
        return False
    if len(str1[str1.rfind('.')+1:])<2:
        return False
    elif len(str1[str1.rfind('@')+1:str1.rfind('.')+1])<2:
        return False
    elif len(str1[:str1.rfind('@')+1])<2:
        return False
    else:
        return True


str1 = input("introduceti adresa de email: ")

while True:
    if(validate(str1)):
        print("adresa este valida")
        break
    else:
        str1 = input("adresa nu este valida, introduceti o alta adresa: ")


