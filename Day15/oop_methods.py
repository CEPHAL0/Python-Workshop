# Class Definition
class Student:
    # Attributes
    percentage = 0.0
    name = ""
    grade = 0
    section = ""

    # Methods
    def is_passed(self):
        if self.percentage > 40:
            print("pass")
        else:
            print("fail")
    
    def greet_student(self):
        print(f"Hello {self.name}, you are from grade {self.grade} and section {self.section}")

student1 = Student()
student1.percentage = float(input("Enter the percentage: "))
student1.name = input("Enter the name: ")
student1.grade = int(input("Enter the class of student: "))
student1.section = input("Enter the section of student: ")

student1.is_passed()
student1.greet_student()