number = 5
message = 'hello'
none = None
a = 10
b = 20

if number == 5:
    print('number is 5')
else:
    print('number is not 5')

if number:
    print("Number is integer and not empty")

if message:
    print("message is not empty and is a str")

if none:
    print("print this is none is true")

if number or message:
    print('both are true')

"""Ternary"""

print ('bigger' if a > b else 'smaller')