# multiple inheritance = when a child class is derived from more than one parent class
# https://i.ytimg.com/vi/mRIeUXhIAxg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLD7mBMgrXOzPk4Wzym4xcq2abI9Lg

class Prey:

    def flee(self):
        print("The animal flees")

class Predator:

    def hunt(self):
        print("The animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# rabbit.flee()
# hawk.hunt()
fish.flee()
fish.hunt()


