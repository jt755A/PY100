b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# prints 10, 2, 3
# lists are mutable, line 4 mutates the original list using a function
# b is not a local variable, so python looks to the outer scopes to find
# the variable.