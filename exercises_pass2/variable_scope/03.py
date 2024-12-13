def my_function():
    a = 1

    if True:
        print(a)

my_function()

# prints 1.
# line 4: if blocks runs because True is truthy. 
# It prints a, which is defined in local scope.