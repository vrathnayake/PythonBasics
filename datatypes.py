machine = 'homePC'
name = 'vindi'
num = None
num2 = True


def add_numbers (a: int, b: int) -> int:
    return a+b

print(float(add_numbers(2, 5)))

print('hello'.replace('e','a'))

print ('Nice to meet you {0}. I am {1}'.format(name,machine))

print (f'Nice to meet you {name}. I am {machine}.')

print (num == None)
print (str(num2)=="True")