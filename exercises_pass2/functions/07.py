my_string = 'Captain Ruby'
# python_string = my_string.replace('Ruby', 'Python')
# print(python_string)

split = my_string.split()
split[1] = 'Python'
python_string = ' '.join(split)
print(python_string)

# index = my_string.find('Ruby')
# result = my_string[:index] + 'Python'
# print(result)