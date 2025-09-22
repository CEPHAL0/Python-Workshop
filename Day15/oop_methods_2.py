# Class Definition
class Student:
    # Attributes
    percentage = 0.0
    name = ""
    grade = 0
    section = ""

    # Methods
    # Set the value of the class using external values
    def set_name(self, n):
        self.name = n

student1 = Student()
print("Before calling the function")
print(student1.name)

value = input("Enter the name of student: ")

# Call the function with external parameters, arguments
student1.set_name(n=value)
print("After calling the function")
print(student1.name)


class Bank:
    name = ""
    currency_reserve = 0

    def set_currency_reserve(self, c):
        self.currency_reserve = c * 132

bank1 = Bank()

bank1.name = input("Enter the name of bank: ")
input_value = int(input("Enter the currency reserve: "))
bank1.set_currency_reserve(c=input_value)

print(bank1.name)
print(bank1.currency_reserve)