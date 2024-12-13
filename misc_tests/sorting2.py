letters = ['a', 'b', 'c', 'd',]
numbers = [1, 2, 3, 4, 79, 80, 5,]
num_lett = {1: 'a', 26: 'z', 10: 'j'}
set1 = {'a', 'z', 'e', 'm'}

print(num_lett)
num_lett_keys = sorted(num_lett, key=int)

num_lett_values = []
for value in num_lett.values():
    num_lett_values.append(value)
num_lett_values.sort()

print(num_lett_values)

# print(num_lett)
