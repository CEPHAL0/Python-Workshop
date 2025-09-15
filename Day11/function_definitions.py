# Percentage Calculator with arguments
def percentage_calculator(marks1, marks2, marks3, marks4):
    sum_marks = marks1 + marks2 + marks3 + marks4
    total_marks = 60 * 4

    percentage = (sum_marks / total_marks) * 100
    return percentage


def division_calculator(percentage):
    if percentage > 90:
        final_division = "Distinction"
    elif percentage > 80:
        final_division = "First Division"
    elif percentage > 70:
        final_division = "Second Division"
    elif percentage > 60:
        final_division = "Third Division"
    else:
        final_division = "Fail"

    return final_division