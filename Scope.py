# Scope = The region that a variable is recongised
#         A variable is only available from the inside that region it is created.
#         A global and locally scoped version of a variable can be created.

name = "Kellie" # global scope (available inside & outside functions)

def display_name():
    name = "Thomsen" # local scope (available only inside this function)
    print(name)

display_name()
print(name)
