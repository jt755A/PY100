a = 1

def my_function():
    print(a)

my_function()

# throws NameError: a in line 4 is not defined in local scope.

# EDIT: line 1 is globally available. Only an issue if a new assignment
# takes place within new function: variable shadowing.