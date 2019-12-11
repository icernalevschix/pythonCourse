from datetime import datetime

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
