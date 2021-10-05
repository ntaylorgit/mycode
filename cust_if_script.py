#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'Your letter grade is: '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your number grade?"))

# if input value was higher or equal to 25
if connection >= 90:
    message = message + ' A. Excellent work.'
elif connection >= 80:
    message = message + ' B. Good job.'
elif connection >= 70:
    message = message + ' C. Good but you can do better.'
elif connection >= 60:
    message = message + ' D. Work a little harder.'
elif connection >= 50:
    message = message + ' F. You are failing;please see me.'

else:
    message = message + 'Please enter a number grade.'
print(message)

