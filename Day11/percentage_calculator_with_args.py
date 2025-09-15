from function_definitions import percentage_calculator, division_calculator
        

marks1 = int(input("Enter the marks 1: "))
marks2 = int(input("Enter the marks 2: "))
marks3 = int(input("Enter the marks 3: "))
marks4 = int(input("Enter the marks 4: "))

percentage = percentage_calculator(marks1=marks1, marks2=marks2, marks3=marks3, marks4=marks4)

print(f"The final percentage is {percentage}%")

division = division_calculator(percentage=percentage)

print(f'The final division is {division}')