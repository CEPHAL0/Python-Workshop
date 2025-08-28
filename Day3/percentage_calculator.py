mark1 = 10
mark2 = 20
mark3 = 0
mark4 = 0

marks_sum = mark1 + mark2 + mark3 + mark4
total_marks = 60 * 4

percentage = (marks_sum/total_marks) * 100

is_passed = percentage > 40

print(f"The student obtained {percentage} and he is passed: {is_passed}")