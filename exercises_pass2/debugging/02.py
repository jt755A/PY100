import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()

# line 6: if block runs if sunshine is truthy. Any non-empty string is truthy:
# 'True' and 'False' are both truthy strings.
# therefore else block will never run, output will remain the same.

# changing the choices in sunshine to Booleans fixes the issue.

