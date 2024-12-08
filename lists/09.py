destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

# def contains(city,list):
#     string = ','.join(list)
#     if string.find(city) == -1:
#         return False
#     else:
#         return True

# print(contains('Barcelona', destinations))
# print(contains('Nashville', destinations))

def contains(city, collection):
    if city in collection:
        return True
    else:
        return False

print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))
