#OBJECT ORIENTED

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def averge_grades(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (90, 90, 93, 78, 90))
student2 = Student("Luis", (100, 98, 93, 78, 80))
print(student.averge_grades())
print(student2.averge_grades())