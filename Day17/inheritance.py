class Cow:
    name = ""
    legs = ""
    food_type = ""
    milk_capacity = ""


class Horse:
    name = ""
    legs = ""
    food_type = ""
    speed = ""

# Parent Class
class Animal:
    name = ""
    legs = ""
    food_type = ""

    def whoami(self):
        print(f"I am {self.name}")

# Child Class
class Cow(Animal):
    milk_capacity = ""

# Child Class
class Horse(Animal):
    speed = ""

cow1 = Cow()
cow1.name = "John"
cow1.legs = "4"
cow1.food_type = "Herbivore"
cow1.milk_capacity = 35

cow1.whoami()