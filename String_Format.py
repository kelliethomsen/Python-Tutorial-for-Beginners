# string format() = optional method that gives users more control when displaying output

number = 1000

print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))

#another one...

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format("cow","moon"))
#or
print("The {} jumped over the {}".format(animal,item))
#or 
print("The {1} jumped over the {0}".format(animal,item)) #positional argument
#or
text = "The {} junped over the {}"
print(text.format(animal,item))
