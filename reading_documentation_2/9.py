tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

# line 6 attempts to excecute: tries to concatenate tweet and 5, within
# a call to len function. This expects two str objects.
# 5 is an integer, so is not the expected data type. Unable to execute,
# throws TypeError.