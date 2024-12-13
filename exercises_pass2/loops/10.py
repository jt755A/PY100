while True:
    print('Should I stop looping?')
    answer = input().casefold().strip()
    if answer == 'yes':
        break
    print('Try again')