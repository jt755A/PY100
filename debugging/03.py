def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()
# number = int(input())

print(f"The result is {multiply_by_five(number)}!")

# When a user is prompted to enter input, the input is a string type.
# So, the return expression in line 2 concatenates the text n times.
# changing line 5 to number = int(input()) fixes issue.