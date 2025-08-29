subject_name_1 = input("Enter the first subject's name: ")
subject_marks_1 = input(f"Enter the marks of {subject_name_1}: ")
subject_full_marks_1 = input(f"Enter the full marks of {subject_name_1}: ")
subject_marks_1 = float(subject_marks_1)
subject_full_marks_1 = float(subject_full_marks_1)

if subject_marks_1 > subject_full_marks_1:
    print("The obtained marks cannot be greater than full marks")

if subject_marks_1 < 40:
    print(f"The student has failed in {subject_name_1}")


subject_name_2 = input("Enter the second subject's name: ")
subject_marks_2 = input(f"Enter the marks of {subject_name_2}: ")
subject_full_marks_2 = input(f"Enter the full marks of {subject_name_2}: ")
subject_marks_2 = float(subject_marks_2)
subject_full_marks_2 = float(subject_full_marks_2)

if subject_marks_2 > subject_full_marks_2:
    print("The obtained marks cannot be greater than full marks")

subject_name_3 = input("Enter the third subject's name: ")
subject_marks_3 = input(f"Enter the marks of {subject_name_3}: ")
subject_full_marks_3 = input(f"Enter the full marks of {subject_name_3}: ")
subject_marks_3 = float(subject_marks_3)
subject_full_marks_3 = float(subject_full_marks_3)

if subject_marks_3 > subject_full_marks_3:
    print("The obtained marks cannot be greater than full marks")


subject_name_4 = input("Enter the fourth subject's name: ")
subject_marks_4 = input(f"Enter the marks of {subject_name_4}: ")
subject_full_marks_4 = input(f"Enter the full marks of {subject_name_4}: ")
subject_marks_4 = float(subject_marks_4)
subject_full_marks_4 = float(subject_full_marks_4)

if subject_marks_4 > subject_full_marks_4:
    print("The obtained marks cannot be greater than full marks")


total_marks = subject_full_marks_1 + subject_full_marks_2 + subject_full_marks_3 + subject_full_marks_4
obtained_marks = subject_marks_1 + subject_marks_2 + subject_full_marks_3 + subject_marks_4
percentage = (obtained_marks/total_marks)*100

print(f"The student has obtained total percentage of {percentage}%")
if percentage > 90:
    print("The student has scored distinction")
elif percentage > 80:
    print("The student has scored first division")
elif percentage > 70:
    print("The student has scored second division")
elif percentage > 60:
    print("The student has scored third division")
elif percentage > 50:
    print("The student has scored fourth division")
else:
    print("The student has failed")