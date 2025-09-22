# Create a class named Rectangle with its necessary attributes
# Add methods called area and perimeter that returns the calculated value
# Create objects and print the area and perimeter using the objects method call

# Area = length * breadth
# Perimeter = 2(length + breadth)

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    # Area Method
    def area(self):
        calculated_area = self.length * self.breadth
        return calculated_area
    
    # Perimeter Method
    def perimeter(self):
        calculated_per = 2 * (self.length + self.breadth)
        return calculated_per

rectangle1 = Rectangle(20, 30)
area = rectangle1.area()
perimeter = rectangle1.perimeter()

print(f"The area is {area} and perimeter is {perimeter}")

rectangle2 = Rectangle(80, 100)
area = rectangle2.area()
perimeter = rectangle2.perimeter()

print(f"The area is {area} and perimeter is {perimeter}")
