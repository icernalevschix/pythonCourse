d = {'mese':10,'scaune':21}

itemi = 0
for i in d.values():
    itemi += i

print("itemi = {}".format(list(d.keys())))

print("numarul de itemi = {}".format(itemi))


l = ['apples', 'bananas','cats']

print(','.join(l[:-1]), "and", l[-1])