def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n
        
find_first_nonzero_among(0, 0, 1, 0, 2, 0)
# find_first_nonzero_among(1)

# Example 1: TypeError is given: in definition, only 1 argument given.
# However, the set is providing 6 arguments --> more than expected.
# providing a list, tuple would correct issue.

# Example 2, TypeError: 'int' object is not iterable
# integers cannot be iterated over because they are not iterables...
# collections or (strings) would work
