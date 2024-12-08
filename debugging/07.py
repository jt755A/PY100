info = {'name': 'Srdjan', 'age': 38}

# print(info['city'])
# print(info.get('city', '"Unknown"'))

# if 'city' in info:
#     print(info['city'])
# else:
#     print('Unknown')

print(info['city']) if 'city' in info else print('Unknown')
