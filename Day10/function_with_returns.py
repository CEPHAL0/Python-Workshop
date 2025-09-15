def percentage_calculator():
    marks_1 = int(input("Enter the marks 1: "))
    marks_2 = int(input("Enter the marks 2: "))
    marks_3 = int(input("Enter the marks 3: "))

    sum = marks_1 + marks_2 + marks_3
    total_sum = 60 * 3

    percentage = (sum/total_sum) * 100
    return percentage


percentage = percentage_calculator()


print(f"The percentage is {percentage}")