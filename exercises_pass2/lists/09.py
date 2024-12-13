destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

# def contains(member, lst):
#     for item in lst:
#         if item == member:
#             return True
#     return False

def contains(member, lst):
    index = 0
    while index < len(lst):
        if lst[index] == member:
            return True
        index += 1
    return False

print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))