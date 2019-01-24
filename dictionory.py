student1 = {
'name': 'Mark',
'stud_id': 12345,
'feedback': None

}
student2 = {
'name': 'Ola',
'stud_id': 12355,
'feedback': None

}

list_of_stud = [student1, 
                student2,
                {'name': 'Nilly','stud_id': 13355,'feedback': None}]


print(student1['name'])
print(student1.get('last_name','Unknown'))
print(student1.keys())
print(student1.values())

for stud in list_of_stud:
    print(stud['name'])

try:
    student2['feedback'] = 3 + 'hey'
    print(student1['last_name'])
except KeyError:
    print('EROOR:no last name')
except TypeError as err:
    print('ERROR:Type error')
    print(err)
except Exception as err:
    print('ERROR:Undefined')

print('done')