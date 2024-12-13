dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['b'] = 42

# print(f'dict1 value = {dict1['b']}')
# print(f'dict2 value = {dict2['b']}')
# print(dict2['b'])

print(dict1.get('c', 'Nothing!'))