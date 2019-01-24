
students = []

class Student:

    school_name = "Springfield Collage"

    def __init__(self, name, student_id= 333):
        self.name = name
        self.student_id = student_id
        students.append(self)       

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalized(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name



class HighSchoolStudent (Student):
    school_name = 'Springfield_highschool'

    def get_school_name(self):
        return "This method is overidden"

    def get_name_capitalized(self):
        org_val = super().get_name_capitalized()
        return org_val + "-HS"


james = HighSchoolStudent('james')
print(james.get_name_capitalized())
print(james.get_school_name())