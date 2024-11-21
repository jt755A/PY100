weather = input("What's the weather like today? ").casefold()
match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('Grab your umbrella.')
    case 'stormy':
        print("Don't hide under a tree.")
    case 'snowy':
        print('Bring your snow shoes!')
    case _:
        print("Let's stay inside.")