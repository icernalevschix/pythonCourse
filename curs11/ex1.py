"""Create 3 classes Car / Electric car / Diesel car. Car class will have following attributes: color, age. Diesel and Electric car classes will inherit from Car class.
Diesel car will have by default fuel type: diesel and electric car will have fuel type li-on bateries by default. Create a metod for counting all Diesel / Electric car on creation. 
Add a method in Car class that will display number of created Diesel and Electric cars."""

class Car:

    electric_cars = 0
    diesel_cars = 0

    def __init__(self, color, age):
        self.color = color
        self.age = age

#2nd method - remove init method from subclasses & uncomment the below code
        # if isinstance(self, ElectricCar):
        #     Car.electric_cars+=1
        # if isinstance(self, DieselCar):
        #     Car.diesel_cars+=1

    def __str__(self):
        return f'Car({self.color},{self.age})'

    @classmethod
    def display_cars(cls):
        return f'Diesel: {cls.diesel_cars}\nElectric: {cls.electric_cars}'

class ElectricCar(Car):

    fuel_type = 'li-on bateries'

    def __init__(self, color, age):
        super().__init__(color, age)
        Car.electric_cars += 1

    def __del__(self):
        Car.electric_cars -= 1
        del self

class DieselCar(Car):

    fuel_type = 'diesel'

    def __init__(self, color, age):
        Car.__init__(self, color, age)
        Car.diesel_cars += 1

    def __del__(self):
        Car.electric_cars -= 1
        del self


e1 = ElectricCar('white', 7)
e2 = ElectricCar('white', 7)
print(e1)
print('e fuel type -', e1.fuel_type)

d1 = DieselCar('black', 9)
d2 = DieselCar('black', 5)
print('d fuel type -', d1.fuel_type)

print(Car.display_cars())

del e1
try:
    print(e1)
except NameError as e:
    print(f"{e} // the object does not exist !")
finally:
    print(Car.display_cars())