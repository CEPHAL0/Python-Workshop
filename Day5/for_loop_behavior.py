names = ["Alex", "Jonas", "Priya", "Layne"]
for name in names:
    print(name)

marks = [24, 20, 33, 34, 90, 45, 44]

sum = 0
total_marks = 0
for mark in marks:
    sum = sum + mark
    total_marks = total_marks + 60 # Assume 60 is the full marks

percentage = (sum/total_marks)*100
print(f"The percentage is {percentage}")