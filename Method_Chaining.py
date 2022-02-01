# method chaining = calling methods sequentially 
#                   each call perfiorms an action on the same object and return self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

# car.turn_on().drive()  #this wont work by itself so you need to put return self under the prints 
# car.brake().turn_off()
#car.turn_on().drive().brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()