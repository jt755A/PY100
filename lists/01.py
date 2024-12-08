def first(list):
    return list[0] if list else None
        
    

lst = ['Earth', 'Moon', 'Mars']
emptylst = []
print(first(lst))
print(first(emptylst))