def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

# find_first_nonzero_among(0, 0, 1, 0, 2, 0) # 1 argument expected, 6 given
find_first_nonzero_among(1) #

# 1: TypeError: too many arguments were given in line 6. Cannot execute.
# 2  TypeError 'int' object is not iterable. 
# integers are immutable and singular: i.e. not collections. They cannot be indexed,
# or loop through