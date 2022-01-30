class Car:

    wheels = 4                  #class variables

    def __init__(self, make, model, year, colour):
        self.make = make        #instance variables
        self.model = model      #instance variables
        self.year = year        #instance variables
        self.colour = colour    #instance variables

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.wheels = 2

print(car_1.wheels)
print(car_2.wheels)

