text = 'Captain Ruby'
# print(text.replace('Ruby', 'Python'))

mylist = text.split(' ')
mylist[1] = 'Python'
result = ' '.join(mylist)
print(result)
