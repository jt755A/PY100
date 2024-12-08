def last(list):
    return list[-1] if list else None

lst = ['Earth', 'Moon', 'Mars']
emptylst = []

print(last(lst))
print(last(emptylst))