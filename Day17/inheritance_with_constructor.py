# Parent class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Child Class
class Student(Person):
    def __init__(self, name, age, address, grade, section):

        # Access the constructor from parent class
        super().__init__(name, age, address)

        self.grade = grade
        self.section = section


# Child Class
class Teacher(Person):
    def __init__(self, name, age, address, salary, type):

        # Access the constructor from parent class
        super().__init__(name, age, address)

        self.salary = salary
        self.type = type

student1 = Student("Alice", 15, "KTM", "12", "A")
teacher1 = Teacher("Chandra", 45, "BRT", 45000, "Part Time")