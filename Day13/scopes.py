name = "Kathmandu"

def print_name():
    # Local Scope
    name = "Biratnagar"
    print("Inside the function")
    print(name)

print_name()

print("Outside the function")

# Global Scope
print(name)

def calc_sum(a, b):
    total_sum = a + b
    return total_sum

total_sum = calc_sum(10, 20)
print(total_sum)


balance = 1000

def withdraw(amount):
    # Explicitly make it remember the global scope variable
    global balance

    balance = balance - amount
    print(balance)

withdraw(amount=10)

name = "Sharad"

option = ""
while option == "5":
    # Local Scope
    name = "Sharad"
    print(name)
    option = "5"

# (ERROR) Cannot access value from local scope of while loop
print(name)

percentage = 70

if percentage > 90:
    final_division = "Distinction"
else:
    final = "Fail"

print(final)