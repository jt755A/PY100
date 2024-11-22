a = 1

def my_function():
    a = 2

my_function()
print(a)

# prints 1. Line 1 is global variable.
# Line 4 means variable shadowing occurs whenever invoked, however there
# is no return value to my_function