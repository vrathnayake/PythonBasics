from student import Student


class HighSchoolStudent (Student):
    school_name = 'Springfield_highschool'

    def get_school_name(self):
        return "This method is overidden"

    def get_name_capitalized(self):
        org_val = super().get_name_capitalized()
        return org_val + "-HS"
