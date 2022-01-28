# **kwargs = parameter that will pack all arguments int a dictionary
#            useful so that a function can accept a varying amount of keyword arguments  

def hello(**kwargs):

    print("hello", end = " ")
    for key, value in kwargs.items():
        print(value, end = " ")

hello(title = "Miss.", first = "Kellie", middle = "Madison", last = "Thomsen")