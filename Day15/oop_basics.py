# Functional Programming

# OOP - Object Oriented Programming


# Class, Object

# Class is a representation of a real world object with its own attributes or properties

# Class Definition Syntax
class Person:
    # Attributes
    name = ""
    age = 0
    address = ""
    height = 0
    weight = 0

# Create an object from class
person1 = Person()

# Access the value of object
print(person1.name)
print(person1.address)

# Manipulate the value of object
person1.name = input("Enter the new name: ")
print(person1.name)

# Create a new object and access its value
person2 = Person()
print(person2.name)

