numbers = {
    'high': 100,
    'medium': 50,
    'low': 10,
}

for key, value in numbers.items():
    # print(f'A {key} number is {value}.')
    print('A {0} number is {1}.'.format(key, value))