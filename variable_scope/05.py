a = 1

def my_function():
    print(a)
    a = 2

my_function()

# prints 1. a is global variable. Furthermore, there is no return
# value in my_function.

# EDIT: no. Throws error: when function is invoked, python runs through
# whole block of code. It see a local assignement of a, which also affects
# the preceding line 4. Cannot print