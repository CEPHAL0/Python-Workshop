def bmi_calculator():
    mass = float(input("Enter the weight of user in kg: "))
    height = float(input("Enter the height of user in cm: "))

    bmi = (mass / height)**2

    print(f"The BMI of user is {bmi}")


bmi_calculator()