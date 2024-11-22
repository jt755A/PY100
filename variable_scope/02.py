x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# line 4 creates a local variable: variable shadowing,
# does not look to line 1
# UnboundLocalError