students = ['mark', 'justin', 'ola', 'alex', 'alex']

print (students[1])

students[2] = 'john'

students.append ('jessica')

print (students[-1])

if 'mark' in students:
    print('he is there')

print (len(students))

print(students.count('alex'))

students.remove('jessica')
print(students.count('jassica'))
print(students.pop())

print (students)

print (students[1: -1])
