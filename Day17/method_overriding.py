# Parent class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def print_information(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

# Child Class
class Student(Person):
    def __init__(self, name, age, address, grade, section):

        # Access the constructor from parent class
        super().__init__(name, age, address)

        self.grade = grade
        self.section = section

    # Method Overriding
    def print_information(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Address: {self.address}, Grade: {self.grade}, Section: {self.section}")

# Child Class
class Teacher(Person):
    def __init__(self, name, age, address, salary, type):

        # Access the constructor from parent class
        super().__init__(name, age, address)

        self.salary = salary
        self.type = type

    # Method Overriding
    def print_information(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Address: {self.address} Salary: {self.salary}, Type: {self.type}"
        )


student1 = Student("Alice", 15, "KTM", "12", "A")
teacher1 = Teacher("Chandra", 45, "BRT", 45000, "Part Time")


student1.print_information()
teacher1.print_information()