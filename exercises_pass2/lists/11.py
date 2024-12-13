grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

grocery_tup = tuple(grocery_list)
for item in grocery_tup:
    grocery_list.remove(item)
    print(item)

# while grocery_list:
#     checked_item = grocery_list.pop(0)
#     print(checked_item)
    # EDIT: this block is the launch school solution

print(grocery_list)

