number1 = 86

number1 = input("Enter the marks: ")
number1 = float(number1)


if number1 > 85:
    print("Distinction")
elif number1 > 75:
    print("First Division")
elif number1 > 65:
    print("Second Division")
elif number1 > 55:
    print("Third Division")
else:
    print("Failed")