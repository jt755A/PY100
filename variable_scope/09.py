a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# prints 7.
# line 6: local variable is created that takes a's value in line 1,
# and adds 7. However, there's no return value. Variable a remains
# unaffected.