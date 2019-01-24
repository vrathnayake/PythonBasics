students = ['anna', 'david', 'john', 'ola', 'bill']

for name in students:
    print(f'hello {name} wellcome to your new class!')

x = 0

for index in range(1,10, 2):
    x += 10
    if x == 30:
        continue
        print("i am 30")
    print(f'value of x is {x}')

x = 50

while x > 10:
    print("hello")
    if x == 70 :
        break
    x += 10
