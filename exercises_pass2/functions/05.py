def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three

#EDIT: no output because function is never invoked

# prints:
# 3 / 1 = 3
# 6 / 2 = 3
# ....
# 30 / 10 = 3