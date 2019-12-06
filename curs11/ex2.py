"""1. Create a database for a Zoo, each animal will have following characteristics:
- Name, age, class (mammals, birds, fishes, reptiles),
2. Add following methods:
- Initialization / Creation ( use __init__ method )
- Initialization / creation by date of birth (use class method)
- For each class of animal add methods that will display his favourite food.
- For reptiles add methods for changing color and length of it’s tail attribute.
3. Try to separate type of animals in base / child Class, use inheritance in order to group common animals attributes.
4. Store each new created animal in a list / dictionary, write a function that will find all animals of a certain class"""

import csv
import random
from datetime import datetime
from zipfile import ZipFile

class Zoo:

#- Name, age, class (mammals, birds, fishes, reptiles)
#- Initialization / Creation ( use __init__ method )
    def __init__(self, name, speciesGroup, age):
        self.name = name
        self.speciesGroup = speciesGroup
        self.age = age

#- Initialization / creation by date of birth (use class method)
    @classmethod
    def init_by_date(cls, name, speciesGroup, bday):
        return cls(name, speciesGroup, datetime.today().year - datetime.strptime(bday, '%Y%m%d').year )

    def __str__(self):
        return f'{self.__class__}({self.name}, {self.speciesGroup}, {self.age})'


class Birds(Zoo):

#- For each class of animal add methods that will display his favourite food.
    @staticmethod
    def favourite_food():
        print("Birds' favourite food: \
                \n  -Insects, worms, and grubs \
                \n  -Seeds, grasses, and plant material \
                \n  -Nectar and pollen" )


class Mammals(Zoo):

    @staticmethod
    def favourite_food():
        print("Mammals' favourite food: \
                \n  -Meet and plants" )


class Amphibians_Reptiles(Zoo):

    @staticmethod
    def favourite_food():
        print("Reptiles' favourite food: \
                \n  -Animal and plant matter, including fruits and vegetables" )

    def __init__(self, name, speciesGroup, age, color = 'Green'):
        super().__init__(name, speciesGroup, age)
        self.color = color

#- For reptiles add methods for changing color and length of it’s tail attribute.
    def change_color(self, new_color):
        self.color = new_color



def list_class(dictionary, cls):
    for animal in dictionary:
        if isinstance(dictionary[animal], cls):
            print(dictionary[animal])

def main():

    a1 = Birds('Parrot','Birds', 2)
    print('\n', a1)
    a1.favourite_food()

    a2 = Mammals.init_by_date('Polar bear', 'Mammals', '20170225' )
    print('\n', a2)
    a2.favourite_food()

    a3 = Amphibians_Reptiles('Salamandrina', 'Amphibians_Reptiles', 5)
    print('\n', a3)
    print(a3.__dict__)
    a3.change_color('Brown')
    print('Color', a3.color)
    a3.favourite_food()


    #4. Store each new created animal in a list / dictionary, write a function that will find all animals of a certain class"""
    Animal_dict = {}

    with ZipFile('European_Red_List_2017_December_csv.zip', 'r') as zip: 
        zip.extractall()

    with open('European_Red_List_2017_December.csv', 'r', encoding="utf-8-sig") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            # print(line['taxonomicRankGenus'], line['taxonomicRankSpecies'], line['speciesGroup'])
            if line['speciesGroup'] == 'Birds':
                name = f"{line['taxonomicRankGenus']} {line['taxonomicRankSpecies']}"
                Animal_dict[name] = Birds(name, 'Birds', random.randrange(0,20))
            elif line['speciesGroup'] == 'Mammals':
                Animal_dict[line['scientificName']] = Mammals(line['scientificName'], 'Mammals', random.randrange(0,20))
            elif line['speciesGroup'] == 'Amphibians_Reptiles':
                name = f"{line['taxonomicRankGenus']} {line['taxonomicRankSpecies']}"
                Animal_dict[name] = Amphibians_Reptiles(name, 'Mammals', random.randrange(0,20))

    # print('\n', Animal_dict['Bubo bubo'])
    list_class(Animal_dict, Mammals)

if __name__ == '__main__':
    main()