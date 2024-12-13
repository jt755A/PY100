def first(lst):
    if isinstance(lst, list) == False:
        return 'This is not a list.'
    elif len(lst) == 0:
        return 'The list is empty.'
    else:
        return lst[0]

print(first(['Earth', 'Moon', 'Mars']))
print(first([]))
print(first({}))