def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
# number = input()
number = int(input())

print(f"The result is {multiply_by_five(number)}!")

# input from user default to being a string type.
# so the function actually concatenates 1 five times.
# coercing line 5 to numeric type fixes the issue.