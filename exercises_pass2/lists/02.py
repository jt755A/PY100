def last(lst):
    if isinstance(lst, list) == False:
        return 'This is not a list.'
    elif len(lst) == 0:
        return 'The list is empty.'
    else:
        return lst[-1]

print(last(['Earth', 'Moon', 'Mars']))
print(last([]))
print(last({}))