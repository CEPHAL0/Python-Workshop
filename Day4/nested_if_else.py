height = float(input("Enter the height (in cms): "))
weight = float(input("Enter the weight (in kgs): "))

if height > 180:
    if weight < 50:
        print("Underweight")
    elif weight > 100:
        print("Overweight")
    else:
        print("Healthy")
elif height > 160:
    if weight < 40:
        print("Underweight")
    elif weight > 80:
        print("Overweight")
    else:
        print("Healthy")