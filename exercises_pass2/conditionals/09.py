speed = 0
acceleration = 24
braking_force = 19

is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# braking_force < acceleration == True

# (speed > 0) == False
# acceleration > 0 == True
# (False or True) == True

# final equation is True and (False or True)

# True and True
# 
# Prints True as result of print(is_moving)


# Bonus q: parantheses not needed for these static conditions, but other values will make a difference:
# and has higher precedence than or (inside the parantheses)