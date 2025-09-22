class Student:
    name = ""
    age = 0
    address = ""
    section = ""

    # Set values through a function
    def set_values(self, name, age, address, section):
        self.name = name
        self.age = age
        self.address = address
        self.section = section


student1 = Student()

student1.set_values("Sharad", 50, "Kathmandu", "A")

print(student1.name)
print(student1.address)
print(student1.age)


class Student:
    name = ""
    age = 0
    address = ""
    section = ""

    # Set values through a function
    def set_values(self, name, age, address, section):
        self.name = name
        self.age = age
        self.address = address
        self.section = section
    
    def print_values(self):
        print(self.name)
        print(self.address)
        print(self.age)


student1.set_values("Sharad", 50, "Kathmandu", "A")
student1.print_values()


# Constructors

class Vehicle:
    def __init__(self, name, country, wheels, year):
        self.name = name
        self.country = country
        self.wheels = wheels
        self.year = year
    


vehicle1 = Vehicle("Toyota", "Japan", 4, "1800")
print(vehicle1.year)