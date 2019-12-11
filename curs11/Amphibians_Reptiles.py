from Zoo import Zoo

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
