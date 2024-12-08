numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

# half_numbers = [ int(numbers[key] / 2) for key in numbers ]
half_numbers = [ int(value / 2) for value in numbers.values() ]

# half_numbers = []
# for key in numbers:
#     half_numbers += [int(numbers[key] / 2)]

# for value in numbers.values():
#     half_numbers.append(value // 2)


print(half_numbers)


    