

# Normal Class
class Grade:
    def __init__(self, name):
        self.name = name

# Nested Class
class Student:
    def __init__(self, name, age, address, grade):
        self.name = name
        self.age = age
        self.address = address
        self.grade = grade

grade1 = Grade("12")
student1 = Student("John", 22, "NYC", grade1)