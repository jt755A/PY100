animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')


# iterates through case conditions in order until it finds the value assigned to
# match statement; at this point it will exit the block.
# In this case, it will print 'neigh'