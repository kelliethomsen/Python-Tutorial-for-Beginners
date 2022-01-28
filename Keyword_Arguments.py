# keyword arguements = arguments preceded by an identified when we pass then to a function.
#                      The oder of the arguments doesn't matter, unlike positional arguments.
#                      Python knows the name of the arguments that our function receives

def hello(first, middle, last):
    print("Hello, " + first + " " + middle + " " + last)

hello (last = "Thomsen", middle = "Madison", first = "Kellie")
