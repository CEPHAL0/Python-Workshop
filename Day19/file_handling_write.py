# Read - r
# Write
    # Append - a
    # Overwrite - w
    # Create - x


f = open("student.txt", "a")

for i in range(3):
    index = i + 6
    name = input("Enter the name: ")
    f.write(f"\n{index}. {name}")

f.close()
