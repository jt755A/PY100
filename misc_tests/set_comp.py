a = (1, 2, 3)
b = ('a', 'b', 'c')

# set1 = { x * 2 for x in b }
# print(set1)

c = zip(a, b)

mydict = { a: ord(b) for a, b in c }
print(mydict)
