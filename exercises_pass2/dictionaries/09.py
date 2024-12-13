numbers = {
    'high': 100,
    'medium': 50,
    'low': 25,
}

half_numbers = []
for value in numbers.values():
    half_numbers.append(value // 2)
# for key, value in numbers.items():
#     half_numbers.append([key, value // 2])


# half_numbers = { key: value // 2 for key, value in numbers.items() }
# half_numbers = {}
# for key, value in numbers.items():
#     half_numbers[key] = value // 2


# half_numbers = [ value // 2 for value in numbers.values() ]

print(half_numbers)
print(type(half_numbers))