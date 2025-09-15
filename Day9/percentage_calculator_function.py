def percentage_calculator():
    marks_1 = int(input("Enter the marks 1: "))
    marks_2 = int(input("Enter the marks 2: "))
    marks_3 = int(input("Enter the marks 3: "))

    sum_marks = marks_1 + marks_2 + marks_3
    total_marks = 60 * 3

    percentage = (sum_marks/total_marks)*100
    print(f"The percentage is {percentage}")

    if percentage > 90:
        print("Distinction")
    elif percentage > 80:
        print("First Division")
    else:
        print("Fail")


percentage_calculator()