class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("The rabbit is eating a carrot") # thsi overrides the top one

rabbit = Rabbit()
rabbit.eat()