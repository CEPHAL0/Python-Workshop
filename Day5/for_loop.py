name = input("Enter your name: ")

number_of_greetings = int(input("Enter the number of times you want to be greeted: "))

for counter in range(10, number_of_greetings):
    print(f"Hello {name}, {counter} times")