f = open("student.txt", "r")
# Read the whole file as a single sentence
value = f.read()
print(value)
f.close()

f = open("student.txt", "r")
# Read only the first 9 characters
first_values = f.read(9)
print(first_values)
f.close()


f = open("student.txt", "r")
# Read the whole line
first_line = f.readline()
second_line = f.readline()
print(first_line)
print(second_line)
f.close()