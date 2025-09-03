person = {
    "name": "",
    "address": "",
    "languages": [],
    "hobbies": []
}

person["name"] = input("Enter the name: ")
person["address"] = input("Enter the address")

number_of_languages = int(input("Enter the number of languages that you know: "))

for number in range(number_of_languages):
    language = input(f"Enter the {number + 1} language: ")
    person["languages"].append(language)


number_of_hobbies = int(input("Enter the number of hobbies that you know: "))

for number in range(number_of_hobbies):
    hobby = input(f"Enter the {number + 1} hobby: ")
    person["hobbies"].append(hobby)

for key, value in person.items():
    print(f"{key}: {value}")