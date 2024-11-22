a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# prints 2. Line 4 means that the assignment in line 5 is global.
# When function is invoked in line 7, a is reassigned to 2.