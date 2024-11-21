def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three


# '3 / 1 = 3'
# '6 / 2 = 3'
# ...
# '30 / 10 = 3'

#EDIT: no return value: because never invoked. (Missing parentheses)