students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student['name'].title())
    return students_titlecase

def print_student_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id= 333):
    student = {'name': name, 'id': student_id}
    students.append(student)

def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student.strip())
        f.close()
    except Exception:
        print("Could not read file" )




read_file()
print_student_titlecase()

yes_no = 'yes'

while yes_no == 'yes':
    student_name = input ("Enter name:")
    student_id = input("Enter ID:")
    add_student(student_name, student_id)
    save_file(student_name)

    yes_no = input("do you whish to enter another student? [yes/no] ")



