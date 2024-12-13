a = 1

def my_function():
    print(a)
    a = 2

my_function()

# prints 2: line 5 assigns a within function scope (line order doesn't matter)

# EDIT line order does matter