# Dunder Methods -> __<name>__
# __init__
# __str__
# __add__
# __sub__
# __mul__
# __eq__
# __lt__
# __gt__
# __lte__
# __gte__


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __str__(self):
        return f"Length: {self.length} Breadth: {self.breadth}"
    
    def area(self):
        return self.length * self.breadth
    
    def __add__(self, rectangle):
        new_length = self.length + rectangle.length
        new_breadth = self.breadth + rectangle.breadth

        new_rectangle = Rectangle(new_length, new_breadth)
        return new_rectangle
    
    def __eq__(self, other):
        area1 = self.area()
        area2 = other.area()

        return area1 == area2

rectangle1 = Rectangle(10, 20)
rectangle2 = Rectangle(5, 40)

print(rectangle1)
rectangle3 = rectangle1 + rectangle2

print(rectangle3.length)
print(rectangle3.breadth)

is_equal = rectangle1 == rectangle2
print(is_equal)