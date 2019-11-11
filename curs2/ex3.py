
class Student:

    def __init__(self):
        self.nume = input("Nume: ")
        self.prenume = input("Prenume: ")
        self.varsta = int(input("Varsta: "))
        self.ocupatie = input("Ocupatie: ")

    def afisare(self):
        print("\nNume:    {:>25}".format(self.nume))
        print("Prenume: {:>25}".format(self.prenume))
        print("Varsta:  {:>25}".format(self.varsta))
        print("Ocupatie:{:>25}".format(self.ocupatie))


def main():

    studList = []

    while True:
        x = Student()
        studList.append(x)

        new = input("\nDoriti sa introduceti datele unui nou student(Da/Nu)? ")
        
        if (new[0].lower()) != 'd':
            break

    for st in studList:
        st.afisare()

if __name__ == '__main__':
    main()