import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()

# line 4 generates a value each time invoked, which is passed to if block.
# The if block in line 6 checks if sunshine is truthy.
# Any non-empty string is truthy, so sunshine will always be returned.
# To correct this, removing the '' string literal syntax notation fixes the issue.
# Now booleans are passed to the line 6, which will evalutate correctly.