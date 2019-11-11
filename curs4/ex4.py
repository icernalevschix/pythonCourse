def fn1():
    a = input("\nintroduceti numele fisierului: ")
    extension = a.split('.')[-1]
    if a.find('.') == -1:
        print("numele fisierului nu are o extensie")
    elif extension != 'py':
        print(extension)
    else:
        print('OK') 

while True:
    fn1()
    new = input("\nDoriti sa introduceti un alt nume de fisier(Yes/No): ")
    if new.lower()[0]=='n':
        break
