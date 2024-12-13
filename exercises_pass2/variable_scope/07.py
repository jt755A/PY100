a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# prints 2. line 4 means any subsequent references to a pull/push to the
# global scope