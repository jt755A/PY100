def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        # print(product)
        product *= digit
    
    return product

result = digit_product('12345')
print(result)

# changed 0 to 1 in line 3