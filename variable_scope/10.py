b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# prints [1, 2, 3]. b in line 1 is unaffected.
# Line 7 shadows the variable: mutates the local variable only.
# Global variable is unaffected.

# EDIT Wrong
# Lists are mutable, and line 4 mutates the collection