a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# prints 7. Line 6 invokes my_function on a resulting in 17.
# However, this only happens in the local scope of the function.
# Global status of a is unaffected.