speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# prints True



# Don't need the parentheses to print True in this case,
# but this will change the order of operation, and can affect values.

# equivalent to:
is_moving = (braking_force < acceleration and speed > 0) or acceleration > 0