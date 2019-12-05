"""1. Declare a class that will describe a Car with following attributes, year, fuel
type, color. Add to your class methods for calculating car’s age, retrieving fuel
type and setting new color."""

import datetime

class Car:

    def __init__(self, year, fuel, typeC, color):
        self.year = year
        self.fuel = fuel
        self.type = typeC
        self.color = color

    def calc_age(self):
        self.year = datetime.datetime.today().year - self.year

    def get_fuel_type(self):
        return self.type

    def set_color(self, new_color):
        self.color = new_color

    def __repr__(self):
        return 'Car({},{},{},{})'.format(self.type, self.year, self.fuel, self.color)

car1 = Car(2011,'Hybrid','HatchBack','Brown')
print(car1)

car1.calc_age()
print(car1)
print(car1.get_fuel_type())

car1.set_color('Gray')
print(car1)
