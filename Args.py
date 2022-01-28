# *args = parameter that will pack all arguments into a Tuple 
#        useful so that a function can accept a varying amount of arguments 

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def add(*stuff):
    sum = 0
    stuff = list(stuff) #remember Tuples are ordered and unchangeable. So when you add line 14 in without 13 an error occurs. You can cast it to a list because they are changeable. 
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6)) 