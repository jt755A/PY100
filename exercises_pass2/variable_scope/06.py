a = 1

def my_function():
    a = 2

my_function()
print(a)

# prints 1. a is defined in global scope on line 1.
# a = 2 is only valid within the function block.